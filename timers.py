import time
import keyboard
from dataclasses import dataclass

times = []
timing = False


@dataclass
class FlightTime:
    start: time
    stop: time

class TaskInterface:
    def getTaskName(self) -> str:
        """Show the task name"""
        pass

    def showTimes(self):
        """show the flight times in a task-relevant fashion"""
        pass

    def getNextFlightTime(self) -> str:
        """Get the next flight time"""
        pass


class BestThree(TaskInterface):
    def getTaskName(self) -> str:
        return "Best 3 Flights"

    def showTimes(self):   
        global times
        times.sort(key=lambda x: (x.stop - x.start), reverse=True)
        total = len(times)
        if total > 0:
            print(f'1st => {displayFlightTime(times[0])}')
        if total > 1:
            print(f'2nd => {displayFlightTime(times[1])}')
        if total > 2:
            print(f'3rd => {displayFlightTime(times[2])}')

    def getNextFlightTime(self) -> str:
        return "Max: 3:20"


class LastThree(TaskInterface):
    def getTaskName(self) -> str:
        return "Last 3 Flights"

    def showTimes(self):   
        global times
        total = len(times)
        if total > 2:
            print(f'3rd Last => {displayFlightTime(times[total-3])}')
        if total > 1:
            print(f'2nd Last => {displayFlightTime(times[total-2])}')
        if total > 0:
            print(f'Last     => {displayFlightTime(times[total-1])}')

    def getNextFlightTime(self) -> str:
        return "Max: 3:20"


class Ladder(TaskInterface):
    def getTaskName(self) -> str:
        return "Ladder"

    def showTimes(self):   
        global times
        total = len(times)
        if total > 6:
            print(f'2:00 => {displayFlightTime(times[total-1])}')
        if total > 5:
            print(f'1:45 => {displayFlightTime(times[total-2])}')
        if total > 4:
            print(f'1:30 => {displayFlightTime(times[total-3])}')
        if total > 3:
            print(f'1:15 => {displayFlightTime(times[total-4])}')
        if total > 2:
            print(f'1:00 => {displayFlightTime(times[total-5])}')
        if total > 1:
            print(f'0:45 => {displayFlightTime(times[total-6])}')
        if total > 0:
            print(f'0:30 => {displayFlightTime(times[total-7])}')

    def getNextFlightTime(self) -> str:
        global times
        total = len(times)
        if(total == 0):
            return "Target: 0:30"
        if(total == 1):
            return "Target: 0:45"
        if(total == 2):
            return "Target: 1:00"
        if(total == 3):
            return "Target: 1:15"
        if(total == 4):
            return "Target: 1:30"
        if(total == 5):
            return "Target: 1:45"
        if(total == 6):
            return "Target: 2:00"


tasks = [
    BestThree(), 
    LastThree(), 
    Ladder()]

currentTask = 0

def displayFlightTime(flightTime):
    sec = flightTime.stop - flightTime.start
    mins = sec // 60
    sec = sec % 60
    mins = mins % 60
    millisecs = int(sec * 1000)
    return f'{int(mins):02d}:{int(sec):02d}.{millisecs:<02d}'

def startStopTimer():
    global timing
    if timing == True:
        stopTimer()
    else:
        startTimer()
        
def showAllTimes():
    global timing, tasks
    if timing == True:
        return
    tasks[currentTask].showTimes()

def startTimer():
    global timing
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
        print(displayFlightTime(currentFlight))
        print(f"{tasks[currentTask].getNextFlightTime()}")

def changeTask():
    global currentTask
    stopTimer()
    showAllTimes()
    reset()
    currentTask = currentTask + 1
    if(currentTask >= len(tasks)):
        currentTask = 0

    print(f"Changed task to {tasks[currentTask].getTaskName()}")
    print(f"{tasks[currentTask].getNextFlightTime()}")

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

