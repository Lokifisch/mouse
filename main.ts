bluetooth.onBluetoothConnected(function () {
    Connectet = 1
    basic.showIcon(IconNames.SmallHeart)
    basic.showIcon(IconNames.Heart)
})
bluetooth.onBluetoothDisconnected(function () {
    Connectet = 0
    basic.showIcon(IconNames.Sad)
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    Active_Mouse = 1 - Active_Mouse
    mouse.click()
})
let Active_Mouse = 0
let Connectet = 0
mouse.startMouseService()
keyboard.startKeyboardService()
basic.showIcon(IconNames.Happy)
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        mouse.rightClick()
    }
    if (input.buttonIsPressed(Button.A)) {
        mouse.click()
    }
})
basic.forever(function () {
    while (1 == Active_Mouse) {
        if (input.acceleration(Dimension.Y) > 90) {
            mouse.movexy(0, 20)
        }
        if (input.acceleration(Dimension.Y) < 90) {
            mouse.movexy(0, -20)
        }
        if (input.acceleration(Dimension.X) > 90) {
            mouse.movexy(20, 0)
        }
        if (input.acceleration(Dimension.X) < 90) {
            mouse.movexy(-20, 0)
        }
    }
})
basic.forever(function () {
	
})
basic.forever(function () {
    while (Connectet == 0) {
        basic.showLeds(`
            . . . . .
            . # # . .
            . # . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # . . .
            . # . . .
            . # . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . # . . .
            . # # . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . # .
            . . # # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . # .
            . . . # .
            . . . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . # # .
            . . . # .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
