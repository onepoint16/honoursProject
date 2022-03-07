import cv2
import numpy as np

def apply_mask(image, mask, color, alpha=0.5):
    """apply mask to image"""
    for n, c in enumerate(color):
        image[:, :, n] = np.where(
            mask == 1,
            image[:, :, n] * (1 - alpha) + alpha * c,
            image[:, :, n]
        )
    return image

# based on https://github.com/matterport/Mask_RCNN/blob/master/mrcnn/visualize.py
# and https://github.com/markjay4k/Mask-RCNN-series/blob/887404d990695a7bf7f180e3ffaee939fbd9a1cf/visualize_cv.py
def display_instances(image, boxes, masks, class_ids, class_names, scores=None):
    assert boxes.shape[0] == masks.shape[-1] == class_ids.shape[0]
    
    N = boxes.shape[0]

    colors = colors = [tuple(255 * np.random.rand(3)) for _ in range(N)]

    for i, c in enumerate(colors):
        if not np.any(boxes[i]):
            continue
        
        y1, x1, y2, x2 = boxes[i]
        label = class_names[class_ids[i]]
        score = scores[i] if scores is not None else None
        caption = "{} {:.3f}".format(label, score) if score else label

        # Mask
        mask = masks[:, :, i]
        image = apply_mask(image, mask, c)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), c, 2)
        image = cv2.putText(image, caption, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, c, 2)
    return image