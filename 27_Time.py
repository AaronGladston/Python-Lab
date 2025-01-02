class Time:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self,other):
        sec = self.__second + other.__second
        minu = self.__minute + other.__minute
        hr = (self.__hour + other.__hour)%24
        if(sec>60):
            sec%=60
            minu+=1
        if(minu>60):
            minu%=60
            hr+=1
        return(hr,minu,sec)
    
    def __str__(self):
        f"The resultant time is given as\nTime = {self.hr}:{self.minu}:{self.sec}"

t1 = Time(13,41,49)
t2 = Time(21,58,29)
t = t1 + t2
print(t)


    
