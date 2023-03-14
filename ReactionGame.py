from microbit import *
from random import *

rightArrow = Image('00900:'
                   '00090:'
                   '99999:'
                   '00090:'
                   '00900')
leftArrow = Image('00900:'
                  '09000:'
                  '99999:'
                  '09000:'
                  '00900')

gameOver = False
lives = 3


def startingAnimation():
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, 9)
        sleep(300)
    sleep(1000)


def livesLostAnimation():
    display.clear()
    for x in range(1, lives + 1):
        display.set_pixel(x, 2, 9)

    for x in range(5):
        display.set_pixel(lives + 1, 2, 9)
        sleep(250)
        display.set_pixel(lives + 1, 2, 0)
        sleep(250)

    sleep(400)


def tutorial():
    display.show(rightArrow)
    while not button_b.is_pressed():
        if button_a.is_pressed():
            display.show(Image.NO)
            sleep(500)
            display.show(rightArrow)
    display.show(Image.YES)
    sleep(500)
    display.show(leftArrow)
    while not button_a.is_pressed():
        if button_b.is_pressed():
            display.show(Image.NO)
            sleep(500)
            display.show(leftArrow)
    display.show(Image.YES)
    sleep(500)


def gameRound():
    global gameOver
    global lives
    randomNum = randint(1, 10)
    waitTime = 0
    if randomNum < 7:
        waitTime = randint(150, 250)
    elif 10 > randomNum > 6:
        waitTime = randint(250, 500)
    elif randomNum == 10:
        waitTime = randint(500, 1500)
    sleep(waitTime)
    randomNum = randint(0, 1)
    buttonIsPressed = False
    if randomNum == 0:
        display.show(leftArrow)
        while not buttonIsPressed:
            if button_a.is_pressed():
                buttonIsPressed = True
            elif button_b.is_pressed():
                display.show(Image.NO)
                sleep(1000)
                lives -= 1
                buttonIsPressed = True
                livesLostAnimation()

    if randomNum == 1:
        display.show(rightArrow)
        while not buttonIsPressed:
            if button_b.is_pressed():
                buttonIsPressed = True
            elif button_a.is_pressed():
                display.show(Image.NO)
                sleep(1000)
                lives -= 1
                buttonIsPressed = True
                livesLostAnimation()
    display.clear()
    if lives == 0:
        gameOver = True



def game():
    global gameOver
    gameOver = False
    global lives
    lives = 3
    display.clear()
    startingAnimation()
    while not gameOver:
        gameRound()
    display.scroll("GAME OVER")


tutorial()
game()
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        game()

