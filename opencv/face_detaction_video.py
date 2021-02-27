import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

def draw_boundary(img,classifier,scale_factor,min_neighbors,color,text):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray,scale_factor,min_neighbors)
    coords = []
    for (x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
    return img

def detect(img,classifier):
    img = draw_boundary(img,classifier,1.1,10,(255,0,0),"Face")
    return img

cap = cv2.VideoCapture(1)

while True:
    rat,frame = cap.read()
    frame = detect(frame,face_cascade)
    cv2.imshow("Video Face", frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()