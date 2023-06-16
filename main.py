import cv2

input_video = cv2.VideoCapture('../assets/arsene.mp4')

if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
 
width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))

while True:
    ret, frame = input_video.read()

    if not ret:
        break
    
    cv2.rectangle(
            img=frame,
            pt1=(100, 100),
            pt2=(300, 300),
            color=(0,0,255),
            thickness=5
        )

    cv2.imshow('Video Playback', frame)
    
    output_video.write(frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
output_video.release()
input_video.release()
cv2.destroyAllWindows()
