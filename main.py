from PIL import Image
import random

# Insert png file paths for each attribute into each list
attribute1_list = []
attribute2_list = []
attribute3_list = []

# Everytime you run the program you can add in the "Already Generated Code" here to avoid producing the same image
already_generated_codes = []


def generate_art(a1, a2, a3):
    # Merges the three attribute images
    background = Image.open(a1)
    foreground = Image.open(a2)
    foreground2 = Image.open(a3)
    background.paste(foreground, (0, 0), foreground)
    background.paste(foreground2, (0, 0), foreground2)
    background.show()


if __name__ == '__main__':
    # Picks one type for each attribute
    a = random.choice(attribute1_list)
    b = random.choice(attribute2_list)
    c = random.choice(attribute3_list)
    code = a + b + c

    # Checks if the image has already been created in order to produce a new one
    if code in already_generated_codes:
        count = 0
        while code in already_generated_codes and count < 500:
            a = random.choice(attribute1_list)
            b = random.choice(attribute2_list)
            c = random.choice(attribute3_list)
            code = a + b + c
        if count >= 500:
            print("All combinations exhausted")
        else:
            print("Already Generated Code: " + a + b + c)
            generate_art(a, b, c)

    else:
        print("Already Generated Code: " + a + b + c)
        generate_art(a, b, c)
