#Boats and streams
"""A boat can travel with a speed of 13km/hr in still water
if the speed of the stream is 4km/hr,
find the time taken by the boat to go 68km downatream"""

#downstream=13+4=17 km/hr
#total time=68/17=4hrs



def boats(speed,speed_str,distance,stream):
    d_s=speed+speed_str
    u_s=speed-speed_str
    if stream=='d':
        total_time=distance/d_s
        return total_time
    elif stream=='u':
        total_time=distance/u_s
        return total_time 
print(boats(13,4,68,'d'))

def even(num):
    if num%2==0:
        return"even number"
    else:
        return "odd number"
print(even(48))
        

"""def boats(speed,stream_speed,distance,stream):
    d_s=speed+stream_speed
    u_s=speed-stream_speed    
    if stream=='d':
        return distance/d_s
    elif stream=='u':
        return distance/u_s
print(boats(13,4,68,'u'))   """ 
        
       