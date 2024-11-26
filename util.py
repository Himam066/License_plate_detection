

#mapping dictionaries for charater conversion

def write_csv(results, output_path): 
    """
    Write the results to a CSV file.

    Args:
        results (dict): Dictionary containing the results.
        output_path (str): Path to the output CSV file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:  # Use utf-8 encoding
        f.write('{},{},{},{},{},{},{}\n'.format('frame_nmr', 'car_id', 'car_bbox',
                                                'license_plate_bbox', 'license_plate_bbox_score', 'license_number',
                                                'license_number_score'))

        for frame_nmr in results.keys():
            for car_id in results[frame_nmr].keys():
                print(results[frame_nmr][car_id])
                if 'car' in results[frame_nmr][car_id].keys() and \
                   'license_plate' in results[frame_nmr][car_id].keys() and \
                   'text' in results[frame_nmr][car_id]['license_plate'].keys():
                    f.write('{},{},{},{},{},{},{}\n'.format(frame_nmr,
                                                            car_id,
                                                            '[{} {} {} {}]'.format(
                                                                results[frame_nmr][car_id]['car']['bbox'][0],
                                                                results[frame_nmr][car_id]['car']['bbox'][1],
                                                                results[frame_nmr][car_id]['car']['bbox'][2],
                                                                results[frame_nmr][car_id]['car']['bbox'][3]),
                                                            '[{} {} {} {}]'.format(
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][0],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][1],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][2],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][3]),
                                                            results[frame_nmr][car_id]['license_plate']['bbox_score'],
                                                            results[frame_nmr][car_id]['license_plate']['text'],
                                                            results[frame_nmr][car_id]['license_plate']['text_score'])
                            )





#License Plate reading
bengali_letter = { 10 : "অ", 11 : "ই", 12 : "উ", 13 : "এ", 14: "ক", 15 : "খ", 16 : "গ", 17 : "ঘ", 18 : "ঙ", 19 : "চ", 20 : "ছ",
                   21 : "জ", 22 : "ঝ", 23 : "ট", 24 : "ঠ", 25 : "ড", 26 : "ঢ", 27 : "থ", 28 : "দ", 29 : "ন", 30 : "প", 
                   31 : "ফ", 32 : "ব", 33 : "ভ", 34 : "ম", 35 : "য", 36 : "র", 37 : "ল", 38 : "শ", 39 : "স", 40 : "হ"}

bengal_district = { 41 : "", 42 : "", 43 : "", 44 : "", 45 : "", 46 : "", 47 : "", 48 : "", 49 : "", 50 : ""

}

def read_license_plate(license_plate_crop):
    return None, None
    

def get_car(license_plate, vehicle_track_ids):
  
    x1, y1, x2, y2, score, class_id = license_plate

    foundIt = False
    for j in range(len(vehicle_track_ids)):
        xcar1, ycar1, xcar2, ycar2, car_id = vehicle_track_ids[j]

        if x1 > xcar1 and y1 > ycar1 and x2 < xcar2 and y2 < ycar2:
            car_indx = j
            foundIt = True
            break

    if foundIt:
        return vehicle_track_ids[car_indx]

    return -1, -1, -1, -1, -1