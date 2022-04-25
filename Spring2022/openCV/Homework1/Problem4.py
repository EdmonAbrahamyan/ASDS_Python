import cv2 as cv

#Rescale the video vid1.jpg by 0.5 and display the original video and the rescaled one in separate windows.

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  # will talk more about this later


capture = cv.VideoCapture('Videos/vid1.mp4')

while True:
    frame_loaded, frame = capture.read()  # returns the frams and a boolean indicarting if it was successfully read

    if frame is not None:
        frame_rescaled = rescaleFrame(frame, 0.5)
        cv.imshow('Video Original', frame)
        cv.imshow('Video Rescaled', frame_rescaled)
    else:
        print('empty frame')
        exit(1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)