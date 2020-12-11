# Native modules
import os
import argparse

# Custom modules
from ImageProcessor import *


# Define the command line arguments
argParser = argparse.ArgumentParser()

argParser.add_argument("-t", "--train", help="Image colorizer training switch", action='store_true')
argParser.add_argument("--training-set", help="Folder containing the training images")

argParser.add_argument("-c", "--colorize", help="Colorize image", action='store_true')
argParser.add_argument("-i", "--input_image", help="Image to try to colorize")
argParser.add_argument("-o", "--output_image", help="Output file for the colorized image")
argParser.add_argument("--use-graphcuts", help="Graph cuts algorithm switch", action='store_true')

# Parse the command lind arguments
args = argParser.parse_args()

if args.train:
    training_images = glob.glob('{}/*'.format(args.training_set))
    
    # Check if all required directories exist
    if not os.path.exists('./objects'): os.mkdir('objects')
    if not os.path.exists('./datasets'): os.mkdir('datasets')

    GenerateColorPaletteDataset(training_images, 'objects/ColorPalette.object')
    GenerateFeatureDataset(training_images, 'objects/ColorPalette.object', 'datasets/Features.dataset')
    GenerateSVMDataset('datasets/Features.dataset', 'objects/PCA.object', 'objects/StandardScaler.object', 'datasets/ReducedFeatures.dataset')
    TrainSVM('datasets/ReducedFeatures.dataset', 'objects/OvR_SVM.object')
    exit()

if args.colorize:
    test_image_infile = args.input_image
    test_image_outfile = args.output_image
    use_graphcuts = args.use_graphcuts

    ColorizeImage(test_image_infile, test_image_outfile, 'objects/ColorPalette.object', 'objects/PCA.object', 'objects/StandardScaler.object', 'objects/OvR_SVM.object', use_graphcuts=use_graphcuts)
    exit()