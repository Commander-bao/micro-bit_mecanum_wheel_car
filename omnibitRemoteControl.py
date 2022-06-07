def on_bluetooth_connected():
    basic.show_icon(IconNames.SKULL)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global uart
    uart = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    if uart == "A":
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        OmniBit.car_run(OmniBit.enCarRun.FORWARD, 255)
    elif uart == "B":
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # . # .
                        . . # . .
        """)
        OmniBit.car_run(OmniBit.enCarRun.BACK, 255)
    elif uart == "C":
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # . #
                        . . . # .
                        . . # . .
        """)
        OmniBit.car_run(OmniBit.enCarRun.MOVE_RIGHT, 255)
    elif uart == "D":
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # . # # #
                        . # . . .
                        . . # . .
        """)
        OmniBit.car_run(OmniBit.enCarRun.MOVE_LEFT, 255)
    elif uart == "E":
        basic.show_leds("""
            . # . . .
                        # . # # #
                        . # . . #
                        . . . . #
                        . # # # #
        """)
        OmniBit.car_run(OmniBit.enCarRun.SPIN_LEFT, 40)
    elif uart == "F":
        basic.show_leds("""
            . . . # .
                        # # # . #
                        # . . # .
                        # . . . .
                        # # # # .
        """)
        OmniBit.car_run(OmniBit.enCarRun.SPIN_RIGHT, 40)
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        OmniBit.car_run(OmniBit.enCarRun.FORWARD, 0)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

uart = ""
bluetooth.start_uart_service()
bluetooth.set_transmit_power(7)
