hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

time_hour = (hour + dura//60 + (mins+ dura%60)//60)%24
time_min = (mins+ dura%60)%60

print(time_hour,time_min,sep=":")
