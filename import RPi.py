import RPi.GPIO as GPIO
import time
import serial

# GPIO pin setup
motor_pin_1 = 17
motor_pin_2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin_1, GPIO.OUT)
GPIO.setup(motor_pin_2, GPIO.OUT)

# Bluetooth setup
bluetooth_serial = serial.Serial("/dev/rfcomm0", baudrate=9600)

def retract_chain_link():
    GPIO.output(motor_pin_1, GPIO.HIGH)
    GPIO.output(motor_pin_2, GPIO.LOW)
    time.sleep(5)  # Run the motor for 5 seconds
    GPIO.output(motor_pin_1, GPIO.LOW)
    GPIO.output(motor_pin_2, GPIO.LOW)

def extend_chain_link():
    GPIO.output(motor_pin_1, GPIO.LOW)
    GPIO.output(motor_pin_2, GPIO.HIGH)
    time.sleep(5)  # Run the motor for 5 seconds
    GPIO.output(motor_pin_1, GPIO.LOW)
    GPIO.output(motor_pin_2, GPIO.LOW)

if __name__ == "__main__":
    try:
        while True:
            if bluetooth_serial.in_waiting > 0:
                command = bluetooth_serial.readline().decode().strip().lower()
                if command == "retract":
                    retract_chain_link()
                elif command == "extend":
                    extend_chain_link()
                else:
                    print("Invalid command. Please send 'retract' or 'extend'.")
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
