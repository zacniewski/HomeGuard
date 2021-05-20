from django.views.decorators import gzip
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import StreamingHttpResponse, HttpResponseServerError

import cv2
import threading
from time import sleep


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(-1)
        self.video.set(3, 640)
        self.video.set(4, 480)
        sleep(2.0)
        (self.grabbed, self.frame) = self.video.read()
        if not self.grabbed:
            print("Can't open camera")
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
@xframe_options_exempt
def camera_usb_streaming(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("Something went wrong!")
