import cv2

image=cv2.imread("Screenshot_2.png",cv2.IMREAD_UNCHANGED)
#cv2.imshow('image',image)

print(image.shape)

width=int(image.shape[1]*50/100)
heigth=int(image.shape[0]*50/100)


dsize=(width,heigth)

output=cv2.resize(image,dsize)


cv2.imwrite('Screenshot_new.jpeg',output)


cv2.waitKey(0)