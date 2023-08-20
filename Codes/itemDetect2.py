import cv2

net = cv2.dnn.readNet("./Codes/dnn_model/yolov4-tiny.weights", "./Codes/dnn_model/yolov4-tiny.cfg")
#net = cv2.dnn.readNet("./Codes/dnn_model/yolov3.weights", "./Codes/dnn_model/yolov3.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

classes = []
with open("./Codes/dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

cam="rtsp://192.168.0.92:554/user=admin&password=halil1978&channel=8&stream=0"
cap = cv2.VideoCapture(2)

def itemDetection():
    ret, frame = cap.read()
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.5, nmsThreshold=0.3)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]
        #print(class_name)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255,128,0), 2)
        cv2.putText(frame, f'{class_name.upper()} {int(score*100)}%', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 128, 0), 2)

    cv2.imshow("Frame", frame)