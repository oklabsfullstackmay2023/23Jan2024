#1 class defination is one time process
class Student():
    #1. property/variable/state
    hindi=0
    english=0
    science=0
    maths=0
    social=0
    percentage=0.0
    #2. constructor/esp.function
    def __init__(self,english,social,science,maths,hindi):
        #the role of constructor is initialize the value
        self.hindi=hindi
        self.english=english
        self.science=science
        self.social=social
        self.maths=maths
        self.percentage=(self.hindi+self.social+self.english+self.science+self.maths)/5
        pass
    #3. method/function/behaviour
    def getPercentage(self):
        print(f'{self.percentage}')
        pass
    pass
#2 create class external object is many time process
#ceo1=ClassName()
vishal=Student(hindi=70,english=80,maths=90,science=60,social=50)
vishal.getPercentage()

anjali=Student(hindi=70,english=50,maths=90,science=80,social=85)
anjali.getPercentage()