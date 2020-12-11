from sklearn.cluster         import KMeans, MiniBatchKMeans                                     # Usage: Color palette
from sklearn.model_selection import RepeatedKFold, RepeatedStratifiedKFold, train_test_split    # Usage: SVM training
from sklearn.preprocessing   import StandardScaler, MinMaxScaler                                # Usage: SVM training
from sklearn.metrics         import accuracy_score                                              # Usage: SVM training
from sklearn.multiclass      import OneVsRestClassifier                                         # Usage: SVM training
from sklearn.decomposition   import PCA                                                         # Usage: SVM training
from sklearn.svm             import SVC, LinearSVC                                              # Usage: SVM training
from skimage.color           import rgb2lab, lab2rgb                                            # Usage: RGB->LAB & LAB->RGB
from skimage.segmentation    import slic, mark_boundaries                                       # Usage: SLIC
from skimage.util            import img_as_float                                                # Usage: Convert image color type from uint8 to float
from pygco                   import cut_simple_vh, cut_simple                                   # Usage: Graph Cuts
import cv2                                                                                      # Usage: Image load / SURF / Gabor
import numpy                                                                                    # Usage: Calculations
import matplotlib.pyplot as plt                                                                 # Usage: Image display
import joblib                                                                                   # Usage: Load/Dump objects
import pandas                                                                                   # Usage: Load/Dump objects
import glob                                                                                     # Usage: List files in directory


# Disable warnings
import warnings
warnings.filterwarnings("ignore")



# ================= #
#  Misc. Functions  #
# ================= #

def ListFiles(directory):
	return glob.glob('{}/*'.format(directory))

def LoadImage(path):
	return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)

def DisplayImage(image, grayscale=False, label='Image'):
	figure = plt.figure(label)
	axis = figure.add_subplot(1, 1, 1)
	axis.imshow(image)
	plt.axis("off")
	plt.show()



# ============ #
#  Converters  #
# ============ #

def RGB2LAB(image):
	return rgb2lab(image / 255)

def LAB2RGB(image):
	return (lab2rgb(image) * 255).astype(numpy.uint8)



# =============== #
#  Color Palette  #
# =============== #

def GenerateColorPalette(n_clusters=8, random_state=100, compute_labels=True):
	return MiniBatchKMeans(n_clusters=n_clusters, random_state=random_state, compute_labels=compute_labels)

def EnrichColorPalette(palette, image):
	palette.partial_fit(numpy.vstack(image[:, :, 1:3]))



# =================== #
#  Superpixels: SLIC  #
# =================== #

def SLIC(image, nSegments=600, sigma=5):
	return slic(img_as_float(image), convert2lab=False, n_segments=nSegments, sigma=sigma)

def HighlightSegments(image, segments):
	return mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments)

def DisplaySegments(image, segments, label='Segments'):
	figure = plt.figure(label)
	axis = figure.add_subplot(1, 1, 1)
	axis.imshow(HighlightSegments(image, segments))
	plt.axis("off")
	plt.show()



# ========================== #
#  Feature Extraction: SURF  #
# ========================== #

def SURF(image, segment, threshold=400, nOctaves=3, nKeypoints=10, window=20):
	surf = cv2.xfeatures2d.SURF_create(hessianThreshold=threshold, nOctaves=nOctaves)

	keypoints = [cv2.KeyPoint(y, x, window) for (x,y) in segment]
	keypoints = sorted(keypoints, key=lambda x: -x.response)[:nKeypoints]

	keypoints, description = surf.compute(image, keypoints)

	if len(keypoints) > 0: description = description.flatten()
	else:                  description = numpy.array([])

	FeatureVectorSize = (nKeypoints * 64)

	if description.size < FeatureVectorSize:
		description = numpy.concatenate([description, numpy.zeros(FeatureVectorSize - description.size)])

	return (keypoints, description)

