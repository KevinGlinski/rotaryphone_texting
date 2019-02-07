import pigpio
import time



count = 0

def cbf(g, L, t):
    global count
    count += 1
    message = "{} gpio={} level={} at {}".format(count, g, L, t)
    print(message)
    
#pigpio.start()
#cb = pigpio.callback(15, pigpio.EITHER_EDGE, cbf)
#time.sleep(30)
#cb.cancel()
#pigpio.stop()

HOOK_PIN= 14

pi = pigpio.pi()
pi.set_mode(HOOK_PIN, pigpio.INPUT)
pi.set_pull_up_down(HOOK_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(HOOK_PIN, 10000)
print(pi.read(HOOK_PIN))
pi.callback(HOOK_PIN, pigpio.EITHER_EDGE, cbf)

input("")
pigpio.stop()
