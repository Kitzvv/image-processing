import time
from PIL import Image, ImageEnhance




def starting_txt():
    print("Welcome to photo editor")
    print("What do u want to do?")


def resize():
    if program == "R":
        choose_img = input("Enter your img file: ")
        choose_width = int(input("Enter photo width: "))
        choose_height = int(input("Enter photo height: "))
        image = Image.open(choose_img)
        new_image = image.resize((choose_width, choose_height))
        new_image.save("resized_img.png")
        ending_text()


def ending_text():
    print("Done")
    print("Program will quit in a moment")
    time.sleep(3)
    quit()


def choose_img(x):
    choose_img = input("Enter your img file: ")
    image = Image.open(choose_img)
    rgb_change = image.convert("RGB")
    rgb_change.save(f"new_img.{x}")


def pick_filters():
    choose_img = input("Enter your img file: ")
    image = Image.open(choose_img)
    global rgb_change
    rgb_change = image.convert("RGB")


def contrast():
    contrast = ImageEnhance.Contrast(rgb_change)
    contrast.enhance(1.5).save("contrast.jpg")


def sharpness():
    sharpness = ImageEnhance.Sharpness(rgb_change)
    sharpness.enhance(1.5).save("sharpness.jpg")


def chooser():
    global program
    loops = True
    while loops:
        program = input("(R)ezise, (C)hange type, Use (F)ilter, (Rotate): ").upper()
        if program in ["R", "C", "F", "ROTATE"]:
            loops = False
        else:
            print("Use one of these 3 options")

def rotate():
    if program == "ROTATE":
        choose_img = input("Enter your img file: ")
        image = Image.open(choose_img)
        rotate_angle = int(input("Enter value to rotate your photo: "))
        out = image.rotate(rotate_angle)
        out.save("rotated_photo.png")
        ending_text()



def change_type():
    change_type = True
    if program == "C":
        while change_type:
            img_type = input("From png to jpg? (1) or jpg to png? (2): ")
            if img_type == "1":
                choose_img("jpg")
                ending_text()
            elif img_type == "2":
                choose_img("png")
                ending_text()
            else:
                print("Enter 1 or 2 bruh")


def filters():
    checker = True
    if program == "F":
        while checker:
            print("Choose one of those options")
            filter_choose = input("(M)ono,(C)ontrast,(S)harpness: ").upper()
            if filter_choose == "M":
                choose_img = input("Enter your img file: ")
                image = Image.open(choose_img)
                greyscale_image = image.convert("L")
                greyscale_image.save("Mono_pic.jpg")
                ending_text()
                break
            elif filter_choose == "C":
                pick_filters()
                contrast()
                ending_text()
                break
            elif filter_choose == "S":
                pick_filters()
                sharpness()
                ending_text()
                break
            else:
                print("i said choose one of these option dude!")


def main():
    starting_txt()
    chooser()
    change_type()
    rotate()
    resize()
    filters()


if __name__ == "__main__":
    main()

