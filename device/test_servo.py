import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(18, 50)
servo.start(0)

servo.ChangeDutyCycle(7.0)  # 90도
time.sleep(1)
servo.ChangeDutyCycle(0)
time.sleep(1)

servo.ChangeDutyCycle(2.5)  # 0도
time.sleep(1)
servo.ChangeDutyCycle(0)

servo.stop()
GPIO.cleanup()