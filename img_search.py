'''
    Search for a pattern from an image

    <<based on https://github.com/drov0/python-imagesearch/blob/master/python_imagesearch/imagesearch.py>>

    input:
    target_img: target image that you want to search from
    pattern: desired pattern you wish to find in the target_img
    precision : the higher, the lesser tolerant and fewer false positives are found. Default is 0.8

    Return:
    the coordinate of the center of the matched pattern
'''

import cv2, os

def image_search(target_img, pattern, precision=0.8):
    # preprocess image
    target = cv2.imread(target_img, 0)
    template = cv2.imread(pattern, 0)
    
    if target_img is None:
        raise FileNotFoundError('Image name {} cannot be found'.format(target_img))
    if template is None:
        raise FileNotFoundError('Image name {} cannot be found'.format(template))

    height, width = template.shape

    x_offset = width/2
    y_offset = height/2

    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val < precision:
        return [-1, -1]
    
    x, y = (max_loc[0]+x_offset, max_loc[1]+y_offset)

    return x, y

def tap_xy(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))

