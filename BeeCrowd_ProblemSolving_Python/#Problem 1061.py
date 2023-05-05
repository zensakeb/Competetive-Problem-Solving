#Problem 1061
start_end_day = []
hour = []
minute = []
sec = []
for i in range(2):
    a = input().split()
    b = input().split(" : ")
    start_end_day.append(int(a[1]))
    hour.append(int(b[0]))
    minute.append(int(b[1]))
    sec.append(int(b[2]))
first_time = start_end_day[0]*24*3600 + hour[0]*3600 + minute[0]*60 + sec[0]
second_time = start_end_day[1]*24*3600 + hour[1]*3600 + minute[1]*60 + sec[1]

valid_time = second_time - first_time
remain = valid_time

d = int(valid_time/(24*3600))
remain = (valid_time/(24*3600)-d)*24
h = int(remain)
remain = (remain - h)*60
m = int(remain)
s = (remain - m)*60
if s>59:
    s = 0
    m += 1
    
print(f"{d} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{round(s)} segundo(s)")