def on_bluetooth_connected():
    global Connectet
    Connectet = 1
    basic.show_icon(IconNames.SMALL_HEART)
    basic.show_icon(IconNames.HEART)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global Connectet
    Connectet = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_ab():
    global Active_Mouse
    Active_Mouse = 1 - Active_Mouse
    mouse.click()
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

Active_Mouse = 0
Connectet = 0
mouse.start_mouse_service()
keyboard.start_keyboard_service()
basic.show_icon(IconNames.HAPPY)

def on_forever():
    while 1 == Active_Mouse:
        if input.button_is_pressed(Button.B):
            mouse.right_click()
        if input.button_is_pressed(Button.A):
            mouse.click()
        if input.acceleration(Dimension.Y) > 90:
            mouse.movexy(0, 20)
        if input.acceleration(Dimension.Y) < 90:
            mouse.movexy(0, -20)
        if input.acceleration(Dimension.X) > 90:
            mouse.movexy(20, 0)
        if input.acceleration(Dimension.X) < 90:
            mouse.movexy(-20, 0)
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)

def on_forever3():
    while Connectet == 0:
        basic.show_leds("""
            . . . . .
            . # # . .
            . # . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . # . . .
            . # . . .
            . # . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . . .
            . # # . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . # .
            . . # # .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . # .
            . . . # .
            . . . # .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . # # .
            . . . # .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            . . . . #
            """)
basic.forever(on_forever3)
