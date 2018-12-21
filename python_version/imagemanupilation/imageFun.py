from PIL import Image


#changes individual or groups of individual pixels
def changePixels(loadedImage, im):
    size =100
    shade =0
    for i in range(size):
        for j in range(size):
            loadedImage[i, j] = loadedImage[i,j] 
    
def main():
    # message limit: each character is 3 pixels, so character limit of message is 
    # total amount of pixels in picture/3 

    #Read image
    fileName = str(input("Please provide image name to hide a message in."))
    im = Image.open( '/home/dc/Projects/Stegano/imagemanupilation/'+fileName )
    print("Message limit is "+str(im.size[0]*im.size[1]/3)+" characters")
    isInputMessageAFile = str(input("Is message in a file?"))
    if isInputMessageAFile.lower()=='no':
        message = str(input("Enter message to be hidden."))
    elif isInputMessageAFile.lower()=='yes':
        fileName= str(input("Enter file name (assumed to be a .txt file, if it isn't .txt contact creator):"))
        openFile = file( fileName, 'r')
        message = processFile(openFile)

    #Display image
    im.show()

    changePixels(im.load(), im)
    im.save('altered_'+fileName)
    im.show()
    #Splitting the image into its respective bands, i.e. Red, Green,
    #and Blue for RGB
    r,g,b = im.split()

"""checks if an integer would be a valid unicode character"""
def isBetween( checkInt):
    characterValueLimits = (32,126)
    return (checkInt >= characterValueLimits[0]) or (checkInt <= characterValueLimits[1])

#process a file and returns all text in file as a single string
def processFile(openFile):
    message =''
    for line in openFile:
        message+=line.strip()+" "
    message.strip()
    return message

main()
