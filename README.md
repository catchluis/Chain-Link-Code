# Chain-Link-Code
Two codes for blue tooth retractable chain link 
import RPi.GPIO as GPIO
import time

# GPIO pin setup
motor_pin_1 = 17
motor_pin_2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin_1, GPIO.OUT)
GPIO.setup(motor_pin_2, GPIO.OUT)

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
            command = input("Enter command (retract/extend/quit): ").strip().lower()
            if command == "retract":
                retract_chain_link()
            elif command == "extend":
                extend_chain_link()
            elif command == "quit":
                break
            else:
                print("Invalid command. Please enter 'retract', 'extend', or 'quit'.")
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
