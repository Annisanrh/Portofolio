import cv2
import numpy as np


# Fungsi nothing digunakan sebagai callback funtion dari trackbar
def nothing(x):
    pass

#membuat trackbar hsv dengan nama window range modifier
cv2.namedWindow("Range Modifier")

cv2.createTrackbar("Lower - H", "Range Modifier", 0, 179, nothing)
cv2.createTrackbar("Lower - S", "Range Modifier", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "Range Modifier", 0, 255, nothing)
cv2.createTrackbar("High - H", "Range Modifier", 179, 179, nothing)
cv2.createTrackbar("High - S", "Range Modifier", 255, 255, nothing)
cv2.createTrackbar("High - V", "Range Modifier", 255, 255, nothing)


#mendefinisikan nilai awal dari variabel yang akan digunakan 
# dalam proses modifikasi rentang nilai warna
lh = 33
ls = 0
lv = 70
hh = 73
hs = 255
hv = 255

# input gambar dan convert gambar RBG menjadi gambar HSV
# Menampilkan perubahan real time gambar dengan trackbar 
image =cv2.imread('bunga.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# Membuat looping 
while True:

    lh = cv2.getTrackbarPos("Lower - H", "Range Modifier")
    ls = cv2.getTrackbarPos("Lower - S", "Range Modifier")
    lv = cv2.getTrackbarPos("Lower - V", "Range Modifier")
    hh = cv2.getTrackbarPos("High - H", "Range Modifier")
    hs = cv2.getTrackbarPos("High - S", "Range Modifier")
    hv = cv2.getTrackbarPos("High - V", "Range Modifier")


    lower_green = np.array([lh, ls, lv])
    higher_green = np.array([hh, hs, hv])

    # membuat mask dan menggabungkan gambar original dengan mask untuk mendapatkan gambar hasil 
    mask = cv2.inRange(hsv_image, lower_green, higher_green)
    imgResult = cv2.bitwise_and(image, image, mask=mask)

    # Menampilkan gambar original, gambar hsv, mask, dan gambar hasil
    cv2.imshow('mask', cv2.resize(mask, (389, 224)))
    cv2.imshow('original', cv2.resize(image, (389, 224)))
    cv2.imshow('image hsv', cv2.resize(hsv_image, (389, 224)))
    cv2.imshow('image hasil', cv2.resize(imgResult, (389, 224)))

    
    #cv2.imshow('heatmap', heatmap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
