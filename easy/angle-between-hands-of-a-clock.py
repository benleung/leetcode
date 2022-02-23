'''
revised on 2/23, but nothing special
'''

'''
heard twitter that someone failed this
probably because of pressure only


'''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        ANGLE_FOR_EACH_HOUR = 360/12
        ANGLE_FOR_EACH_MINUTE = 360/60

        hourAngle = ANGLE_FOR_EACH_HOUR*(hour if hour != 12 else 0) + (minutes/60.0)*ANGLE_FOR_EACH_HOUR

        minuteAngle = ANGLE_FOR_EACH_MINUTE*minutes
        
        difference = abs(hourAngle-minuteAngle)
        return difference if difference <=180 else 360-difference
