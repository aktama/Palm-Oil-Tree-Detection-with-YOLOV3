from PIL import Image, ImageEnhance, ImageStat
import statistics
import os
import sys

def brightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

im = os.path.join(sys.path[0], "input.jpg")
im_brightness = brightness(im)

target_brightness = 105.36314380508921

im = Image.open(os.path.join(sys.path[0], "input.jpg")).convert('L')

difference = target_brightness-im_brightness

enhancer = ImageEnhance.Brightness(im)

factor = (float(target_brightness+difference))/(float(target_brightness))
im_output = enhancer.enhance(factor)
im_output.save(os.path.join(sys.path[0], "input_ready.jpg"))