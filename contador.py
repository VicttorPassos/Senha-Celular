import time 
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = (f'{mins:02d}:{secs:02d}')
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Tente novamente') 
t = print('Aguarde 30 segundos para nova tentantiva') 
countdown(int(30))