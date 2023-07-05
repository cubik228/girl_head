import numpy as np

def yes_no(x):
    if (x<0.5):
        return 0
    else:
        return 1








def result( home,roc,attr):
    x = np.array([home,roc,attr])
    w1=[0.3,0.3,0]
    w2=[0.4,-0.5,1]

    sfere_1= np.array([w1,w2])
    sfere_2=np.array([-1,1])

    sum = np.dot(sfere_1,x)
    #print(sum)

    out = np.array([yes_no(x) for x  in sum])

    end = np.dot(sfere_2,out)
    v = yes_no(end)
    #print(v)
    return v

home = int(input("если у парня есть дом введите число 1 если нет то 0:\n"))

roc = int(input("парень любит рок то введите число 1 если нет то 0:\n"))

attr = int(input("если парень красивый  введите число 1 если нет то 0:\n"))



res_2 = result(home,roc,attr)
if res_2 == 0:
    print("гуляй")

else:
    print("ты мне нравишься")