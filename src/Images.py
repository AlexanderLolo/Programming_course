import os
from PIL import  Image, ImageDraw, ImageFont

def imageconverter(ext1, ext2):
    
    for image in os.listdir("./"):
        if os.path.isdir(image):
            continue

        elif image.endswith(ext1):
            with Image.open(image) as im:
                draw = ImageDraw.Draw(im)
                sz = im.size
                halfside = min(sz[0],sz[1])/8
                cr = [sz[0]/2, sz[1]/2]

                draw.rectangle([cr[0]-halfside , cr[1]-halfside, cr[0]+halfside, cr[1]+halfside], outline = (13,0,255), width = 4)
                font = ImageFont.truetype("arial.ttf", 22) 
                draw.multiline_text([cr[0]-halfside*7/8 , cr[1]-halfside*7/8], "Hello,\nWorld!", font = font)

                im.save(os.path.splitext(image)[0] + ext2)
                del draw


def main():
    imageconverter(".png", ".bmp")

if __name__ == "__main__":
    main()