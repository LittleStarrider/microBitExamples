from microbit import *

while True:
    if button_b.is_pressed():
        while button_b.is_pressed():
            display.show(Image('00900:'
                               '00090:'
                               '99999:'
                               '00090:'
                               '00900'))
            sleep(50)
            display.clear()
            sleep(50)
    if button_a.is_pressed():
        while button_a.is_pressed():
            display.show(Image('00900:'
                               '09000:'
                               '99999:'
                               '09000:'
                               '00900'))
            sleep(50)
            display.clear()
            sleep(50)
