from random import choice


def visual_generator():
    return choice((1, 2, 3, 4, 5, 6))


def audio_generator():
    t = tuple(i for i in range(1, 26))
    return choice(t)


def check_visual(seq,user_input=False,n=1):
    if type(seq) is not list:
        raise TypeError('Type should be List not '+str(type(seq)))
    if type(user_input) is not bool:
        raise TypeError('user_input should be of type bool')
    if type(n) is not int or n<=0 :
        raise ValueError('N can not be negative or non integer')
    if(n<=(len(seq)-1)):
        if seq[-1]==seq[-1-n] and user_input==True:
            return 1
        elif seq[-1]==seq[-1-n] and user_input is False:
            return 2
        elif seq[-1] != seq[-1 - n] and user_input is True:
            return 3
        elif seq[-1] != seq[-1 - n] and user_input is False:
            return 4
    elif(user_input is True):
        return 3
    else:
        return 4



def check_audio(seq,user_input,n=1):
    pass
