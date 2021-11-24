import time
import keyboard
from dataclasses import dataclass

@dataclass
class FlightTime:
    start: time
    stop: time

times = []
timing = False

currentTask = 0
tasks = ["Task1", "Task2"]

def displayFlightTime(flightTime):
    sec = flightTime.stop - flightTime.start
    mins = sec // 60
    sec = sec % 60
    mins = mins % 60
    millisecs = int(sec * 1000)
    return f'{int(mins):02d}:{int(sec):02d}.{millisecs:<02d}'

def startStopTimer():
    global timing
    if timing is True:
        stopTimer()
    else:
        startTimer()
        
def showAllTimes():
    global timing
    if timing is True:
        return
    for (i,t) in enumerate(times):
        print(f'Flight {i+1} => {displayFlightTime(t)}')

def startTimer():
    global timing
    if timing is True:
        return
    else:
        print("start")
        timing = True
        currentFlight = FlightTime(time.time(), time.time())
        times.append(currentFlight)

def stopTimer():
    global timing
    if timing is False:
        return
    else:
        print("stop")
        currentFlight = times[len(times)-1]
        currentFlight.stop = time.time()
        timing = False
        print(displayFlightTime(currentFlight))

def changeTask():
    stopTimer()
    showAllTimes()
    reset()
    for count, value in enumerate(tasks):     
        print(count, value)

    print("Change Task")

def reset():
    global times, timing
    times = []
    timing = False
    print("Reset")

while True:
    if keyboard.is_pressed('q'):
        reset()
        time.sleep(0.5)
        continue
    if keyboard.is_pressed('a'):
        changeTask()
        time.sleep(0.5)
        continue
    if keyboard.is_pressed('w'):
        startStopTimer()
        time.sleep(0.5)
        continue
    if keyboard.is_pressed('s'):
        showAllTimes()
        time.sleep(0.5)
        continue

