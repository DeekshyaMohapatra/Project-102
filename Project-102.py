import cv2
import dropbox
import time
import random

startTime = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    videoObject = cv2.VideoCapture(0)
    result = True

    while (result) :
        ret, frame = videoObject.read()
        imgName = str(number) +'img.jpg'
        cv2.imwrite(imgName, frame)
        startTime=time.time

        result = False

    return imgName
    
    videoObject.release()
    cv2.destroyAllWindows()

def upload_file(imgName):
    accesstoken = 'sl.BByLvv9jAX0c11LNoLo5kj0s9MoT_-AnyraWLbDwqQxHq36Lo_E46sYtVdLr1qwIFGbT9pBmE8JoEXfRsq472q2S8j9W0pASUrk_TT7LSYtYwDw8a0OGEeMOfe_iKzDQfpr2F0Y'
    file_from = imgName
    file_to = '/Class102/'+ imgName
    dbx = dropbox.Dropbox(accesstoken)

    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

    print("File uploaded")

def main():
    while (True) :
        if((time.time()-startTime)>=1):
            name = takeSnapshot()
            upload_file(name)

main()