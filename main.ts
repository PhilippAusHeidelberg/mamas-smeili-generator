input.onButtonEvent(Button.A, input.buttonEventClick(), function on_button_a() {
    basic.showIcon(IconNames.Happy)
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function on_button_ab() {
    basic.showLeds(`
        # # . # #
                # # . # #
                . . . . .
                . # # # .
                # . . . #
    `)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function on_button_b() {
    basic.showIcon(IconNames.Sad)
})
