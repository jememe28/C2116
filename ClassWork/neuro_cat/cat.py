import cv2
from PIL import Image

image_path = 'd:/Progrming/Python/reposit/C2116/ClassWork/neuro_cat/cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('d:/Progrming/Python/reposit/C2116/ClassWork/neuro_cat/haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open('d:/Progrming/Python/reposit/C2116/ClassWork/neuro_cat/glasses.png')

cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h / 3)))
    cat.paste(glasses, (x, int(y + h / 4)), glasses)

cat.save("d:/Progrming/Python/reposit/C2116/ClassWork/neuro_cat/cat_with_glasses.png")
cat_with_glasses = cv2.imread("d:/Progrming/Python/reposit/C2116/ClassWork/neuro_cat/cat_with_glasses.png")

cv2.imshow("d:/Progrming/Python/reposit/C2116/ClassWork/neuro_cat/Cat_with_glasses", cat_with_glasses)
cv2.waitKey()