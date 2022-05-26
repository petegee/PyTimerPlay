import time
from taskInterface import TaskInterface
from helpers import displayFlightTime
from helpers import secondsToMinutesAndSecondsOnly

class Ladder(TaskInterface):
    def getTaskName(self) -> str:
        return "Ladder"

    def showTimes(self, times):   
        total = len(times)
        i = 0
        for time in times:
            if i+1 >= len(self.getTaskTargetTimes()):
                continue

            print(f'{secondsToMinutesAndSecondsOnly(self.getTaskTargetTimes()[i])} => {displayFlightTime(time)}')
            i = i + 1

    def getNextFlightTime(self, times) -> str:
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
        
    def isTaskComplete(self, times) -> bool:
        total = len(times)
        if total >= len(self.getTaskTargetTimes()):
            return True
        else:
            return False