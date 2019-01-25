import dualnback.core as core
class Game():
    round_no = 1
    def __init__(self,user_id,start_n):
        self.user_id = user_id
        self.start_n = start_n
    @staticmethod
    def start_round():
        pressed_when_should=0
        pressed_when_should_not=0
        not_pressed_when_whould=0
        not_pressed_should_not=0
        audio_list=[]
        visual_list=[]
        carryon=True
        count=0
        while(carryon is True):
            audio=core.audio_generator()
            audio_list.append(audio)
            visual=core.visual_generator()
            visual_list.append(visual)

            print('Audio: '+str(audio))
            print('Visual: '+str(visual))
            print('Enter Visual(t/f): ')
            result_audio=core.check_visual(visual_list,bool(input()),2)
            print('Enter Audio(t/f): ')
            result_visual = core.check_visual(visual_list,bool(input()),2)
            if(result_audio==1 and result_visual==1):
                count+=1
            if count>=5:
                carryon=False


    def start_game(self,persist_n):
        if type(persist_n) is not bool:
            raise TabError('start_n should be True/False')
        if persist_n is True :
            pass
        else:
            pass


Game.start_round()

