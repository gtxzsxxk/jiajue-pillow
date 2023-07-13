import pywss
import time

millsecond=1500
deg_delay=1

def writeMillsecondsHandler(ctx:pywss.Context):
    global millsecond
    millsecond=int(ctx.route_params["mill"])
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
app.run(port=9600)