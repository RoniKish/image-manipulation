# The images used should be inside the python project folder, other wise a full
# Path is needed to access them
from PIL import Image
import os.path


# Interface for the software
def interface():
    # Functions menu
    menu = {
        1: show_image,
        2: resize_image,
        3: duplicate_image,
        4: diverse_image,
        5: save_image
    }
    pick = 1
    # I used test_1.png,test_2.png as names
    print('Welcome to my testing software ^^')
    path = input('Enter the file name: ')
    # In case the file was not found
    if not os.path.isfile(path):
        while not os.path.isfile(path):
            path = input('The file was not found, enter the name again: ')
    while pick != 0:
        print('Please select programs 1-5 or enter 0 if u wish to exit')
        print('1 to watch the image')
        print('2 to resize the image')
        print('3 to multiply the image')
        print('4 to diverse the image')
        print('5 to save the image')
        print('6 to pick another image')
        pick = int(input('your input: '))
        # In case the user wish to exit
        if pick == 0:
            break
        # In case the user wish to change the image
        if pick == 6:
            path = input('Enter the file name: ')
            continue
        # In case the pick is out of bounds
        if pick < 0 or pick > 6:
            print('You must select a number between 0 to 2')
            continue
        menu[pick](path)


def duplicate_image(path):
    # Takes the number of times the user wish to duplicate the image
    runs = int(input('Enter the number of times u wish to multiply the image: '))
    # If the image was already changed open the changed version, other wise create a result file
    if os.path.isfile('result.png'):
        image = Image.open('result.png')
    else:
        image = Image.open(path)
        image.save('result.png')
    # Duplicates the image the number of times we want
    for i in range(runs):
        image = Image.open('result.png')
        width, height = image.size
        box = (0, 0, (width * 2), (height * 2))
        cropped_image = image.crop(box)
        image_copy = cropped_image.copy()
        # Decides on the new spaces the image will be positioned in
        position_1 = (width, 0, (width * 2), height)
        position_2 = (0, height, width, (height * 2))
        position_3 = (width, height, (width * 2), (height * 2))
        # Pastes the original image in the 3 newly created spaces
        image_copy.paste(image, position_1)
        image_copy.paste(image, position_2)
        image_copy.paste(image, position_3)
        # Saves the new image
        image_copy.save('result.png')


def resize_image(path):
    # Enter the width and height we wish to change
    width = int(input('Enter the width of the image: '))
    height = int(input('Enter the height of the image: '))
    # If the image was already changed open the changed version, other wise create a result file
    if os.path.isfile('result.png'):
        image = Image.open('result.png')
    else:
        image = Image.open(path)
        image.save('result.png')
    # Creates and saves the image
    new_image = image.resize((width, height))
    new_image.save('result.png')


def show_image(path):
    if os.path.isfile('result.png'):
        image = Image.open('result.png')
    else:
        image = Image.open(path)
    image.show()


def diverse_image(path):
    # Takes the number of times the user wish to diverse the image
    runs = int(input('Enter the number of times u wish to diverse the image: '))
    # If the image was already changed open the changed version, other wise create a result file
    if os.path.isfile('result.png'):
        image = Image.open('result.png')
    else:
        image = Image.open(path)
        image.save('result.png')
    # Diverse the image the number of times we want
    for i in range(runs):
        image = Image.open('result.png')
        width, height = image.size
        box = (0, 0, (width / 2), (height / 2))
        cropped_image = image.crop(box)
        # Saves the new image
        cropped_image.save('result.png')


def save_image(path):
    # If the image was already changed open the changed version, other wise create a result file
    if os.path.isfile('result.png'):
        image = Image.open('result.png')
    else:
        image = Image.open(path)
    name = input('Enter the image name: ')
    name = name + '.png'
    image.save(name)


interface()
# Deletes the changed image
if os.path.isfile('result.png'):
    os.remove('result.png')