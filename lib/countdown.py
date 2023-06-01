import time

def countdown(int):
    x = int
    while x >0:
        print(f'{x} SECOND(S)!')
        x-=1
    print("HAPPY NEW YEAR!")
    

def countdown_with_sleep(int):
    x = 10
    while x > 0:
        print(f'{x} SECOND(S)!')
        x-=1
        time.sleep(int)
    print("HAPPY NEW YEAR!")