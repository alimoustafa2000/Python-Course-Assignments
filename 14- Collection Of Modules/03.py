from PIL import Image


# Open the image
my_image = Image.open("G:\elzero-pillow.jpg")

# crop "L" letter
box1 = (400, 0, 800, 400)
letter_l = my_image.crop(box1)

# convert "L" letter to grayscale mood
gray_letter_l = letter_l.convert("L")

# save "L" letter image
gray_letter_l.save('G:/first_task.jpg')

# ===============================================

# crop 2nd row
box2 = (0, 400, 1200, 800)
second_row = my_image.crop(box2)

# convert 2nd row to grayscale mood
gray_second_row = second_row.convert("L")

# rotate 2nd row image
angle = 180
rotated_image = gray_second_row.rotate(angle)

# save 2nd row image
rotated_image.save('G:/second_task.jpg')

