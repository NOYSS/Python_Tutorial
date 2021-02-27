import cv2

# เปิดการใช้ webcam
video_capture = cv2.VideoCapture(1)

while True:

    # ดึงเฟรมภาพมาจากวีดีโอ
    ret, frame = video_capture.read()

    # ปรับสีภาพ
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # แสดงรูปภาพผลลัพธ์
    cv2.imshow('Video', gray)

    # กด 'q' เพื่อปิด!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()