import time
from taskInterface import TaskInterface
from helpers import displayFlightTime
from helpers import secondsToMinutesAndSecondsOnly

class BestThree(TaskInterface):
    def getTaskName(self) -> str:
        return "Best 3 Flights"

    def showTimes(self, times):   
        times.sort(key=lambda x: (x.stop - x.start), reverse=True)
        total = len(times)
        if total > 0:
            print(f'1st => {displayFlightTime(times[0])}')
        if total > 1:
            print(f'2nd => {displayFlightTime(times[1])}')
        if total > 2:
            print(f'3rd => {displayFlightTime(times[2])}')

    def getNextFlightTime(self, times) -> str:
        tasks = self.getTaskTargetTimes()
        return f"Next fligt max: {secondsToMinutesAndSecondsOnly(tasks[0])}"

    def getTaskTargetTimes(self) -> list[int]:
        return [200]

    def hasLastFlightMetTarget(self, time) -> bool:
        return True

    def isTaskComplete(self, times) -> bool:
        return False