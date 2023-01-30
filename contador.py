from time import sleep 
def regressiva(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = (f'{mins:02d}:{secs:02d}')
        print(timer, end="\r") 
        sleep(1) 
        t -= 1
    print('Tente novamente') 
t = print('Aguarde 30 segundos para nova tentantiva') 
regressiva(int(30))