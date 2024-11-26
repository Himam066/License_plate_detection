# img = cv2.imread("C:/Users/ASUS/Desktop/Learning/vehicle889.jpg")
# new_width = 640
# new_height = 640
# resized_image = cv2.resize(img, (new_width, new_height))

# detections = coco_model(resized_image)[0]
# detections_ = []
# for detection in detections.boxes.data.tolist():
#     x1, y1, x2, y2, score, class_id = detection
#     if int(class_id) in vehicles:
#         detections_.append([x1, y1, x2, y2, score])

# track_ids = mot_tracker.update(np.asarray(detections_))

# license_plates = license_plate_detector(resized_image)[0]
# for license_plate in license_plates.boxes.data.tolist():
#     x1, y1, x2, y2, score, class_id = license_plate

# xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

# if car_id not in queue:
#     #crop license plate
#     license_plate_crop = resized_image[int(y1):int(y2), int(x1): int(x2), :]
#     filename = f"LP{i}.png"
#     output_path = os.path.join(output_folder, filename)
#     cv2.imwrite(output_path, license_plate_crop)
            
            
#     #process license plate
#     license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
#     # _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 180, 255, cv2.THRESH_BINARY_INV)
#     # filename = f"thresh{i}.png"
#     # path = os.path.join(output_folder, filename)
#     # cv2.imwrite(path, license_plate_crop_thresh)
#     i += 1
                
#     #read license plate
#     license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_gray)
#     print((license_plate_text, license_plate_text_score))


#     # if license_plate_text is not None:
#     results[0][car_id] = {"car":{"bbox":[xcar1, ycar1, xcar2, ycar2]},
#                                                   "license_plate": {"bbox": [ x1, y1, x2, y2],
#                                                                     "text": license_plate_text,
#                                                                     "bbox_score": score,
#                                                                     "text_score":license_plate_text_score}}
#     queue.add(car_id)

from ultralytics import YOLO
import cv2

# Load YOLO model and input image
model = YOLO("./exp1.pt")
img = cv2.imread("./1.jpg")
results = model(img)[0]

# Extract bounding boxes and class IDs
detections = []
for result in results.boxes.data.tolist():
    xmin, ymin, xmax, ymax, confidence, class_id = result
    
    # Draw bounding box
    cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 1)
    
    # Label the bounding box
    cv2.putText(img, str(int(class_id)), (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 1)

# Display the sorted bounding boxes and labels
cv2.imshow("Sorted Detection Results", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
