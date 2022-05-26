class TaskInterface:
    def getTaskName(self) -> str:
        """Show the task name"""
        pass

    def showTimes(self, times):
        """show the flight times in a task-relevant fashion"""
        pass

    def getNextFlightTime(self, times) -> str:
        """Get the next flight time"""
        pass

    def getTaskTargetTimes(self) -> list[int]:
        """Get the taks target flight times"""
        pass

    def hasLastFlightMetTarget(self, time) -> bool:
        """Has the flight met the target time of the flight"""
        pass

    def isTaskComplete(self, times) -> bool:
        """Is the task complete"""
        pass