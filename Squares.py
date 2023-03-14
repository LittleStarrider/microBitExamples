from microbit import *
from random import *


def squares():
    waitBetweenPic = 1500
    waitBetweenLine = 200
    waitBetweenPixel = 50

    for y in range(5):
        for x in range(5):
            display.set_pixel(x, y, 9)
            sleep(waitBetweenPixel)
        sleep(waitBetweenLine)
    sleep(waitBetweenPic)
    display.clear()
    for x in range(4, -1, -1):
        for y in range(5):
            display.set_pixel(x, y, 9)
            sleep(waitBetweenPixel)
        sleep(waitBetweenLine)
    sleep(waitBetweenPic)
    display.clear()
    for y in range(4, -1, -1):
        for x in range(4, -1, -1):
            display.set_pixel(x, y, 9)
            sleep(waitBetweenPixel)
        sleep(waitBetweenLine)
    sleep(waitBetweenPic)
    display.clear()
    for x in range(5):
        for y in range(4, -1, -1):
            display.set_pixel(x, y, 9)
            sleep(waitBetweenPixel)
        sleep(waitBetweenLine)
    sleep(waitBetweenPic)
    display.clear()


def star():
    imagelist = [Image('00200:'
                       '00400:'
                       '24742:'
                       '00400:'
                       '00200'),
                 Image('00300:'
                       '00500:'
                       '35753:'
                       '00500:'
                       '00300'),
                 Image('00500:'
                       '04740:'
                       '57875:'
                       '04740:'
                       '00500'),
                 Image('00600:'
                       '04840:'
                       '68986:'
                       '04840:'
                       '00600'),
                 Image('01610:'
                       '17871:'
                       '68986:'
                       '17871:'
                       '01610'),
                 Image('01810:'
                       '17971:'
                       '89998:'
                       '17971:'
                       '01810'),
                 ]
    for x in range(4):
        for image in imagelist:
            display.show(image)
            sleep(250)
        for image in reversed(imagelist):
            display.show(image)
            sleep(250)
        display.clear()
    display.clear()


def square_pulse():
    intensity = 0

    for i in range(5):
        for intensity in range(10):
            for x in range(5):
                for y in range(5):
                    display.set_pixel(x, y, intensity)
            sleep(100)
        for intensity in range(9, -1, -1):
            for x in range(5):
                for y in range(5):
                    display.set_pixel(x, y, intensity)
            sleep(100)
    display.clear()


def random_dots():
    for i in range(9):
        xy_coordinates = []
        for x in range(5):
            while True:
                xy = (randint(0, 4), randint(0, 4))
                if xy not in xy_coordinates:
                    display.set_pixel(xy[0], xy[1], 9)
                    xy_coordinates.append(xy)
                    break
            display.set_pixel(xy[0], xy[1], 9)
        sleep(1500)
        display.clear()
    display.clear()


def spin():
    imagelist = [Image('00900:'
                       '00900:'
                       '00900:'
                       '00900:'
                       '00900'),
                 Image('00090:'
                       '00900:'
                       '00900:'
                       '00900:'
                       '09000'),
                 Image('00009:'
                       '00090:'
                       '00900:'
                       '09000:'
                       '90000'),
                 Image('00000:'
                       '00009:'
                       '09990:'
                       '90000:'
                       '00000'),
                 Image('00000:'
                       '00000:'
                       '99999:'
                       '00000:'
                       '00000'),
                 Image('00000:'
                       '90000:'
                       '09990:'
                       '00009:'
                       '00000'),
                 Image('90000:'
                       '09000:'
                       '00900:'
                       '00090:'
                       '00009'),
                 Image('09000:'
                       '00900:'
                       '00900:'
                       '00900:'
                       '00090')
                 ]
    for x in range(17):
        for image in imagelist:
            display.show(image)
            sleep(80)
    display.clear()


def random_dots_fill():
    for y in range(5):
        xy_coordinates = []
        for i in range(25):
            while True:
                xy = (randint(0, 4), randint(0, 4))
                if xy not in xy_coordinates:
                    display.set_pixel(xy[0], xy[1], 9)
                    xy_coordinates.append(xy)
                    break
            sleep(100)
        sleep(1500)
        display.clear()


def running_dots():
    for u in range(12):
        x = 0
        y = 0
        x1 = 4
        y1 = 4
        for i in range(4):
            for j in range(5):
                display.set_pixel(x, j, 9)
                display.set_pixel(j, y, 9)
                display.set_pixel(x1, j, 9)
                display.set_pixel(j, y1, 9)
            x += 1
            y += 1
            x1 -= 1
            y1 -= 1
            sleep(200)
            display.clear()


def spiral():
    speed = 100
    x = 2
    y = 2
    display.set_pixel(x, y, 9)
    sleep(speed)
    revert = False

    for s in range(6):
        x = 2
        y = 2
        display.set_pixel(x, y, 0 if revert else 9)
        finish = False
        step = 1
        while True:
            if step % 2 == 1:
                for j in range(step):
                    y -= 1
                    display.set_pixel(x, y, 0 if revert else 9)
                    sleep(speed)
                    if y == 0 and x == 4:  # top right corner of the matrix
                        finish = True
                        revert = not revert
                        break
                if finish:
                    break
                for j in range(step):
                    x -= 1
                    display.set_pixel(x, y, 0 if revert else 9)
                    sleep(speed)
            else:
                for j in range(step):
                    y += 1
                    display.set_pixel(x, y, 0 if revert else 9)
                    sleep(speed)
                for j in range(step):
                    x += 1
                    display.set_pixel(x, y, 0 if revert else 9)
                    sleep(speed)
            step += 1


def waves():
    imagelist = [Image('00000:'
                       '00000:'
                       '00900:'
                       '00000:'
                       '00000'),
                 Image('00000:'
                       '09990:'
                       '09090:'
                       '09990:'
                       '00000'),
                 Image('99999:'
                       '90009:'
                       '90009:'
                       '90009:'
                       '99999')
                ]
    for i in range(10):
        for image in imagelist:
            display.show(image)
            sleep(200)
        display.clear()
        imagelist.reverse()
        sleep(500)


while True:
    random = randint(9, 9)
    if random == 1:
        squares()
    elif random == 2:
        star()
    elif random == 3:
        square_pulse()
    elif random == 4:
        random_dots()
    elif random == 5:
        spin()
    elif random == 6:
        random_dots_fill()
    elif random == 7:
        running_dots()
    elif random == 8:
        spiral()
    elif random == 9:
        waves()
