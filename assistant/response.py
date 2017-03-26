"""
All of the individual methods that the assistant has
"""
import subprocess

def answer(question):
    '''
    Will respond to any question with the best answer it can find
    '''
    ans = subprocess.Popen(['sirius.sh', question], stdout=subprocess.PIPE).stdout.read() 
    if(ans):
	    return ans
    else:
        return "No answers could be divined. Please try again"
