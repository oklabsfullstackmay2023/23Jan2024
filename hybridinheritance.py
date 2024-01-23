#1 class defination is one time process
class GrandFather():
    #1. property/variable/state
    grandfathermobno=9617103148
    #2. constructor/esp.function
    #3. function/method
    pass
class Father(GrandFather):
    #1. property/variable/state
    fathermobno=7987811924
    #2. constructor//esp.function
    #3. function/method
    pass
class Vishal(Father):
    #1. property/variable/state
    #2. constrcutor/esp.function
    #3. function/method
    pass
class Preet(Father):
    #1. property/variable/state
    #2. constructor/esp.function
    #3. function/method
    pass

#2 create class external object is many time process
v1=Vishal()
print(f' Vishal says Grandfather mobile no. is {v1.grandfathermobno}')
print(f'Vishal says father mobile no. is {v1.fathermobno}')
p1=Preet
print(f'Preet says grandfather mobile no. is {p1.grandfathermobno}')
print(f'Preet says father mobile no. is {p1.fathermobno}')
