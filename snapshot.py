import cv2
import dropbox
import time,random
from dropbox.files import WriteMode
start_time = time.time()


def take_snapshot():
    number = random.randint(0,100)
    
    #Initializing cv2 and making our webcam as the videoCapturObject
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result): 
        # Read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        # cv2.imwrite() method is used to save an image to any storage device
        img_name = "img" + str(number) + ".jpg"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken!!!")
    # releases the camera
    videoCaptureObject.release()
    
    # closes all the window that might be opened while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
     access_token = 'mvYxKMTROkgAAAAAAAAAAWAM0t0QSvIbZQ9vcNEv9V-N6A5ex8sLS3ycdneOAhju'
     file = img_counter
     file_from = file
     file_to = "/newFolder1/" + (img_name)
     dbx = dropbox.Dropbox(access_token)
     # API v2
     with open(file_from, 'rb') as f:
         dbx = upload_file(f.read(),file_to, mode = dropbox.files.WriteMode.overwrite)
     print("files uploaded!!!")
    
def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)