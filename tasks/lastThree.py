
from taskInterface import TaskInterface
from helpers import displayFlightTime
from helpers import secondsToMinutesAndSecondsOnly

class LastThree(TaskInterface):
    def getTaskName(self) -> str:
        return "Last 3 Flights"

    def showTimes(self, times):   
        total = len(times)
        if total > 2:
            print(f'3rd Last => {displayFlightTime(times[total-3])}')
        if total > 1:
            print(f'2nd Last => {displayFlightTime(times[total-2])}')
        if total > 0:
            print(f'Last     => {displayFlightTime(times[total-1])}')

    def getNextFlightTime(self, times) -> str:
        total = len(times)
        tasks = self.getTaskTargetTimes()
        return f"Next fligt max: {secondsToMinutesAndSecondsOnly(tasks[0])}"

    def getTaskTargetTimes(self) -> list[int]:
        return [200]

    def hasLastFlightMetTarget(self, time) -> bool:
        return True
        
    def isTaskComplete(self, times) -> bool:
        return False