import cv2

# เปิดการใช้ webcam
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

video_capture.release()
cv2.destroyAllWindows()