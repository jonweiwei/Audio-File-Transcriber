# Audio-File-Transcriber
A Python program that reads audio data from a given .wav file and creates a new text file with the transcribed audio

This program uses the PyPI SpeechRecognition library, which can be found here:
https://pypi.org/project/SpeechRecognition/

For the program to work, the SpeechRecognition library must be installed on your system, which can be done easily with 
*pip install SpeechRecognition*

In order for the program to transcribe the desired file, you must go into AudioFileTranscriber.py and set the value of the file_name variable on line 5 to 'filename.wav', where "filename" is replaced by the name of the .wav file you would like to transcribe.
