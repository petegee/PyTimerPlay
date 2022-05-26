import time
from taskInterface import TaskInterface
from helpers import displayFlightTime

class OneTwoThreeFour(TaskInterface):

    targets = { "240": False, "180": False, "120": False, "60": False }

    def getTaskName(self) -> str:
        return "1, 2, 3, 4"

    def showTimes(self, times):   
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

    def getNextFlightTime(self, times) -> str:
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
     
    def isTaskComplete(self, times) -> bool:
        res = all(t is True for t in self.targets)