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
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, 165, SuperBit.enMotors.M2, 165)
        SuperBit.motor_run_dual(SuperBit.enMotors.M3, 255, SuperBit.enMotors.M4, 255)
    elif uart == "B":
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # . # .
                        . . # . .
        """)
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, -165, SuperBit.enMotors.M2, -165)
        SuperBit.motor_run_dual(SuperBit.enMotors.M3, -255, SuperBit.enMotors.M4, -255)
    elif uart == "C":
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # . #
                        . . . # .
                        . . # . .
        """)
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, -200, SuperBit.enMotors.M2, 255)
        SuperBit.motor_run_dual(SuperBit.enMotors.M3, 180, SuperBit.enMotors.M4, -255)
    elif uart == "D":
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # . # # #
                        . # . . .
                        . . # . .
        """)
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, 180, SuperBit.enMotors.M2, -255)
        SuperBit.motor_run_dual(SuperBit.enMotors.M3, -170, SuperBit.enMotors.M4, 255)
    elif uart == "E":
        basic.show_leds("""
            . # . . .
                        # . # # #
                        . # . . #
                        . . . . #
                        . # # # #
        """)
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, -40, SuperBit.enMotors.M2, -40)
        SuperBit.motor_run_dual(SuperBit.enMotors.M3, 40, SuperBit.enMotors.M4, 40)
    elif uart == "F":
        basic.show_leds("""
            . . . # .
                        # # # . #
                        # . . # .
                        # . . . .
                        # # # # .
        """)
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, 40, SuperBit.enMotors.M2, 40)
        SuperBit.motor_run_dual(SuperBit.enMotors.M3, -40, SuperBit.enMotors.M4, -40)
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, 0, SuperBit.enMotors.M2, 0)
        SuperBit.motor_run_dual(SuperBit.enMotors.M3, 0, SuperBit.enMotors.M4, 0)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

uart = ""
bluetooth.start_uart_service()
bluetooth.set_transmit_power(7)
