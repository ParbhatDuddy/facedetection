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
    # draw rectangle L-shaped on detected faces
     
    for (x, y, w, h) in faces:
        thickness = 2
        color = (0, 255, 0)  
        corner_length = int(w * 0.2)  # 20% of width

        # Top-left corner
        cv2.line(video_data, (x, y), (x + corner_length, y), color, thickness)
        cv2.line(video_data, (x, y), (x, y + corner_length), color, thickness)

        # Top-right corner
        cv2.line(video_data, (x + w, y), (x + w - corner_length, y), color, thickness)
        cv2.line(video_data, (x + w, y), (x + w, y + corner_length), color, thickness)

        # Bottom-left corner
        cv2.line(video_data, (x, y + h), (x, y + h - corner_length), color, thickness)
        cv2.line(video_data, (x, y + h), (x + corner_length, y + h), color, thickness)

        # Bottom-right corner
        cv2.line(video_data, (x + w, y + h), (x + w - corner_length, y + h), color, thickness)
        cv2.line(video_data, (x + w, y + h), (x + w, y + h - corner_length), color, thickness)

    cv2.imshow("Live_Camera",video_data)
# opened camera while we press "space" key 
    if cv2.waitKey(10) == ord(" "):
        break
    # Release the camera resource after exitin loop
video_capture.release()


