import time
import keyboard
from dataclasses import dataclass

from helpers import displayFlightTime

from tasks.bestThree import BestThree
from tasks.ladder import Ladder
from tasks.lastThree import LastThree
from tasks.oneTwoThreeFour import OneTwoThreeFour

times = []
timing = False

@dataclass
class FlightTime:
    start: time
    stop: time


tasks = [
    BestThree(), 
    LastThree(),
    OneTwoThreeFour(), 
    Ladder()]

currentTask = 0


def startStopTimer():
    global timing
    if timing == True:
        stopTimer()
    else:
        startTimer()
        
def showAllTimes():
    global timing, tasks
    #if timing == True:
    #    return
    tasks[currentTask].showTimes(times)

def startTimer():
    global timing
    if tasks[currentTask].isTaskComplete(times):
        print("Task complete")
        return

    if timing == True:
        return
    else:
        print("start")
        timing = True
        currentFlight = FlightTime(time.time(), time.time())
        times.append(currentFlight)

def stopTimer():
    global timing
    if timing == False:
        return
    else:
        print("stop")
        currentFlight = times[len(times)-1]
        currentFlight.stop = time.time()
        timing = False
        task = tasks[currentTask]
        mostRecentFlightTime = currentFlight.stop - currentFlight.start
        if task.hasLastFlightMetTarget(mostRecentFlightTime):
            print(f"Valid flight: {displayFlightTime(currentFlight)}")
            print(f"{task.getNextFlightTime(times)}")
        else:
            print(f"Flight failed to meet target - {displayFlightTime(currentFlight)}")
            times.pop() # clear last flight

def changeTask():
    global currentTask
    stopTimer()
    showAllTimes()
    reset()
    currentTask = currentTask + 1
    if(currentTask >= len(tasks)):
        currentTask = 0

    print(f"Changed task to {tasks[currentTask].getTaskName()}")
    print(f"{tasks[currentTask].getNextFlightTime(times)}")

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

