import RPi.GPIO as GPIO
import datetime
from time import sleep
import requests
import json

# 초기 설정
servo_pin = 18
SERVO_MAX_DUTY = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY = 3    # 서보의 최소(0도) 위치의 주기
now = datetime.datetime.now()
today = now.day

# URL 읽기
f = open("/home/espriter/github/servomotor_move_when_even_odd_days/webhook_url.txt", 'r')
url_read = f.readline()
f.close()

# 슬랙 메시지 설정
def send_message_to_slack(text):
    url = url_read
    headers = {"Content-type": "application/json"}
    data = {"text": text }
    res = requests.post(url_read, headers=headers, data=json.dumps(data))
    print(res.status_code)

# 서보모터 init
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz (서보모터 PWM 동작을 위한 주파수)
pwm.start(0)  # 서보의 0도 위치(0.6ms)이동:값 3.0은 pwm주기인 20ms의 3%를 의미하므로,0.6ms됨.

# 각도 설정 및 주파수 전환
degree = 90
duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
print("Degree: {} to {}(Duty)".format(degree, duty))


# 짝수일 기준
if (today % 2) == 0:
    print("{0} 은 짝수".format(today))
    pwm.ChangeDutyCycle(duty)
    sleep(1.05)
    pwm.ChangeDutyCycle(0)
    sleep(14400)
    pwm.ChangeDutyCycle(duty)
    sleep(0.9)
    pwm.ChangeDutyCycle(0)
    sleep(0)
    pwm.ChangeDutyCycle(duty)
    sleep(0.9)
    pwm.ChangeDutyCycle(0)
    sleep(0)
    pwm.ChangeDutyCycle(duty)
    sleep(0.92)
    pwm.ChangeDutyCycle(0)
    sleep(0)
    send_message_to_slack("오늘은 짝수 날짜 랍니다! 🚩")

# 홀수일 기준
else:
    print("{0} 는 홀수".format(today))
    pwm.ChangeDutyCycle(duty)
    sleep(1.05)
    pwm.ChangeDutyCycle(0)
    sleep(0)
    pwm.ChangeDutyCycle(duty)
    sleep(0.9)
    pwm.ChangeDutyCycle(0)
    sleep(0)
    pwm.ChangeDutyCycle(duty)
    sleep(0.9)
    pwm.ChangeDutyCycle(0)
    sleep(14400)
    pwm.ChangeDutyCycle(duty)
    sleep(0.92)
    pwm.ChangeDutyCycle(0)
    sleep(0)
    send_message_to_slack("오늘은 홀수 날짜 랍니다! 🏳️")

pwm.stop()
GPIO.cleanup()