def DisplaySURF(image, keypoints):
	img = cv2.drawKeypoints(image, keypoints, None)
	DisplayImage(img)
	#cv2.imshow("SURF Image", img)
	#cv2.waitKey(delay=5000)
	#cv2.destroyAllWindows()



# =========================== #
#  Feature Extraction: Gabor  #
# =========================== #

def LocalEnergy(image):
	return numpy.sum(numpy.square(image))

def MeanAmplitute(image):
	return numpy.sum(numpy.absolute(image))

def Gabor(image, theta_range=[0, numpy.pi/6, numpy.pi/4, numpy.pi/3, numpy.pi/2, 2*numpy.pi/3, 3*numpy.pi/4, 5*numpy.pi/6], scale_range=[3, 6, 13, 28, 58]):
	features = ([], [])

	for scale in scale_range:
		for angle in theta_range:
			gabor = cv2.getGaborKernel(ksize=(20, 20), sigma=scale, theta=angle, lambd=7, gamma=0.9, psi=1.5, ktype=cv2.CV_32F)
			filtered = cv2.filter2D(image, cv2.CV_8UC3, gabor)
			features[0].extend([LocalEnergy(filtered)])
			features[1].extend([MeanAmplitute(filtered)])

	return features



# ======================= #
#  Dataset Preprocessing  #
# ======================= #

'''
Color Palette Generation:
	1. Extract the colors of each train image
	2. Enrich the color palette with the new colors
	3. Save the color palette for future use
'''
def GenerateColorPaletteDataset(images, outfile):
	print('# ========================== #')
	print('#  Color Palette Generation  #')
	print('# ========================== #')
	print('')

	# Generate the color palette
	palette = GenerateColorPalette()

	# Enrich the color palette
	print('[+] Color Extraction:')
	for image in images:
		print('\t[*] Extracting colors from image: {}'.format(image))
		EnrichColorPalette(palette, RGB2LAB(LoadImage(image)))
	
	# Save the color palette
	print('')
	print('[+] Saving the color palette at: {}\n'.format(outfile))
	joblib.dump(palette, outfile)


