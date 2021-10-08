from pdf2image import convert_from_path
import os

#Function returns name of .pdf files and path to the file.
#file = path to folder containing all .pdf files
def get_paths(folder):
    name = [] 
    paths = []
    count = 0
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            name.append(f[:-4])
            paths.append(folder+'/'+f)
            count = count+1
    return name, paths, count



#Function to convert pdf to image
#pdf_path = path to .pdf file
#name = name of the .pdf file
#save = path to directory where image is to be stored
def convert(paths, name, save, count):
    for i in range(count):
        pdf_path = paths[i]
        file_name = name[i]
        images = convert_from_path(pdf_path)
        for j in range(len(images)):
            images[i].save(save + '/' + file_name + '_' + str(j) +'.jpg', 'JPEG')