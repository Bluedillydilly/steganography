from PIL import Image # hdhdh
from encodeWithBytes import encrypt

def main():
    """ message limit: each character is 3 pixels,
        we're using diagonals so 1 for every 2 pixels, so character limit of message is
        # total amount of pixels in picture/3/2
    """
    #Read image
    # fileName = str(
            # raw_input("Please provide image name to hide a message in(include extension):\n"))
    # im = Image.open( '/home/dc/Projects/Stegano/imagemanupilation/'+fileName)
    # print("Message limit is "+str(im.size[0]*im.size[1]/6)+" characters")
    # isInputMessageAFile = str(raw_input("Is message in a file?:\n"))
    # if isInputMessageAFile.lower()=='no':
    #     message = str(raw_input("Enter message to be hidden:\n"))
    # elif isInputMessageAFile.lower()=='yes':
    #     fileName= str(
            # raw_input("Enter file name (assumed to be a .txt file, if it isn't .txt contact creator):"))
    #     openFile = file( fileName, 'r')
    #     message = processFile(openFile)
    # else:
    #     print("Invalid input")
    #     return
    image = Image.open('testPNG.png')
    message = "Hello."
    #Display image
    image.show()
    print(string_to_byte(message))
    encrypt(image, string_to_byte(message))
    image.save('altered_image.png')#saves new image with hidden message
    image.show()

def is_between(check_int):
    """
        checks if an integer would be a valid unicode character
    """
    character_value_limits = (32, 126)
    return character_value_limits[0] <= check_int <= character_value_limits[1]

def process_file(open_file):
    """
        process a file and returns all text in file as a single string
    """
    message = ''
    for line in open_file:
        message += line.strip()+" "
    message.strip()
    return message

def string_to_byte(message):
    """
        returns the bytearray of a string
    """
    byte_array = []
    for char in message:
        char_value = ord(char) if char is int else char
        byte_array.append(char_to_byte(char_value))
    return byte_array

def char_to_byte(char_value):
    """
        return bytearray of a character
    """
    byte = [0, 0, 0, 0, 0, 0, 0, 0]
    value = ord(char_value)
    for i in range(7, -1, -1):
        if value >= 2**i:
            byte[7-i] = 1
            value -= 2**i
    return byte

main()
