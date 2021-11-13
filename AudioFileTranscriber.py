import speech_recognition as sr
from os import path

# get the file name and the path of the audio file to be transcribed
file_name = 'audiotest.wav'
audio_file_path = path.join(path.dirname(path.realpath(__file__)), file_name)

# create the speech recognizer
speech_recognizer = sr.Recognizer()

# set the audio file to be transcribed as the source
with sr.AudioFile(audio_file_path) as source:

    # record and get the data from the audio file
    file_data = speech_recognizer.record(source)

    # convert the file data to text via Google API
    transcribed_audio = speech_recognizer.recognize_google(file_data)

# create a text file named "filename.wav.txt"
text_file = open(path.join(path.dirname(path.realpath(__file__)), '{}.txt'.format(file_name)), 'w')

# writing transcribed audio to newly created text file
# the transcribed audio is also printed to the terminal
try:
    text_file.write(transcribed_audio)
    print('Transcribed audio: {}'.format(transcribed_audio))

# if the audio file was not readable, write an error message to the text file and print it to the terminal
except sr.UnknownValueError:
    text_file.write('Error: the audio could not be read')
    print('Error: the audio could not be read')

# close the file instance
text_file.close()
