import os

documents = ['txt', 'doc', 'pdf']
pictures = ['png', 'jpg', 'jpeg']
music = ['mp3', 'mp4', 'wav']
videos =  ['webm']

#os.chdir('/home/annie/Downloads')
files = os.listdir('/home/annie/Downloads')

for file in files:
    splited_file = file.split('.')
    
    if splited_file[-1] in pictures:
        os.system("mv {} /home/annie/Pictures".format(file))
    
    elif splited_file[-1] in documents:
        os.system("mv {} /home/annie/Documents".format(file))
    
    elif splited_file[-1] in music:
        os.system("mv {} /home/annie/Music".format(file))
    
    elif splited_file[-1] in videos:
        os.system("mv {} /home/annie/Videos".format(file))
    
    else:
        pass 


