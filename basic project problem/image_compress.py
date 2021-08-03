from PIL import Image
import os 

# single file copress
def single_file_copress(filename,qual=30):
    img=Image.open(filename)
    img.save('__Scompress_'+filename,optimize=True,quality=qual)
# single_file_copress('4kImage.jpg',43)


# multiple file compress
# list directory all jpg & pdg file  in list
def multiple_file_compress(q):
    list_files=os.listdir()
    only_image_file=[i for i in list_files if i.endswith(('.jpg','.png'))]


    for file in only_image_file:
        im =Image.open(file)
        im.save('__Mcompress_'+file,optimize=True,quality=q)
# multiple_file_compress(30)