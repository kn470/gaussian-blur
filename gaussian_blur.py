import cv2
import numpy as np

img = cv2.imread("colorpic.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (400,400))

def get_surrounding(img, i, j):
    surround_list = [img[i-1,j-1], img[i,j-1], img[i+1,j-1], img[i-1,j], img[i+1,j], img[i-1,j+1], img[i,j+1], img[i+1,j+1]]
    return surround_list

def gaussian():
    global img
    size_x, size_y = img.shape[0], img.shape[1]
    new_list = []
    for i in range(1,size_x-1):
        for j in range(1,size_y-1):
            new_val = sum(get_surrounding(img, i, j))/len(get_surrounding(img, i, j))
            new_list.append(new_val)

    new_list = np.array(new_list)
    new_list = np.reshape(new_list, (398,398))
    img[1:399, 1:399] = new_list

for i in range(1):
    gaussian()

cv2.imshow("blur", img)
cv2.imshow("image", cv2.imread("colorpic.jpg"))
cv2.waitKey(0)
cv2.destroyAllWindows()
