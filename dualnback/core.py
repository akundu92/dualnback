from random import choice


def visual_generator():
    return choice((1, 2, 3, 4, 5, 6))


def audio_generator():
    t = tuple(i for i in range(1, 26))

    return choice(t)


def check_visual(seq,user_input,n=1):
    pass


def check_audio(seq,user_input,n=1):
    pass
