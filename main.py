#put your sprinkler slightly above the center in strawberry field.
#make sure you're looking straight down with the 15 bee zone at the top of your screen.
#graphics quality must be set to 1 for precise targets to be recognised (since they glow)
#the server should not be "snowing" (happens after mms/honeystorm and resets after night) as it will not recognise some things.
#run the script then press o+p while on roblox to start it.

import time
import pyautogui
from PIL import Image, ImageDraw, ImageGrab
import mss
import pynput
import time
from multiprocessing import Process
pyautogui.FAILSAFE = False

cycle = 15
keyx = ''
keyy = ''
field = "strawberry" #or pepper, but dont use pepper just do
with mss.mss() as sct:
    monitor = sct.monitors[1]
    sct_img = sct.grab(monitor)
    im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
width,height = im.size
midx = width/2
midy = height/2
freq = round(width/170)
print(midx,midy)
print(freq)
ratio = 1
floorcolor = ()
scorchtime = 0
run = False
alwaysgetprecision = False

glitterslot = 7
extractslot = 2
diceslot = 4

#boosting
doboost = False
lastextract = time.time()-600
glitter = True # not toggleable do not touch
keys = pynput.keyboard.Controller()
def swap(): 
    global run 
    run = not(run)
    global lastseensaturator
    lastseensaturator = time.time()
    keys.release('w')
    keys.release('a')
    keys.release('s')
    keys.release('d')
listener = pynput.keyboard.GlobalHotKeys({'o+p': swap})
listener.start()
hastereset = time.time()
haste = 1
def gethaste():
    global haste
    global hastereset
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    width,height=im.size
    for x in range (width):
        if x % 76 == 0:
            (r,g,b) =  im.getpixel((x-1,147))
            if (r,g,b) == (240,240,240):
                temphaste = haste
                if im.getpixel((x-30,130)) == (113, 114, 116):
                    haste = 1.1
                if im.getpixel((x-6,140)) == (192,192,192):
                    haste = 1.2
                elif im.getpixel((x-11,133)) == (172,172,172):
                    haste = 1.3
                elif im.getpixel((x-15,128)) == (130,130,130):
                    haste = 1.4
                elif im.getpixel((x-16,121)) == (102, 102, 102):
                    haste = 1.5
                elif im.getpixel((x-14,124)) == (142,142,142):
                    haste = 1.6
                elif im.getpixel((x-12,130)) == (243,243,243):
                    haste = 1.7
                elif im.getpixel((x-21,120)) == (45, 45, 45):
                    haste = 1.8
                elif im.getpixel((x-15,139)) == (166,166,166):
                    haste = 1.9
                elif im.getpixel((x-26,140)) == (155,155,155):
                    haste = 2.0
                if haste > temphaste:
                    hastereset = time.time()+20
                elif haste == temphaste:
                    hastereset = time.time()+2
                if hastereset < time.time():
                    haste = 1
    return haste
def keypress(delay,key,key2='none',key3='none'):
    if delay > 0:
        keys.press(key)
        if key2 != 'none': keys.press(key2)
        if key3 != 'none': keys.press(key3)
        time.sleep(delay)
        if key2 != 'none': keys.release(key2)
        if key3 != 'none': keys.release(key3)
        keys.release(key)
    else:
        pyautogui.press(key)
def goto(location):
    if location == 'hivetocannon':
        color = (0,0,0)
        while color != (238, 238, 242):
            keypress(1,'w') # cannon
            keypress(5/gethaste(),'d')
            keypress(0.03,'s')
            keypress(0.3,pynput.keyboard.Key.space)
            keypress(0.1,'d')
            time.sleep(0.5)
            keypress(0.5,'d')
            keypress(0.15,pynput.keyboard.Key.space)
            keypress(0.6,'d')
            time.sleep(0.5)
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)
                im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            color = im.getpixel((1100,80))
            if color == (238, 238, 242):
                pyautogui.click(700,70)
            else:
                reset()
    if location == 'cannontostrawberry':
        time.sleep(0.72)
        keypress(0,'space')
        keypress(0,'space')
        keypress(2.1,'d')
        keypress(0,'space')
        time.sleep(2)
        for i in range(4):
            keypress(0,'.')
            keypress(0,'pageup')
            keypress(0,'o')
            time.sleep(0.2)
        keypress(0,'o')
        keypress(1/gethaste(),'w','d')
        keypress(4/gethaste(),'w')
        keypress(2/gethaste(),'a')
        keypress(1.3/gethaste(),'d')
        keypress(0.7/gethaste(),'s')
        pyautogui.click(500,828)
        time.sleep(0.3)
        pyautogui.click(750,400)
    if location == 'cannontoclock':
        time.sleep(1.3)
        keypress(0,'space')
        keypress(0,'space')
        keypress(10,'a','w')
        keypress(4/gethaste(),'s')
        for i in range(5):
            keypress(0.15,'d')
            pyautogui.click(700,70)
        for i in range(10):
            time.sleep(0.15)
            pyautogui.click(700,700)
        