'''
Feature Generation:
	- Load the pre-calculated color palette
	- For each train image:
		- Convert the train image to LAB
		- Split the train image to superpixels using the SLIC algorithm
		- For each superpixel:
			- Extract the colors (A & B)
			- Find the dominant color
			- Extract the SURFT features
			- Extract the Gabor features
			- Associate the final feature vector {SURF, Gabor} with the corresponding color class of the dominant color in the color palette
	- Save the feature vectors for future use
'''
def GenerateFeatureDataset(images, palette_infile, outfile):
	print('# ==================== #')
	print('#  Feature extraction  #')
	print('# ==================== #')
	print('')

	dataset = None

	# Load the color palette
	print('[+] Loading the pre-calculated color palette from: {}'.format(palette_infile))
	palette = joblib.load(palette_infile)

	print('')
	print('[+] SURF & Gabor feature extraction:')
	for image in images:
		print('\t[Image: {}]:'.format(image))

		# Load the current image and convert it to LAB
		print('\t\t[*] Converting to LAB color space')
		train_image_rgb = LoadImage(image)
		train_image_lab = RGB2LAB(train_image_rgb)

		# Split the image into segments (superpixels)
		print('\t\t[*] Splitting the image into superpixels')
		segments = SLIC(train_image_lab)

		# Count the generated segments (for printing purposes)
		segmentCount = len(list(enumerate(numpy.unique(segments))))

		print('\t\t[*] Superpixel processing:')
		for (index, segment) in enumerate(numpy.unique(segments)):
			print('\t\t\tSuperpixel: {:3d}/{:3d} | Dominant Color Extraction: {:7s} | SURF Feature Extraction: {:7s} | Gabor Feature Extraction: {:7s}'.format(index+1, segmentCount, 'Pending', 'Pending', 'Pending'), end='\r')

			# Isolate the current superpixel
			mask = numpy.zeros(train_image_rgb.shape[:2], dtype="uint8")
			mask[segments == segment] = 255
			superpixel = cv2.bitwise_and(train_image_lab, train_image_lab, mask=mask)

			# Get the superpixel colors
			superpixel_colors = pandas.DataFrame(numpy.vstack(superpixel[segments == segment, 1:3]), columns=['A', 'B'])

			# Cluster the superpixel's colors with KMeans
			kmeans = KMeans(n_clusters=5, n_init=4, max_iter=100, n_jobs=1)
			kmeans.fit(superpixel_colors.values)

			# Find the dominant color of the current superpixel
			superpixel_colors['labels']     = kmeans.labels_
			superpixel_dominant_label       = superpixel_colors['labels'].value_counts().index[0]
			superpixel_dominant_color       = superpixel_colors.loc[superpixel_colors['labels'] == superpixel_dominant_label].apply(lambda x: x.median())[['A', 'B']]
			superpixel_dominant_color_class = palette.predict(superpixel_dominant_color.values.reshape(1,-1))

			print('\t\t\tSuperpixel: {:3d}/{:3d} | Dominant Color Extraction: {:7s} | SURF Feature Extraction: {:7s} | Gabor Feature Extraction: {:7s}'.format(index+1, segmentCount, 'Done', 'Pending', 'Pending'), end='\r')

			# Construct the color feature
			color_vector = numpy.array(superpixel_dominant_color_class[0])

			# SURF feature extraction
			surf_vector = SURF(numpy.uint8(train_image_lab[:, :, 0]), numpy.argwhere(segments == segment))[1]
			print('\t\t\tSuperpixel: {:3d}/{:3d} | Dominant Color Extraction: {:7s} | SURF Feature Extraction: {:7s} | Gabor Feature Extraction: {:7s}'.format(index+1, segmentCount, 'Done', 'Done', 'Pending'), end='\r')

			# Gabor feature extraction
			gabor_vector = numpy.hstack(Gabor(numpy.uint8(superpixel[:, :, 0])))
			print('\t\t\tSuperpixel: {:3d}/{:3d} | Dominant Color Extraction: {:7s} | SURF Feature Extraction: {:7s} | Gabor Feature Extraction: {:7s}'.format(index+1, segmentCount, 'Done', 'Done', 'Done'), end='\r')

			# Construct the final feature vector for the current superpixel
			feature_vector = numpy.hstack((surf_vector, gabor_vector, color_vector))

			# Update the dataset
			if dataset is None: dataset = numpy.array(feature_vector)
			else:               dataset = numpy.row_stack((dataset, feature_vector))

			# All superpixels have been processed
			if segmentCount == index + 1:
				print('\t\t\tSuperpixel: {:3d}/{:3d} | Dominant Color Extraction: {:7s} | SURF Feature Extraction: {:7s} | Gabor Feature Extraction: {:7s}'.format(index+1, segmentCount, 'Done', 'Done', 'Done'))
		
		print('')

	# Save the training dataset
	print('[+] Saving the extracted features at: {}\n'.format(outfile))
	dataset = pandas.DataFrame(dataset)
	dataset.to_pickle(outfile)


