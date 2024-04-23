from gpiozero import Button
from time import sleep

button27 = Button(27)# used Stats
button19 = Button(19) #used Items
button18 = Button(18)
button20 = Button(20) #used MAP
button21 = Button(21)
button16 = Button(16)
button22 = Button(22)
# button23 = Button(23) #Reboots system if called pin 16
button26 = Button(26) #No edge detection pin 18
# button25 = Button(25)
while True:
    
    if button20.is_pressed:
        print("20 Pressed pin7")
    elif button19.is_pressed:
        print("19 Pressed pin xx")
    elif button18.is_pressed:
        print("18 Pressed pin 12")
    # elif button27.is_pressed:
    #     print("27 Pressed pin 13")
    elif button21.is_pressed:
        print("21 Pressed pin 15")
    elif button22.is_pressed:
        print("22 Pressed pin 15")
    elif button16.is_pressed:
        print("16 Pressed pin 15")
    # elif button23.is_pressed:
    #    print("23 Pressed pin 16")
    elif button26.is_pressed:
       print("26 Pressed pin 18")
    sleep(1)
