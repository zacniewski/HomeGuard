import cv2
import threading
import time


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        if not self.grabbed:
            print("Can't receive frame (stream end?). Exiting ...")
            exit()
        else:
            print(f"Frame shape in init : {self.frame.shape}")
        threading.Thread(target=self.update, args=()).start()
        #self.update()

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        image = self.frame
        print(f"Frame (from gen) shape: {self.frame.shape}")
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            if not self.grabbed:
                print("Can't receive frame (stream end?). Exiting ...")
                exit()
            else:
                print(f"Frame shape in update: {self.frame.shape}")


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


#cam = VideoCamera()
#print(cam)
#for i in range(10):
#    gen(cam)
