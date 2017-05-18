def personality():
    print('    I\'m great thanks!')

def thanks():
    print('    It\'s all good')

def okay():
    print('    Okay man whatever you want.')

def curse_words():
    print('''    Look, I can see you\'re really upset about this.
    I honestly think you ought to sit down calmly, take a
    stress pill, and think things over.''')


commands = [('how are you', personality),
            ('whats up', personality),
            ('how you doin', personality),
            ('shit', curse_words),
            ('fuck', curse_words),
            ('nevermind', okay),
            ('thanks', thanks),
            ('thank', thanks),]

help_options = []
