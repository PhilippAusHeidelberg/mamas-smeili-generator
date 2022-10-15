def on_button_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_ab():
    basic.show_leds("""
        # # . # #
                # # . # #
                . . . . .
                . # # # .
                # . . . #
    """)
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    basic.show_icon(IconNames.SAD)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)