def reset():
    color = (0,0,0)
    color2 = (0,0,0)
    while not(color2 == (249, 255, 249)):
        keypress(0,'escape')
        time.sleep(0.5)
        keypress(0,'r')
        time.sleep(0.5)
        keypress(0,'return')
        time.sleep(8)
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        color = im.getpixel((1100,80))
        color2 = im.getpixel((1200,104))
        if color == (238, 238, 242):
            pyautogui.click(700,70)
        while color == (238, 238, 242):
            time.sleep(0.1)
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)
                im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            color = im.getpixel((1100,80))
            color2 = im.getpixel((1200,104))
while run == False:
    time.sleep(0.1)

wealthclock = time.time()
floorcolor = ()
if field == "pepper": floorcolor = (26, 55, 19)
if field == "strawberry": floorcolor = (250, 228, 101)
z = 0
saturatorx = 0
saturatory = 0
closestx = 9999
closesty = 9999
c = 0
dontmove = False
lastseensaturator = time.time()
def scan(width,y):
    for x in range(width):
        if x % freq == 0:
            r,g,b = im.getpixel((x,y))
            global z
            global c
            global getprecision
            global saturatory
            global saturatorx
            global lastseensaturator
            global giftedhive
            global dontmove
            global closestx
            global closesty
            if not((r,g,b) == floorcolor):# and not(r>240 and g>240 and b>240):
                colors = [(98, 213, 251),(99, 214, 251),(102, 213, 251),(107, 217, 251)]
                if (r,g,b) in colors: #saturator
                    z = 0
                    (saturatorx,saturatory) = (x,y)
                    lastseensaturator = time.time()
                if not(dontmove):
                    colors = [(192, 108, 247),(192, 114, 247),(194, 112, 247)]
                    if (r,g,b) in colors: # precise
                        targets.append((x, y))
                    elif ((r,g,b) == (247, 207, 122) or (r,g,b) == (247, 208, 119) or (r,g,b) == (247, 209, 119)): # normal
                        targets.append((x, y))
                    elif ((r,g,b) == (117, 251, 76) or (r,g,b) == (120, 251, 85) or (r,g,b) == (118, 251, 76)) and (not(scorching) or backpackfull): # activated
                        if not(getprecision):
                            z = 80
                            dontmove = True
                            closestx = x
                            closesty = y
                    elif (r,g,b) == (0,0,0) and not(x > 2000) and not(x < 1554 and x > 1410 and y < 914 and y > 816):
                        smileys.append((x,y))
                else:
                    if (r,g,b) == (117, 251, 76):
                        if (abs(detectx-x)**2 + abs(detecty-y)**2)**0.5 < (abs(detectx-closestx)**2 + abs(detecty-closesty)**2)**0.5:
                            closestx = x
                            closesty = y
                if not(x > 2000 and y < 480):
                    if r >= 254 and g > 251 and b < 100 and b > 80: #normal flames
                        flames.append((x,y))
                    # if r >= 195 and g >= 52 and b >= 43 and r <= 236 and b <= 98 and b <= 123: #dark flames
                    #     flames.append((x,y))
            else:
                if (x < midx and y < midy):
                    if im.getpixel((x-freq, y)) == floorcolor: c = c + 1
                    if im.getpixel((x-freq, y-freq)) == floorcolor: c = c + 1
                    if im.getpixel((x, y-freq)) == floorcolor: c = c + 1