'''
Feature Dimensionality Reduction:
	- Load the pre-calculated features
	- Perform the dimensionality reduction
	- Save the reduced features for future use
'''
# Feature dimensionality reduction
def GenerateSVMDataset(features_infile, pca_outfile, stdscaler_outfile, dataset_outfile):
	print('# ================================== #')
	print('#  Feature Dimensionality Reduction  #')
	print('# ================================== #')
	print('')

	print('[+] Loading the pre-calculated features from: {}'.format(features_infile))
	features = pandas.read_pickle(features_infile)

	print('[+] Generating the PCA (Principal Component Analysis)')
	pca = PCA(n_components=64, svd_solver='auto', random_state=100)

	print('[+] Generating the standard scaler')
	stdScaler = StandardScaler()

	print('[+] Perfoming the dimensionality reduction')
	X_scaled  = stdScaler.fit_transform(features.iloc[:,:-1].values)
	X_pca     = pca.fit_transform(X_scaled)
	features  = pandas.DataFrame(numpy.column_stack((X_pca, features.iloc[:,-1].values)))

	print('')
	print('[+] Saving the PCA at: {}'.format(pca_outfile))
	joblib.dump(pca, pca_outfile)

	print('[+] Saving the standard scaler at: {}'.format(stdscaler_outfile))
	joblib.dump(stdScaler, stdscaler_outfile)

	print('[+] Saving the reduced features at: {}\n'.format(dataset_outfile))
	features.to_pickle(dataset_outfile)



# ============== #
#  SVM training  #
# ============== #

'''
SVM Training:
	- Load the pre-calculated reduced features
	- Create an OvR (one vs rest) SVM classifier
	- Create a repeated K-Fold cross validator
	- Train the OvR SVM classifier
	- Save the OvR SVM classifier for future use
'''
def TrainSVM(infile, outfile):
	print('# ================== #')
	print('#  OvR SVM training  #')
	print('# ================== #')
	print('')

	# Read the pre-calculated reduced features
	print('[+] Loading the pre-calculated reduced features from: {}'.format(infile))
	dataset = pandas.read_pickle(infile)

	# Create an OvR (one vs rest) SVM classifier
	print('[+] Generating the OvR SVM classifier')
	svm = SVC(kernel='rbf', gamma='scale', cache_size=700, random_state=110)
	OvR = OneVsRestClassifier(svm, n_jobs=-1)
	OvR_accuracy = []

	# Create a repeated K-Fold cross validator for the OvR SVM training
	print('[+] Generating a repeated K-Fold cross validator')
	rkf = RepeatedKFold(n_splits=10, n_repeats=2, random_state=100)
	X = dataset.iloc[:,:-1].values
	Y = dataset.iloc[:,-1].values

	# Train the OvR SVM classifier
	print('')
	print('[+] Training progress:')

	step = 1
	for train_index, test_index in rkf.split(X):
		X_train, X_test = X[train_index], X[test_index]
		Y_train, Y_test = Y[train_index], Y[test_index]

		OvR.fit(X_train, Y_train)
		accuracy = round(OvR.score(X_test, Y_test) * 100, 3)
		print ('\t[Step: {:2d}] OvR SVM Classifier Accuracy: {} %'.format(step, accuracy))

		# Add the current accuracy with the rest
		OvR_accuracy.append(accuracy)

		step += 1

	print('')
	print('\tMax. OvR SVM Classifier Accuracy: {} %'.format(max(OvR_accuracy)))
	print('\tMin. OvR SVM Classifier Accuracy: {} %'.format(min(OvR_accuracy)))

	# Save the OvR SVM classifier for future use
	print('')
	print('[+] Saving the OvR SVM classifier at: {}'.format(outfile))
	joblib.dump(OvR, outfile)



# ==================== #
#  Image Colorization  #
# ==================== #

