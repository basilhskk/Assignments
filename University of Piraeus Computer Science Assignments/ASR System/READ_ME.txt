Run guide for the scripts: asr.py, neural_network.py, dataset.py 

Speakers on our dataset: ['theo,'yweweler','jackson', 'nicolas']


Automatic speech recognition (asr.py):

	Predict single .wav file: python asr.py -a [filename] #filename πρέπει να είναι στον ίδιο φάκελο
	Predict multiple .wav file: python asr.py -a [foldername] #foldername πρέπει να είναι στον ίδιο φάκελο
	
	.wav file must have name format of: [number_sequence].wav


Neural network (neural_network.py):

	See statistics: python neural_network.py -s
	See history data: python neural_network.py -hi
	Data for specific speaker: python neural_network.py -sp [speaker_name]
	Re-train network: python neural_network.py -t
	Re-calculate MFCCs: python neural_network.py -m
	Change trainin epochs numbers: python neural_network.py -e [epoch number]


Dataset/Sentence Recording (dataset.py):

	Record dataset: python dataset.py -d
	Recrod sentence: python dataset.py -s
	Move recorded dataset to main folder: python dataset -m


AM: Π16057, Π16066