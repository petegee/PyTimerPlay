
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