while True:
    if run:
        if time.time()-wealthclock < 3600:
            tick=time.time()
            detectx = 1440
            detecty = 880
            if keyx == 'a':
                detectx = 1440-200
            if keyx == 'd':
                detectx = 1440+200
            if keyx == 'w':
                detecty = 880-200
            if keyx == 's':
                detecty = 880+200 # move center of detection to prevent it getting confused
            detectx = 1440
            detecty = 880
            pynput.mouse.Controller().press(pynput.mouse.Button.left)
            closestx = 9999
            closesty = 9999
            saturatorx = 9999
            saturatory = 9999
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)
                im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            targets = []
            tokens = []
            smileys = []
            flames = []
            type = ""
            z = 0
            haste = gethaste()
            c = 0
            width, height = im.size
            tracking = False
            dodge = False
            scorching = False
            backpackfull = False
            heat = True
            getprecision = True
            dontmove = False
            boost = True #boosting
            for x in range (width):
                if x % 76 == 0:
                    (r,g,b) = im.getpixel((x-38,108))
                    if r >= 216 and r <= 220 and g >= 69 and g <= 73 and b >= 35 and b <= 40:
                        scorching = True
                        scorchtime = time.time()
                    (r,g,b) = im.getpixel((x-5,108))
                    if (r,g,b) == (134, 81, 175):
                        if im.getpixel((x-45,99)) == (133, 81, 174):
                            getprecision = False
                    if (r,g,b) == (213, 54, 34):
                        heat = False
                    if doboost:
                        (r,g,b) = im.getpixel((x-2,137))
                        (r2,g2,b2) = im.getpixel((x-44,137))
                        if (r >= 180 and r <= 225 and g >= 165 and g <= 210 and b >= 70 and b <= 115) and (r2,g2,b2) != (172, 138, 61):
                            if (r2-25>g2 and g2>b2):
                                boost = False
                                if not(glitter):
                                    glitter = True
            if alwaysgetprecision or scorching:
                getprecision = True
            if time.time()-scorchtime <= 15: # once ya scorch ya scorch for the next 15s
                scorching = True
            if boost and doboost:
                if glitter:
                    pyautogui.keyDown(str(glitterslot))
                    time.sleep(0.08)
                    pyautogui.keyUp(str(glitterslot))
                    glitter = False
                    time.sleep(1)
                else:
                    pyautogui.keyDown(str(diceslot))
                    time.sleep(0.08)
                    pyautogui.keyUp(str(diceslot))
                if (time.time()-lastextract) >600:
                    lastextract = time.time()
                    pyautogui.keyDown(str(extractslot))
                    time.sleep(0.08)
                    pyautogui.keyUp(str(extractslot))
            tick = time.time()
            for y in range(height):
                if y % freq == 0:
                    t = Process(target=scan, args=(width,y))
                    t.run()
            if c >= 1 and len(targets) == 0:
                keys.press('a')
                keys.press('w')
                time.sleep(0.1)
                keys.release('a')
                keys.release('w')    
            c = 0
            blocked = []
            actualtargets = []
            keys.release('w')
            keys.release('a')
            keys.release('s')
            keys.release('d')
            if not(dontmove):
                if len(flames) == 0:
                    heat = False
                if not(heat) and len(targets) > 0:
                    for (x,y) in targets:
                        z=100
                        ignore = 0
                        c = 0
                        try:
                            if (x+freq, y) in targets: 
                                c = c + 1 
                            if (x-freq, y) in targets: 
                                c = c + 1
                            if (x, y+freq) in targets: 
                                c = c + 1
                            if (x, y-freq) in targets: 
                                c = c + 1
                        except: pass
                        if (abs(detectx-x)**2 + abs(detecty-y)**2)**0.5 < (abs(detectx-closestx)**2 + abs(detecty-closesty)**2)**0.5 and c>0:
                            if not(x < midx+z and x > 1400-z and y < midy+z and y > midy-x) and (abs(midx-x)**2+abs(midy-y)**2)**0.5 > ignore:
                                closestx = x
                                closesty = y
                                tracking = True
                elif len(flames) > 0 and scorching and heat:
                    for (x,y) in flames:
                        z = 250
                        c = 0
                        try:
                            if (x+freq, y) in flames: 
                                c = c + 1 
                                if im.getpixel((x+2*freq, y)) == floorcolor: c = -1000
                            if (x-freq, y) in flames: 
                                c = c + 1
                                if im.getpixel((x-2*freq, y)) == floorcolor: c = -1000
                            if (x, y+freq) in flames: 
                                c = c + 1
                                if im.getpixel((x, y+2*freq)) == floorcolor: c = -1000
                            if (x, y-freq) in flames: 
                                c = c + 1
                                if im.getpixel((x, y-2*freq)) == floorcolor: c = -1000
                        except:pass
                        if c > 0:
                            if (abs(detectx-x)**2 + abs(detecty-y)**2)**0.5 < (abs(detectx-closestx)**2 + abs(detecty-closesty)**2)**0.5:
                                closestx = x
                                closesty = y
                                tracking = True
                elif len(smileys) > 0:
                    for (x,y) in smileys:
                        z = 100
                        type = "smiley"
                        c = 0
                        if (abs(detectx-x)**2 + abs(detecty-y)**2)**0.5 < (abs(detectx-closestx)**2 + abs(detecty-closesty)**2)**0.5:
                            closestx = x
                            closesty = y
                            tracking = True

                if tracking:
                    cycle = 15
                if tracking == False:
                    if saturatorx != 9999 and cycle >= 15:
                        tracking = True
                        closestx = saturatorx
                        closesty = saturatory
                        tz = 250
                        if closestx <= midx+tz and closestx >= midx-tz and closesty <= midy+tz and closesty >= midy-tz: #midx is mid
                            cycle = 0
                            tracking = False
                    else:
                        if time.time()-lastseensaturator > 100:
                            keys.press('s')
                            keys.press('d')
                            time.sleep(7)
                            keys.release('s')
                            time.sleep(3)
                            keys.release('d')
                            keys.press('w')
                            keys.press('a')
                            keys.press(pynput.keyboard.Key.space)
                            time.sleep(12)
                            keys.release('w')
                            keys.release('a')
                            keys.release(pynput.keyboard.Key.space)
                        elif time.time()-lastseensaturator > 60:
                            keys.press('w')
                            keys.press('a')
                            keys.press(pynput.keyboard.Key.space)
                            time.sleep(8)
                            keys.release('w')
                            keys.release('a')
                            keys.release(pynput.keyboard.Key.space)
                keys.release('w')
                keys.release('a')
                keys.release('s')
                keys.release('d')
                if not(tracking):
                    cycle = cycle + 1
                    if cycle <= 3:
                        keys.press('a')
                        time.sleep(0.2)
                        keys.release('a')
                    elif cycle == 4 or cycle == 8 or cycle == 12:
                        keys.press('s')
                        time.sleep(0.6)
                        keys.release('s')
                    elif cycle == 5 or cycle == 7 or cycle == 9 or cycle == 11 or cycle == 13:
                        keys.press('d')
                        time.sleep(0.12)
                        keys.release('d')
                    elif cycle == 6 or cycle == 10 or cycle == 14:
                        keys.press('w')
                        time.sleep(0.6)
                        keys.release('w')
                    else:
                        keys.press('w')
                        keys.press('a')
                        time.sleep(0.1)
                        keys.release('w')
                        keys.release('a')
            xdistance = 0
            ydistance = 0
            if dontmove or tracking:
                keyx = ''
                keyy = ''
                if closestx <= midx+z and closestx >= midx-z and closesty <= midy+z and closesty >= midy-z:
                    cycle = 0
                else:
                    if closestx != 9999:
                        if closestx > midx+z: #midx is mid
                            keyx = 'd'
                        elif closestx < midx-z:
                            keyx = 'a'
                    if closesty != 9999:
                        if closesty > midy+z: #midy is mid
                            keyy = 's'
                        elif closesty < midy-z:
                            keyy = 'w'
                if type == "smiley" and (abs(closestx-midx)**2 + abs(closesty-midy)**2)**0.5 < 200:
                    time.sleep(0.1)
                if keyx != '': keys.press(keyx)
                if keyy != '': keys.press(keyy)
                # if abs(closestx-midx)+abs(closesty-midy) < 300:
                #     time.sleep(0.3)
                #     keys.release('w')
                #     keys.release('a')
                #     keys.release('s')
                #     keys.release('d')

                
        else:
            reset()
            goto('hivetocannon')
            goto('cannontoclock')
            reset()
            goto('hivetocannon')
            goto('cannontostrawberry')
            wealthclock = time.time()
