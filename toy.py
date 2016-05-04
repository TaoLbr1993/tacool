'''
Create on 4/29/2016

@author = Tao
'''

from PIL import Image,JpegImagePlugin
import sys

def img_to_asciiart(image, height_num, width_num=0,charset="MMMWNXK0Okxdolc:;,'...   ", out=sys.stdout):
    '''
    convert an image to asciiart
    :param image: The image to be converted. Type `PIL.JpegImagePlugin.JpegImageFile` required
    :param height_num: Amount of chars per column
    :param width_num: Amount of chars per row. **Make it 0 if require proportion
    :param charset: The charset to be used in asciiart. **It is recommended to sort the chars in order of ascendant 'grayscale'
    :param out: Where to output. Defaultly it is `sys.stdout`.
    :return: None
    '''

    if not isinstance(height_num, int):
        raise TypeError('Parameter `height_num` requires type of `int`')
    if not isinstance(width_num,int):
        raise TypeError('Parameter `width_num` requries type of `int`')

    # convert to greyscale
    image = image.convert('L')

    # calculate the number of char on height and width
    height,width = image.size
    hstep = int(height / height_num)
    wstep = 0
    if width_num==0:
        width_num = int(width/hstep)
        wstep = hstep
    else:
        wstep = int(width/width_num)

    gray_step = 256/len(charset)

    # store the result
    draw = [[' ' for i in range(height_num)] for i in range(width_num)]

    for h in range(height_num):
        for w in range(width_num):
            gray = 0
            for i in range(hstep):
                for j in range(wstep):
                    gray += image.getpixel((h*hstep+i,w*wstep+j))

            gray = int(gray/(hstep*wstep*gray_step))
            draw[w][h] = charset[gray]

    for l in draw:
        out.write(''.join(l))
        out.write('\n')


if __name__ == '__main__':
    image = Image.open('test.png')
    print(image)
    fout = open('res.txt','w')
    img_to_asciiart(image, 50, 45,out=fout)
    fout.close()

