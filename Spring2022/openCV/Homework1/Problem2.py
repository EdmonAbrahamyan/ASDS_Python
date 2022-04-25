import cv2 as cv

# Open the video vid1.mp4 and display it frame by frame in a window named vid1.

capture = cv.VideoCapture('Videos/vid1.mp4')

while True:
    frame_loaded, frame = capture.read()

    if frame_loaded:
        cv.imshow('Vid1', frame)
    else:
        print('empty frame')
        exit(1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)