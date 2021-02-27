import numpy as np
import cv2

# อ่านรูปภาพเข้ามา กำหนดค่า 1 คือค่าสีจะเหมือนค่าเดิมของภาพ, 0 คือ grayscale, -1 คือ ความโปรงแสง
img = cv2.imread("./images/pienza-town-italy-1080x720.jpg", 1)

# Drawing Line เส้นตรง
img = cv2.line(img,(0,0),(255,255),(255,0,0), 10)

# Drawing Arrow Line ลูกศร
img = cv2.arrowedLine(img,(0,200),(255,200),(255,255,100), 10)

# Drawing Rectangle สี่เหลี่ยม
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Drawing Circle วงกลม
img =  cv2.circle(img,(447,103), 63, (0,0,255), 0)

# Drawing Ellipse วงรี
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Drawing Polygon รูปหลายเหลี่ยม
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img =  cv2.polylines(img,[pts],True,(0,255,255))

# Adding Text to Images
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV By Noy',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

# แสดงภาพบนจอ จะสร้าง GUI ขึ้นมา
cv2.imshow('Drawing image', img)
# รอรับค่าเมื่อกดปิดจอ
cv2.waitKey(0)
# ปิดหน้าต่าง GUI ทั้งหมด
cv2.destroyAllWindows();