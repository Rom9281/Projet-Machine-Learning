# import required modules 
import os
from pydub import AudioSegment 

TEST_DATA_PATH = '/home/rom1/convertion/test'

foldersInTest = list(os.listdir(TEST_DATA_PATH))
print(foldersInTest)

for folderName in foldersInTest:
    PATH_TO_FOLDER = os.path.join(TEST_DATA_PATH, folderName)

    filesInFolder = os.listdir(PATH_TO_FOLDER)
    
    for fileNameMP3 in filesInFolder:
        splitName = fileNameMP3.split('.')
        fileNameWAV = splitName[0] + '.wav'

        if(splitName[1] == 'mp3'):
            print("[$] Converting " + fileNameMP3 + " to wav]")
            PATH_TO_FILE = os.path.join(PATH_TO_FOLDER, fileNameMP3)
            PATH_TO_OUTPUT_FILE = os.path.join(PATH_TO_FOLDER, fileNameWAV)

            print(PATH_TO_FILE)
            print(os.path.exists(PATH_TO_FILE))
            
            sound = AudioSegment.from_mp3(PATH_TO_FILE) 
            sound.export(PATH_TO_OUTPUT_FILE, format="wav")

            # Delete the PATH_TO_FILE
            os.remove(PATH_TO_FILE)