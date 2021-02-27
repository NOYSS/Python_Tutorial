import cv2

# อ่านรูปภาพเข้ามา กำหนดค่า 1 คือค่าสีจะเหมือนค่าเดิมของภาพ, 0 คือ grayscale, -1 คือ ความโปรงแสง
img = cv2.imread("./images/pienza-town-italy-1080x720.jpg", 1)

# Crop image
y = 350
x = 500
w = 200
h = 200
# img = img[y:y+h, x:x+w]

# แสดงภาพบนจอ จะสร้าง GUI ขึ้นมา
cv2.imshow('image', img)
# รอรับค่าเมื่อกดปิดจอ
cv2.waitKey(0)
# ปิดหน้าต่าง GUI ทั้งหมด
cv2.destroyAllWindows();