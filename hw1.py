import cv2 as cv
import numpy as np

def mouse_callback(event, x, y, flags, param):
    if event == 1:
        print('B: ', param[y][x][0], '\nG: ', param[y][x][1], '\nR: ', param[y][x][2])
        print('=================================')


Path = 'Data/'
Name = 'rabong2.jpg'
FullName = Path + Name

# 이미지 읽기
img = cv.imread(FullName)

#
#
# 여기에 소스코드 작성
red = np.zeros(img.shape, np.uint8)
four_xy= [0,0,0,0]



for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if img[y][x][0] > 100 or img[y][x][1] > 100 or img[y][x][2] > 100:
            red[y][x] = [0,0,255]
            if x> img.shape[0]/2 and y<img.shape[0]/2:
                four_xy[0] +=1
            if x< img.shape[0]/2 and y<img.shape[0]/2:
                four_xy[1] += 1
            if x< img.shape[0]/2 and y>img.shape[0]/2:
                four_xy[2]+=1
            if x> img.shape[0] / 2 and y > img.shape[0] / 2:
                four_xy[3]+=1
        else:
            red[y][x] = img[y][x]
if four_xy.index(max(four_xy)) ==0:
    print('제1사분면')
elif four_xy.index(max(four_xy)) ==1:
    print('제2사분면')
elif four_xy.index(max(four_xy)) ==2:
    print('제3사분면')
elif four_xy.index(max(four_xy)) ==3:
    print('제4사분면')

#
#
# 이미지 출력
cv.imshow('red', red)
#cv.imshow('gray1', gray1)
#cv.imshow('gray', gray)
#cv.imshow('blur', blur)


while cv.waitKey(33) <= 0:
    cv.setMouseCallback('red', mouse_callback, red)

cv.waitKey(0)
