import src_poc.Logger as Logger
from PIL import Image

def read_file(filePath):
    lines = []
    with open(filePath,'r') as file:
        for line in file:
            lines.append(line)
            # Logger.log_info(line)
            # Logger.log_info(line[0])

            # words = line.split('=')
            # Logger.log_info(words)

            # if words[0] == 'Highscore':
                # Logger.info("The highscore is " + words[1])
    return lines

def write_file(filePath, contents):
    with open(filePath,'w') as file:
        file.write(contents)

def update_file(filePath, newFilePath):
    with open(filePath,'r') as readFile:
        with open(newFilePath,'w') as writeFile:
            for line in readFile:
                words = line.split('=')
                newLine = line

                if words[0] == 'Highscore':
                    words[1] = '75'
                    newLine = words[0] + '=' + words[1]
                
                writeFile.write(newLine)

def read_image_file(filePath):
    image = Image.open(filePath)
    pixels = image.load()
    size = image.size
    x = 0
    y = 0
    while x < size[0]:
        Logger.info('Column: ' + str(x))
        while y < size[1]:
            Logger.info(pixels[x,y])
            y += 1
        x += 1
        y = 0

# read_file()
# write_file()
# update_file()
# read_image_file()