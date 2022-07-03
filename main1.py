import RPi.GPIO as GPIO
import datetime
from time import sleep

# 초기 설정
servo_pin = 18
SERVO_MAX_DUTY = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY = 3    # 서보의 최소(0도) 위치의 주기
now = datetime.datetime.now()
today = now.day

# 서보모터 init
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz (서보모터 PWM 동작을 위한 주파수)
pwm.start(0)  # 서보의 0도 위치(0.6ms)이동:값 3.0은 pwm주기인 20ms의 3%를 의미하므로,0.6ms됨.

# 각도 설정 및 주파수 전환
degree = 91.7
duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
print("Degree: {} to {}(Duty)".format(degree, duty))
pwm.ChangeDutyCycle(duty)

print("{0} is Odd".format(today))
#홀수 flag up
pwm.ChangeDutyCycle(duty)
sleep(0.97)
pwm.ChangeDutyCycle(0)
sleep(0.97) # 5초 딜레이 후 / 추후 24시간 뒤로 바꾸던가
pwm.ChangeDutyCycle(duty)
sleep(0.97)
pwm.ChangeDutyCycle(0)
sleep(0.97)
pwm.ChangeDutyCycle(duty)
sleep(0.97)
pwm.ChangeDutyCycle(0)
sleep(5)
# 원상복귀
pwm.ChangeDutyCycle(duty)
sleep(0.97)
pwm.ChangeDutyCycle(0)
sleep(0.97)


# # 홀수 짝수에 따라 회전 횟수 변경
# if (today % 2) == 0:
#    print("{0} is Even".format(today))
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    # 짝수 Flag Up
#    pwm.ChangeDutyCycle(0)
#    sleep(5) # 5초 딜레이 후 / 추후 24시간 뒤로 바꾸던가
#    # 원상 복귀
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(0)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(0)
#    sleep(1)
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(0)
#    sleep(0.97)
#
# else:
#    print("{0} is Odd".format(today))
#    #홀수 flag up
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(0)
#    sleep(0.97) # 5초 딜레이 후 / 추후 24시간 뒤로 바꾸던가
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(0)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(0)
#    sleep(5)
#    # 원상복귀
#    pwm.ChangeDutyCycle(duty)
#    sleep(0.97)
#    pwm.ChangeDutyCycle(0)
#    sleep(0.97)

pwm.stop()
GPIO.cleanup()
