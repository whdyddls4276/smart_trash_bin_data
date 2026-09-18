import RPi.GPIO as GPIO
import time

# 초음파 센서 핀 (BCM 기준)
TRIG = 10
ECHO = 9

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    timeout = time.time() + 0.05
    while GPIO.input(ECHO) == 0:
        if time.time() > timeout:
            print("[DEBUG] Echo rising timeout")
            return -1
    start = time.time()

    timeout = time.time() + 0.05
    while GPIO.input(ECHO) == 1:
        if time.time() > timeout:
            print("[DEBUG] Echo falling timeout")
            return -1
    stop = time.time()

    duration = stop - start
    distance = duration * 34300 / 2
    return distance

try:
    while True:
        dist = get_distance()
        if dist != -1:
            print(f"Distance: {dist:.1f} cm")
        else:
            print("Measurement failed")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    GPIO.cleanup()