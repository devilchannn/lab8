from PIL import Image, ImageFont, ImageDraw

def lab1():

    image = Image.open('newcard.jpg')
    imcrop = image.crop((100, 100, 400, 400))
    imcrop.save('imcropped.jpg')
    imcrop.show()

def lab2():
    s = {'Новый год': 'ny.jpg', '8 марта': '8m.jpg', '23 февраля': '23f.jpg', 'Рождество': 'roz.jpg'}
    p = input('Какой праздник?')
    img = Image.open(s[p])
    img.show()

def lab3():
    image = Image.open('newcard.jpg')
    name = input('Введите имя: ')
    fon = ImageFont.truetype('arial_bold.ttf', 40)
    img = ImageDraw.Draw(image)
    img.text((40, 400), name + ', поздравляю!', font = fon, fill = 'white')
    image.show()

