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

    def getTaskTargetTimes(self) -> list[int]:
        """Get the taks target flight times"""
        pass

    def hasLastFlightMetTarget(self, time) -> bool:
        """Has the flight met the target time of the flight"""
        pass

    def isTaskComplete(self, time) -> bool:
        """Is the task complete"""
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
        tasks = self.getTaskTargetTimes()
        return f"Next fligt max: {secondsToMinutesAndSecondsOnly(tasks[0])}"

    def getTaskTargetTimes(self) -> list[int]:
        return [200]

    def hasLastFlightMetTarget(self, time) -> bool:
        return True

    def isTaskComplete(self, time) -> bool:
        return False

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
        global times
        total = len(times)
        tasks = self.getTaskTargetTimes()
        return f"Next fligt max: {secondsToMinutesAndSecondsOnly(tasks[0])}"

    def getTaskTargetTimes(self) -> list[int]:
        return [200]

    def hasLastFlightMetTarget(self, time) -> bool:
        return True
        
    def isTaskComplete(self, time) -> bool:
        return False


class Ladder(TaskInterface):
    def getTaskName(self) -> str:
        return "Ladder"

    def showTimes(self):   
        global times
        total = len(times)
        i = 0
        for time in times:
            if i+1 >= len(self.getTaskTargetTimes()):
                continue

            print(f'{secondsToMinutesAndSecondsOnly(self.getTaskTargetTimes()[i])} => {displayFlightTime(time)}')
            i = i + 1

    def getNextFlightTime(self) -> str:
        global times
        total = len(times)
        return f"Next flight target: {secondsToMinutesAndSecondsOnly(self.getTaskTargetTimes()[total-1])}"

    def getTaskTargetTimes(self) -> list[int]:
        return [30, 45, 60, 75, 90, 105, 120]

    def hasLastFlightMetTarget(self, time) -> bool:
        global times      
        taskTargetTime = self.getTaskTargetTimes()[len(times)-1]
        if(time > taskTargetTime):
            return True
        else:
            return False
        
    def isTaskComplete(self) -> bool:
        global times
        total = len(times)
        if total >= len(self.getTaskTargetTimes()):
            return True
        else:
            return False


class OneTwoThreeFour(TaskInterface):

    targets = { "240": False, "180": False, "120": False, "60": False }

    def getTaskName(self) -> str:
        return "1, 2, 3, 4"

    def showTimes(self):   
        global times
        times.sort(key=lambda x: (x.stop - x.start), reverse=True)
        total = len(times)
        if total > 0:
            print(f'4min => {displayFlightTime(times[0])}')
        if total > 1:
            print(f'3min => {displayFlightTime(times[1])}')
        if total > 2:
            print(f'2min => {displayFlightTime(times[2])}')
        if total > 3:
            print(f'1min => {displayFlightTime(times[3])}')

    def getNextFlightTime(self) -> str:
        res = { key:val for key, val in self.targets.items() if val == False }
        print(res)

    def getTaskTargetTimes(self) -> list[int]:
        return [1,2]
        #return [30, 45, 60, 75, 90, 105, 120]

    def hasLastFlightMetTarget(self, time) -> bool:
        if time >=240:
            self.targets["240"] = True
        elif time >=180:
            self.targets["180"] = True
        elif time >=120:
            self.targets["120"] = True
        elif time >=60:
            self.targets["60"] = True

        return True
     
    def isTaskComplete(self) -> bool:
        res = all(t is True for t in self.targets)


tasks = [
    BestThree(), 
    LastThree(),
    OneTwoThreeFour(), 
    Ladder()]

currentTask = 0

def secondsToMinutesAndSecondsOnly(sec):
    mins = sec // 60
    sec = sec % 60
    mins = mins % 60
    millisecs = int(sec * 1000)
    return f'{int(mins):02d}:{int(sec):02d}'

def displayFlightTime(flightTime):
    sec= flightTime.stop - flightTime.start
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
    if tasks[currentTask].isTaskComplete():
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
            print(f"{task.getNextFlightTime()}")
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

