import os
from PIL import Image, ImageDraw, ImageFont
import piexif
from config import *
rootdir = '/home/specs/public_html/ymmts_imglist'
def visiblewatermark(subdir , Key , file) :
      prefixes = ['watermark','invisible']
      try:
        if ((file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))) and (not file.startswith(tuple(prefixes)))):
            #Create an Image Object from an Image
            img_obj = Image.open(os.path.join(subdir, file))
            width, height = img_obj.size

            draw = ImageDraw.Draw(img_obj)
            #text  = "vinaudit.com"
            text = chooseText(Key)
            print(text)

            font = ImageFont.truetype('/usr/share/fonts/msttcore/arial.ttf', 24)
            textwidth, textheight = draw.textsize(text)

            # calculate the x,y coordinates of the text
            # x = width - textwidth - 80
            # y = height - textheight - 30
            x = width - textwidth
            y = height - textheight

            # draw watermark in the bottom right corner
            draw.text((x/2, y/2), text, fill=(211,211,211), font=font)
            img_obj.show()

            print((os.path.join(subdir, 'watermark_'+ Key +'_'+ file)))

            #Save watermarked image
            img_name = os.path.join(subdir, 'watermark_' + Key + '_' + file)
            img_obj.save(img_name)

            # Add the metadata to image
            modify_img = Image.open(img_name)
            exifData = modify_img._getexif()
            zeroth_ifd = {piexif.ImageIFD.Copyright: text}
            exif_dict = {"0th": zeroth_ifd, "Exif": {}, "1st": {}, "thumbnail": None, "GPS": {}}
            exif_dat = piexif.dump(exif_dict)
            save_modified_img = Image.open(img_name)
            save_modified_img.save(img_name, exif=exif_dat)
            #exit()
      except Exception as ex:
           print(ex)
