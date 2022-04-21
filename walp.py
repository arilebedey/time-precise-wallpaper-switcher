import datetime
import time
import os

def todayAt(hr, min, sec=0, micros=0):
    now = datetime.datetime.now()
    return(now.replace(hour=hr, minute=min, second=sec, microsecond=micros))

def timeNow():
    now = datetime.datetime.now()
    return(now.replace(second=0, microsecond=0))

# Had some fun & a good Vim practice
deepnight = [lambda: todayAt(1, 41), lambda: todayAt(5, 10), "/home/ari/Images/Wallpapers/energy-aurora.jpg"]
dawn  = [lambda: todayAt(5, 11), lambda: todayAt(5, 59), "/home/ari/Images/Wallpapers/river-china-landscape.jpg"]
earlymorning = [lambda: todayAt(6, 0), lambda: todayAt(7, 12), "/home/ari/Images/Wallpapers/altai-mountains-lake-scenic-reflection-clouds-dark-gloomy-fog.jpeg"]
morning = [lambda: todayAt(7, 13), lambda: todayAt(8, 42), "/home/ari/Images/Wallpapers/altai-republic.jpg"]
middlemorning = [lambda: todayAt(8, 43), lambda: todayAt(10, 7), "/home/ari/Images/Wallpapers/justrees.jpg"]
latemorning = [lambda: todayAt(10, 8), lambda: todayAt(10, 35), "/home/ari/Images/Wallpapers/cool-sunny-ice-antartica.jpg"]
latermorning = [lambda: todayAt(10, 36), lambda: todayAt(11, 27), "/home/ari/Images/Wallpapers/russia-summer-paysage.jpg"]
noon = [lambda: todayAt(11, 28), lambda: todayAt(13, 39), "/home/ari/Images/Wallpapers/birch-trail.jpg"]
latenoon = [lambda: todayAt(13, 40), lambda: todayAt(14, 17), "/home/ari/Images/Wallpapers/altai-mountains-valley-hills-river-landscape-19372.jpg"]
afternoon = [lambda: todayAt(14, 18), lambda: todayAt(15, 10), "/home/ari/Images/Wallpapers/mountain-full-of-pines.jpg"]
earlyevening = [lambda: todayAt(15, 11), lambda: todayAt(17, 0), "/home/ari/Images/Wallpapers/spring-in-antarctica.jpg"]
evening = [lambda: todayAt(17, 1), lambda: todayAt(17, 25), "/home/ari/Images/Wallpapers/a-la-moon-base.jpg"]
lateevening = [lambda: todayAt(17, 26), lambda: todayAt(19, 15), "/home/ari/Images/Wallpapers/mountain-aurora.jpg"]
dusk = [lambda: todayAt(19, 16), lambda: todayAt(20, 55), "/home/ari/Images/Wallpapers/sunsethorizon.jpg"]
night = [lambda: todayAt(20, 56), lambda: todayAt(21, 58), "/home/ari/Images/Wallpapers/iss-aurora.jpg"]
latenight = [lambda: todayAt(21, 59), lambda: todayAt(23, 59, 59), "/home/ari/Images/Wallpapers/late-night-aurora.jpg"]
latenight2 = [lambda: todayAt(0, 0), lambda: todayAt(1, 41, 59), "/home/ari/Images/Wallpapers/late-night-aurora.jpg"]

now = timeNow()
if deepnight[0]() < now < deepnight[1]():
    os.system("xwallpaper --zoom " + deepnight[2])
if dawn[0]() < now < dawn[1]():
    os.system("xwallpaper --zoom " + dawn[2])
if earlymorning[0]() < now < earlymorning[1]():
    os.system("xwallpaper --zoom " + earlymorning[2])
if morning[0]() < now < morning[1]():
    os.system("xwallpaper --zoom " + morning[2])
if middlemorning[0]() < now < middlemorning[1]():
    os.system("xwallpaper --zoom " + middlemorning[2])
if latemorning[0]() < now < latemorning[1]():
    os.system("xwallpaper --zoom " + latemorning[2])
if latermorning[0]() < now < latermorning[1]():
    os.system("xwallpaper --zoom " + latermorning[2])
if noon[0]() < now < noon[1]():
    os.system("xwallpaper --zoom " + noon[2])
if latenoon[0]() < now < latenoon[1]():
    os.system("xwallpaper --zoom " + latenoon[2])
if afternoon[0]() < now < afternoon[1]():
    os.system("xwallpaper --zoom " + afternoon[2])
if earlyevening[0]() < now < earlyevening[1]():
    os.system("xwallpaper --zoom " + earlyevening[2])
if evening[0]() < now < evening[1]():
    os.system("xwallpaper --zoom " + evening[2])
if lateevening[0]() < now < lateevening[1]():
    os.system("xwallpaper --zoom " + lateevening[2])
if dusk[0]() < now < dusk[1]():
    os.system("xwallpaper --zoom " + dusk[2])
if night[0]() < now < night[1]():
    os.system("xwallpaper --zoom " + night[2])
if latenight[0]() < now < latenight[1]():
    os.system("xwallpaper --zoom " + latenight[2])
    print("Success yes")
if latenight2[0]() < now < latenight2[1]():
    os.system("xwallpaper --zoom " + latenight2[2])
    print("Success")

while True:
    now = timeNow()
    time.sleep(15)
    # print(now)
    if deepnight[0]() < now < deepnight[1]():
        os.system("xwallpaper --zoom " + deepnight[2])
        continue
    if dawn[0]() < now < dawn[1]():
        os.system("xwallpaper --zoom " + dawn[2])
        continue
    if earlymorning[0]() < now < earlymorning[1]():
        os.system("xwallpaper --zoom " + earlymorning[2])
        continue
    if morning[0]() < now < morning[1]():
        os.system("xwallpaper --zoom " + morning[2])
        continue
    if middlemorning[0]() < now < middlemorning[1]():
        os.system("xwallpaper --zoom " + middlemorning[2])
        continue
    if latemorning[0]() < now < latemorning[1]():
        os.system("xwallpaper --zoom " + latemorning[2])
        continue
    if latermorning[0]() < now < latermorning[1]():
        os.system("xwallpaper --zoom " + latermorning[2])
        continue
    if noon[0]() < now < noon[1]():
        os.system("xwallpaper --zoom " + noon[2])
        continue
    if latenoon[0]() < now < latenoon[1]():
        os.system("xwallpaper --zoom " + latenoon[2])
        continue
    if afternoon[0]() < now < afternoon[1]():
        os.system("xwallpaper --zoom " + afternoon[2])
        continue
    if earlyevening[0]() < now < earlyevening[1]():
        os.system("xwallpaper --zoom " + earlyevening[2])
        continue
    if evening[0]() < now < evening[1]():
        os.system("xwallpaper --zoom " + evening[2])
        continue
    if lateevening[0]() < now < lateevening[1]():
        os.system("xwallpaper --zoom " + lateevening[2])
        continue
    if dusk[0]() < now < dusk[1]():
        os.system("xwallpaper --zoom " + dusk[2])
        continue
    if night[0]() < now < night[1]():
        os.system("xwallpaper --zoom " + night[2])
        continue
    if latenight[0]() < now < latenight[1]():
        os.system("xwallpaper --zoom " + latenight[2])
        print("Success")
        continue
    if latenight2[0]() < now < latenight2[1]():
        os.system("xwallpaper --zoom " + latenight2[2])
        print("Success")
        continue
    else:
        print("nope.>>>")
        continue