def ColorizeImage(image_infile, image_outfile, palette_infile, pca_infile, stdscaler_infile, svm_infile, use_graphcuts=False):
	print('# ==================== #')
	print('#  Image Colorization  #')
	print('# ==================== #')
	print('')

	# Load the color palette
	print('[+] Loading the color palette ..... Resource: {}'.format(palette_infile))
	palette = joblib.load(palette_infile)

	# Load the PCA
	print('[+] Loading the PCA ............... Resource: {}'.format(pca_infile))
	pca = joblib.load(pca_infile)

	# Load the standard scaler
	print('[+] Loading the standard scaler ... Resource: {}'.format(stdscaler_infile))
	stdscaler = joblib.load(stdscaler_infile)
	
	# Load the trained OvR SVM classifier
	print('[+] Loading the OvR SVM ........... Resource: {}'.format(svm_infile))
	OvR = joblib.load(svm_infile)

	# Load the test image
	print('[+] Loading the test image ........ Resource: {}\n'.format(image_infile))
	image_rgb = LoadImage(image_infile)

	# Convert the test image from RGB to LAB
	print('[+] Converting the test image from RGB to LAB color space')
	image_lab = RGB2LAB(image_rgb)

	# Convert the test image from LAB to grayscale LAB
	image_lab_L = image_lab[:, :, 0]

	# Split the test image into segments (superpixels)
	print('[+] Splitting the test image to superpixels')
	image_lab_segments = SLIC(image_lab[:, :, 0])
	image_lab_segments_count = len(list(enumerate(numpy.unique(image_lab_segments))))

	# Create a grayscale image of the test image (in LAB)
	colorized_image = numpy.zeros_like(image_lab)
	colorized_image[:, :, 0] = image_lab_L

	print('[+] Colorizing the test image:')

	# Colorize the image without using the graph cuts
	if not use_graphcuts:
		print('\t[*] Using graph cuts: NO')

		for (index, segment) in enumerate(numpy.unique(image_lab_segments)):
			print('\t[*] Colorizing superpixel: {:3d}/{:3d}'.format(index+1, image_lab_segments_count), end='\r')

			# Isolate the current superpixel from the test image (in LAB)
			mask = numpy.zeros(image_lab_L.shape, dtype="uint8")
			mask[image_lab_segments == segment] = 255
			superpixel = cv2.bitwise_and(image_lab_L, image_lab_L, mask=mask)

			# Extract the SURF & Gabor features of the current superpixel
			superpixel_surf_vector = SURF(numpy.uint8(image_lab_L), numpy.argwhere(image_lab_segments == segment))[1]
			superpixel_gabor_vector = numpy.hstack(Gabor(numpy.uint8(superpixel)))

			# Generate the current superpixel's vector
			superpixel_vector = pca.transform(stdscaler.transform(numpy.hstack((superpixel_surf_vector, superpixel_gabor_vector)).reshape((1,-1))))

			# Predict the superpixel's color class
			predicted_color_class = OvR.predict(superpixel_vector)[0]

			# Get the A & B color values from the predicted color class
			predicted_color_A = palette.cluster_centers_[int(predicted_color_class)][0]
			predicted_color_B = palette.cluster_centers_[int(predicted_color_class)][1]

			# Colorize the respective superpixel in the blank image with the predicted color
			colorized_image[image_lab_segments == segment, 1:3] = numpy.array([predicted_color_A, predicted_color_B])
		print('')

	# Colorize the image using the graph cuts
	else:
		print('\t[*] Using graph cuts: YES')

		label_costs = numpy.zeros((image_lab_L.shape[0], image_lab_L.shape[1], len(OvR.classes_)))

		for (index, segment) in enumerate(numpy.unique(image_lab_segments)):
			print('\t[*] Generating the graph matrix from the SVM Margins: {:3d} %'.format(int(round(((index+1) / image_lab_segments_count)*100))), end='\r')

			# Isolate the current superpixel from the test image (in LAB)
			mask = numpy.zeros(image_lab_L.shape, dtype="uint8")
			mask[image_lab_segments == segment] = 255
			superpixel = cv2.bitwise_and(image_lab_L, image_lab_L, mask=mask)

			# Extract the SURF & Gabor features of the current superpixel
			superpixel_surf_vector = SURF(numpy.uint8(image_lab_L), numpy.argwhere(image_lab_segments == segment))[1]
			superpixel_gabor_vector = numpy.hstack(Gabor(numpy.uint8(superpixel)))

			# Generate the current superpixel's vector
			superpixel_vector = pca.transform(stdscaler.transform(numpy.hstack((superpixel_surf_vector, superpixel_gabor_vector)).reshape((1,-1))))

			# Get SVM margins to estimate confidence for each color class
			predicted_margins = -1* OvR.decision_function(superpixel_vector).flatten()
			label_costs[image_lab_segments == segment] = predicted_margins
		print('')

		# Calculate the image edges
		print('\t[*] Calculating the edges using the sobel filter')
		blur_width = 3
		sobel_blur = 5
		
		sobelX = cv2.Sobel(image_lab_L, cv2.CV_64F, 1, 0, ksize=sobel_blur)
		sobelY = cv2.Sobel(image_lab_L, cv2.CV_64F, 0, 1, ksize=sobel_blur)
		
		image_lab_L_edges = numpy.hypot(sobelX, sobelY)
		image_lab_L_edges = image_lab_L_edges / numpy.max(image_lab_L_edges)

		# Use graph cuts on the label costs
		color_classes = OvR.classes_
		color_classes_count = len(OvR.classes_)
		color_map = palette.cluster_centers_

		pairwise_costs = numpy.zeros((color_classes_count, color_classes_count))
		for i in range(color_classes_count):
			for j in range(color_classes_count):
				print('\t[*] Calculating the pairwise costs between the color labels: {:3d} %'.format(int(round((((i*color_classes_count + j + 1) / color_classes_count**2)*100)))), end='\r')
				iColor = numpy.array(color_map[int(i)])
				jColor = numpy.array(color_map[int(i)])
				pairwise_costs[i,j] = numpy.linalg.norm(iColor - jColor)
		print('')		

		label_costs_int32 = (100 * label_costs).astype(numpy.int32)
		pairwise_costs_int32 = (100 * pairwise_costs).astype(numpy.int32)

		edgesX_int32 = image_lab_L_edges.astype(numpy.int32)
		edgesY_int32 = image_lab_L_edges.astype(numpy.int32)

		print('\t[*] Calculating the final color labels using the graph cuts algorithm')
		graphcuts_labels = cut_simple_vh(label_costs_int32, pairwise_costs_int32, edgesY_int32, edgesX_int32, n_iter=10, algorithm='swap')

		# Calculate the final A and B colors
		image_lab_A = numpy.zeros_like(image_lab_L)
		image_lab_B = numpy.zeros_like(image_lab_L)

		for i in numpy.arange(graphcuts_labels.shape[0]):
			for j in numpy.arange(graphcuts_labels.shape[1]):
				print('\t[*] Predicting the A and B color layers for the test image: {:3d} %'.format(int(round((((i*graphcuts_labels.shape[1] + j + 1) / (graphcuts_labels.shape[0]*graphcuts_labels.shape[1]))*100)))), end='\r')
				predicted_color_class = color_classes[graphcuts_labels[i,j]]
				predicted_color_A = palette.cluster_centers_[int(predicted_color_class)][0]
				predicted_color_B = palette.cluster_centers_[int(predicted_color_class)][1]

				image_lab_A[i,j] = predicted_color_A
				image_lab_B[i,j] = predicted_color_B
		print('')

		# Merge the L, A and B colors for the final colorized image
		print('\t[*] Merging L, A and B color layers together')
		colorized_image = numpy.dstack((image_lab_L, image_lab_A, image_lab_B))

	print('')

	# Convert the colorized image back to RGB
	print('[+] Converting the colorized image back to the RGB color space')
	colorized_image_rgb = LAB2RGB(colorized_image)

	# Display the colorized image
	if input('[+] Display image? (y/n) ').lower() in ['y', 'yes']:
		DisplayImage(colorized_image_rgb)

	# Save the colorized image
	print('[+] Saving the colorized image at: {}'.format(image_outfile))
	cv2.imwrite(image_outfile, cv2.cvtColor(colorized_image_rgb, cv2.COLOR_RGB2BGR))
