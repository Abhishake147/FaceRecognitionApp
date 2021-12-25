import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow('Webcam Screenshot')

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print('Unable to grab frame')
        break

    cv2.imshow('Webcam Screenshot', frame)


    k = cv2.waitKey(1)

    if k%256 == 27:
        print('Escape button pressed. closing windows')
        break

    elif k%256 == 32:
        #img_name = Image
        img_name = 'frame_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        print('Screen shot taken')
        img_counter += 1

cam.release()

cam.destroyAllWindows()