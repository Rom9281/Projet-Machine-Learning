# Projet-Machine-Learning
Analysing the https://www.kaggle.com/datasets/rayonegautam/charanet dataset

by Romain Gaud, Romain Galmier, Maxime Curral

## Extracting Files

### MP3 to WAV

The files in Utilities are used to change the mp3 files in the dataset to be compatible with wav.

For this, we used the programs in Utilities:
 - Utilities\ConversionToWAV\ConvertToWav.py
 - Utilities\ConversionToWAV\DeleteIdentifier.py

#### ConvertToWav
Used to convert audio files from MP3 format to WAV format. It uses the `pydub` library to perform the audio format conversion.

For each file in the folder, the script checks if the file is an MP3 file by splitting the file name on the '.' character and checking the file extension. If the file is an MP3 file, it constructs the name of the new WAV file by replacing the '.mp3' extension with '.wav'.

Finally, the script deletes the original MP3 file using `os.remove`. This is done after the WAV file has been successfully created to ensure that no data is lost if the conversion process fails.


#### DeleteIdentifier

The provided Python script is designed to delete files with a specific identifier in their names from a given directory and its subdirectories. The identifier is ".Identifier" and the directory path is provided as an argument to the function `delete_files_with_identifier`.

The function then iterates over each file in the `filenames` list. If a file ends with the ".Identifier" extension, the `os.path.join` function is used to concatenate the directory path and the file name to create the full path to the file. The `os.remove` function is then called with this full path to delete the file.


## Using the Tenserflow library

### Extracting features

####  extractAudio.ipynb

Extract audio extracts all the files in the dataset and extracts the waveform and spectrogram to be processed by the models.

#### extractAudioFiltered.ipynb

The Filter one extracts only the files from folders with enough training data: it's fixed by `MIN_NUM_FILES`.

This makes the model produce better results.

### Testing diverse models

#### Standard model: standard_model.ipynb

Standard model from the exemple, takes in extractAudio as data source

#### Model 2 & 3

Playing with additional layers, using the filered data. The second model seems to be best (number 2).

## Playing with another library to get better results: Librosa

The file librosaFeatures.ipynb contains better result, as it is a different method to extract features. we then train a similar model using Tenserflow.