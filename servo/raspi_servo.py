import pywss
import time
import RPi.GPIO as GPIO
time.sleep(20)
servo_pin = 12                # 舵机信号线接树莓派GPIO17
millsecond=1500
deg_delay=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo_pin, GPIO.OUT, initial=False)
 
# 旋转角度转换到PWM占空比
def angleToDutyCycle(angle):
    return 2.5 + angle / 180.0 * 10

def millsecondToDutyCycle(ms):
    return ms/1000/20*100
 
p = GPIO.PWM(servo_pin, 50)    # 初始频率为50HZ
p.start(angleToDutyCycle(90))  # 舵机初始化角度为90
time.sleep(0.5)
p.ChangeDutyCycle(0)           # 清空当前占空比，使舵机停止抖动
 
# if __name__ == '__main__':
#     print('当前为90度')
#     while True:
#         angle = int(input('旋转度数：'))
#         if angle >= 0 and angle <= 180:
#             p.ChangeDutyCycle(angleToDutyCycle(angle))
#             time.sleep(0.1)
#             p.ChangeDutyCycle(0) # 清空当前占空比，使舵机停止抖动
#         else:
#             print('旋转度数在0-180之间！')

def writeMillsecondsHandler(ctx:pywss.Context):
    global millsecond
    dist=abs(float(ctx.route_params["mill"])-millsecond)/1200
    millsecond=int(ctx.route_params["mill"])
    p.ChangeDutyCycle(millsecondToDutyCycle(millsecond))
    time.sleep(0.8)
    p.ChangeDutyCycle(0)
    ctx.write_text("Servo millsecond updated to %d"%millsecond)

def writeModeHandler(ctx:pywss.Context):
    global millsecond
    mode=ctx.route_params["mode"]
    ctx.write_text("Servo mode is switching to %s"%mode)
    time.sleep(20)
    ctx.write_text("Servo mode switched to %s"%mode)

def writeTimingHandler(ctx:pywss.Context):
    global millsecond
    timing=int(ctx.route_params["time"])
    ctx.write_text("Servo deg_delay timing set to %d"%timing)

def index(ctx:pywss.Context):
    ctx.set_header("Content-Type", "text/html")
    fp=open("index.html","r",encoding='utf-8')
    html=fp.read()
    fp.close()
    ctx.write_text(html)

app = pywss.App()
app.get("/",index)
app.get("/servo/millseconds/{mill}", writeMillsecondsHandler)
app.get("/servo/mode/{mode}", writeModeHandler)
app.get("/servo/timing/{time}", writeTimingHandler)
time.sleep(60)
app.run(port=9600)