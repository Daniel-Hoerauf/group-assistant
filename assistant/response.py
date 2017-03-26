"""
All of the individual methods that the assistant has
"""
import subprocess
import random

def answer(question):
    '''
    Will respond to any question with the best answer it can find
    '''
    ans = subprocess.Popen(['sirius.sh', question], stdout=subprocess.PIPE).stdout.read() 
    if(ans):
	    return ans
    else:
        return "No answers could be divined. Please try again"


def eight_ball(options):
    '''
    Given a list of quote enclosed options, will choose one
    '''
    choices = [ 'It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes, definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Signs point to yes',
                'Reply hazy try again',
                'Ask again later',
                'Better not to tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don\'t count on it',
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful'
                ]

    ans = random.choice(choices)
    return ans
