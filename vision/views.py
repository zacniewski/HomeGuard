from django.http import StreamingHttpResponse
import cv2
import imutils
import numpy as np
import time

from imutils.video import VideoStream


# vs = VideoStream(src=0).start()


def test_usb_camera(request):
    cap = cv2.VideoCapture(0)
    time.sleep(2.0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        time.sleep(2.0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # if frame is read correctly 'success'' is True
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")

        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        image = imutils.resize(image, width=400)
        ret, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"


def camera_usb(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
