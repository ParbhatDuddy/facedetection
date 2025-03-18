# Importing cv library
import cv2
# Capturing face by cv library
face_capture = cv2.CascadeClassifier("frontface.xml")
# capturing video through cv
video_capture = cv2.VideoCapture(0)
# Starts an infinite  loop for video processing
while True:
    # read video frame by frame
    ret,video_data = video_capture.read()
    # convert the frame to grayscale
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    # captures faces
    faces = face_capture.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # draw rectangle on detected faces
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Live_Camera",video_data)
# opened camera while we press "space" key 
    if cv2.waitKey(10) == ord(" "):
        break
    # Release the camera resource after exitin loop
video_capture.release()


