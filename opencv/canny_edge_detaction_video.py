import cv2

print(cv2.__version__)

# เปิดการใช้ webcam ตรง parameter หากมีกล้องมากกว่า 1 ตัว ระบุ index ในที่ใส่ 1 เป็นกล้อง webcam usb
video_capture = cv2.VideoCapture(1)

while True:

    # ดึงเฟรมภาพมาจากวีดีโอ
    ret, frame = video_capture.read()

    # หาเส้นขอบ
    frame = cv2.Canny(frame, 100, 200)

    # แสดงรูปภาพผลลัพธ์
    cv2.imshow('Video', frame)

    # กด 'q' เพื่อปิด!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# คืนทรัพยากร
video_capture.release()
# ปิดหน้าต่างทั้งหมด
cv2.destroyAllWindows()