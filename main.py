import cv2 as cv
import easyocr
import matplotlib.pyplot as plt

# read image
image_path = r'G:\Career\Curriculum\Courses\Advanced Computer Vision\Text Recognition\data\test3.png'
img = cv.imread(image_path)

# instantiate text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t in text_:
    print(t)

    bbox, text, score = t

    if score > 0.25:
        cv.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv.putText(img, text, bbox[0], cv.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()