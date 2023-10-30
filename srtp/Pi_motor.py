import RPi.GPIO as GPIO
import time
import pigpio  # 用于舵机控制

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 定义LED引脚（示例中使用的是LED_BUILTIN，根据实际连接修改）
led_pin = 12  # 替换为实际的GPIO引脚

# 初始化LED引脚
GPIO.setup(led_pin, GPIO.OUT)

# 初始化pigpio库
pi = pigpio.pi()

try:
    while True:
        # 点亮LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("45 Horizontal Init Pos")

        # 控制舵机
        pi.set_servo_pulsewidth(17, 135)  # 替换为实际的GPIO引脚和位置

        time.sleep(0.5)

        print("Recyclable")

        # 控制舵机
        pi.set_servo_pulsewidth(17, 180)  # 替换为实际的GPIO引脚和位置

        time.sleep(1.5)

        print("Harmful")

        # 控制舵机
        pi.set_servo_pulsewidth(17, 135)  # 替换为实际的GPIO引脚和位置

        time.sleep(0.5)

        print("other")

        # 控制舵机
        pi.set_servo_pulsewidth(17, 90)  # 替换为实际的GPIO引脚和位置

        time.sleep(1.5)

        print("Organic")

        # 控制舵机
        pi.set_servo_pulsewidth(17, 90)  # 替换为实际的GPIO引脚和位置

        time.sleep(1.5)

except KeyboardInterrupt:
    pass

# 清理GPIO引脚和pigpio资源
GPIO.cleanup()
pi.stop()
