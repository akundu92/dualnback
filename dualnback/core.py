from random import choice


def visual_generator():
    return choice((1, 2, 3, 4, 5, 6))


def audio_generator():
    t = tuple(i for i in range(1, 26))
    return choice(t)


def check_visual(seq,user_input=None,n=1):
    if seq[-1]==seq[-1-n] and user_input==True:
        return 1
    elif seq[-1]==seq[-1-n] and user_input==None:
        return 2
    elif seq[-1] != seq[-1 - n] and user_input is True:
        return 3
    elif seq[-1] != seq[-1 - n] and user_input is None:
        return 4



def check_audio(seq,user_input,n=1):
    pass
