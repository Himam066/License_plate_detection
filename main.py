# load models
from ultralytics import YOLO
import cv2
from sort.sort import *
from util import get_car, read_license_plate, write_csv

output_folder = "./result/"g

coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO("./yolov8.pt")
mot_tracker = Sort()
# results = {}
# queue = set()
vehicles = [2,3,5,7]

#load Video
cap = cv2.VideoCapture("./test3.mp4")
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video_path = "C:/Users/ASUS/Desktop/Learning/output2.mp4"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))



#read frames
# frame_num = 1
ret = True
while ret:
    # frame_num += 1
    ret, frame = cap.read()
    if ret:
        # results[frame_num] = {}
        #detect vehicles
        detections = coco_model(frame)[0]
        detections_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, score])

        #tracking vehicles
        track_ids = mot_tracker.update(np.asarray(detections_))


        #detect license plate
        license_plates = license_plate_detector(frame)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate
            cv2.rectangle(frame,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),-1)

            #asigning license plate
            xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)
            cv2.rectangle(frame,(int(xcar1),int(ycar1)), (int(xcar2),int(ycar2)),(0,255,0),1)

        out.write(frame)
            
            # queue.add(car_id)
            # if car_id not in queue:
                # Visualized
                
                #crop license plate
                # license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]
                # filename = f"LP{i}.png"
                # output_path = os.path.join(output_folder, filename)
                # cv2.imwrite(output_path, license_plate_crop)
            
            
            #     #process license plate
                # license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
                # _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 70, 255, cv2.THRESH_BINARY_INV)
                # filename = f"thresh{i}.png"
                # path = os.path.join(output_folder, filename)
                # cv2.imwrite(path, license_plate_crop_thresh)
                # i += 1
                
                 #read license plate
                

            #     # if license_plate_text is not None:
                # results[frame_num][car_id] = {"car":{"bbox":[xcar1, ycar1, xcar2, ycar2]},
                #                                   "license_plate": {"bbox": [ x1, y1, x2, y2],
                #                                                     "text": license_plate_text,
                #                                                     "bbox_score": score,
                #                                                     "text_score":license_plate_text_score}}
                # queue.add(car_id)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


#write results
# write_csv(results, "./test.csv")








