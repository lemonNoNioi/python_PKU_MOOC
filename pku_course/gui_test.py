import easygui as g
import sys
while 1:
    g.msgbox('Hello!')
    msg = 'What do you want?'
    title = 'Game'
    choices = ['coffee', 'milk', 'water', 'cola']
    choice = g.choicebox(msg, title, choices)
    g.msgbox('Your choice is: '+str(choice), 'Result')
    msg = 'Do you want to play again?'
    title = 'Please make choice.'
    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)