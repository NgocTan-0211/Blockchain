from ultralytics import YOLO
import cv2
import time

from hash_utils import create_hash

from backend.blockchain import save_hash
from backend.database import insert_event

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

last_capture = 0

while True:

    ret, frame = cap.read()

    results = model(frame)

    person_found = False

    for result in results:

        for box in result.boxes:

            if int(box.cls) == 0:

                person_found = True

    current_time = time.time()

    if person_found and \
       current_time-last_capture > 10:

        filename = \
        f"uploads/{int(current_time)}.jpg"

        cv2.imwrite(
            filename,
            frame
        )

        hash_value = \
        create_hash(filename)

        tx_hash = \
        save_hash(hash_value)

        insert_event(
            filename,
            hash_value,
            tx_hash
        )

        print(
            "ALERT:",
            filename
        )

        last_capture = current_time

    annotated = results[0].plot()

    cv2.imshow(
        "Smart Anti Theft",
        annotated
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()