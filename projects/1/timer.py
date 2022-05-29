# импорт библиотеки "time"
import time

hours = 0
minutes = 0
seconds = 0

# код до цикла
while True:
    # seconds = seconds + 1
    seconds += 1

    if seconds > 59:
        minutes += 1
        seconds = 0

    if minutes > 59:
        hours += 1
        minutes = 0

    if hours > 23:
        seconds = 0
        minutes = 0
        hours = 0

    time.sleep(secs=0.00001)
    print(f"{hours}:{minutes}" + ":" + str(seconds))
# код после цикла
