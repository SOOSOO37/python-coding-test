import sys
result = 0
for i in range(5):
    start, end = sys.stdin.readline().split(" ")
    start_time, start_minute = start.split(":")
    end_time, end_minute = end.split(":")
    start_time, start_minute, end_time, end_minute = int(start_time), int(start_minute), int(end_time),int(end_minute)

    if end_minute >= start_minute:
        result += (end_time - start_time) * 60 + end_minute - start_minute
    else:
        result += (end_time - start_time - 1) * 60 + end_minute + 60 - start_minute

print(result)
