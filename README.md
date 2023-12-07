# Projet-Machine-Learning
Analysing the https://www.kaggle.com/datasets/rayonegautam/charanet dataset

## Extracting Files

### MP3 to WAV

The files in Utilities are used to change the mp3 files in the dataset to be compatible with wav

### extractAudio and extractAudioFiltered

Extract audio extracts all the files in the dataset and extracts the waveform and spectrogram to be processed by the models.

The Filter one extracts only the files from folders with enough training data: it's fixed by `MIN_NUM_FILES`.

## Models

### Standard model

Standard model from the exemple, takes in extractAudio as data source

### Model 2 & 3

Playing with additional layers, using the filered data
