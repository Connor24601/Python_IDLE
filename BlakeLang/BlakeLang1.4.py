
version = '1.4'
version_functionality=""" This version contains functional Python."""
version_goal="""This version will have awesome tutorials! \nRecursion now functions."""



import sys
import time
import math



#WELCOME TO BLAKELANG CODEBASE.
#FEEL FREE TO EDIT THE BELOW VARIABLES THAT ARE USED FOR TESTING.
#FOR A LIST OF ALL VARIABLES AND OPTIONS, PLEASE VIEW THE INTERACTIVE TUTORIAL AT STARTUP.
test=4
tutorial_at_startup=False
#using_temp is no longer located here. It can be edited in exe(), but please only edit it while in BlakeLang.



true=True
false=False
echo=print
report=print






def read():
    with open('C:/Users/Blake/Desktop/temp.py', 'r') as doc:
        mytesttext = doc.read()
        doc.close()
    return (mytesttext)



def write(python, using_temp):
    #print(using_temp)
    if using_temp:
        in_doc=read()
        with open('C:/Users/Blake/Desktop/temp.py','w') as doc:
            doc.write(in_doc +'\n'+ str(python))
            doc.close()
        return read()
    return "not using temp"
        


def clear():
    i=0
    while i<25:
        print('\n\n')
        i+=1
    return





with open('C:/Users/Blake/Desktop/temp.py','w') as doc:
        doc.write('#placeholder')
        doc.close()

'''
syntax={'echo':'print',
        'end':'exit',
        'kill':'exit'}

def compileBS(code):
    for letterscode in code:
        for keys in syntax:
            BS=True
            for letter in keys:
                if letter != letterscode:
                    BS=False
                    break
    

'''

#tutorials are located here: python, BL, interactive


def python_tutorial(*args):
    clear()
    print("\nHi! this is a python tutorial. \nPython built-in help() command still works in BL.\nThis tutorial presumes you are new to python.")
    print("\nLet's start by writing some python. \nWhy don't you try some math operations?")
    print("\npy> 1 + 2\n3")
    print("py> ")
    prompt=input("py> ")
    lesson_complete=False
    while not lesson_complete:
        try:
            print(int(eval(prompt)))
            lesson_complete=True
        except:
            clear()
            print("Sorry, we didn't recognize that math. Try something simpler!\n")
            print("py> 1 + 2\n3")
            print("py> ")
            prompt=input("py> ")
    print("Good Job!")
    prompt=input('press enter to continue to lesson 2')
    clear()
    lesson_complete=False
    print("\nOk, now let's try printing something! \"printing\" just means \ngetting the computer to tell us something.")
    print("\npy> print(\"hello world\")\nhello world")
    print("py> ")
    prompt=input("py> ")
    lesson_complete=False
    while not(lesson_complete):
        if prompt.find('print') == -1:
            clear()
            print('We didn\'t understand that!\nTry printing something!\n')
            print("py> print(\"hello world\")\nhello world")
            print("py> ")
            prompt=input("py> ")
        else:
            try:
                eval(prompt)
                lesson_complete=True
            except:
                clear()
                print("\nSorry, we didn't recognize that. Be sure to include \"quotes\" and the (parentheses)!\n")
                print("\npy> print(\"hello world\")\nhello world")
                print("py> ")
                prompt=input("py> ")
    print('\nGreat! You learn fast!')
    prompt=input('press enter to continue to lesson 3')
    clear()
    lesson_complete=False
    print("Now let's try writing an if statement!")
    print("\npy> if True:\n.... \tprint('yes!')\n... else:\n... \tprint('no')\n... \nyes!")
    print("py> ")
    prompt='if '
    while not(lesson_complete):
        if prompt.find('if ') == -1:
            clear()
            print('We didn\'t understand that!\nTry writing an if statement!\n')
            print("""\nif statements require a condition (try True or False) and a colon, \nwith a statement (try a print statement!) indented after. \nTry to not just copy our example!""")
            print("\npy> if True:\n.... \tprint('yes!')\n... else:\n... \tprint('no')\n... \nyes!")
            print("py> ")
        prompt=input("py> ")
        code=prompt
        while prompt!='':
            prompt=input('... ')
            code=code+prompt
        else:
            try:
                exec(code)
                lesson_complete=True
            except:
                pass
                '''
                clear()
                print("\nSorry, we didn't recognize that. Be sure to include \"quotes\" and the (parentheses)!\n")
                print("\npy> print(\"hello world\")\nhello world")
                print("py> ")
                prompt=input("py> ")'''
    print('\ngood job!')
    prompt=input('press enter to continue to lesson 4')
    clear()
    lesson_complete=False
    print("Last lesson! You're gonna write your own function!")
    print("functions are extremely useful! They do things!")
    print("\ndef greetings(name):\n... \tprint(\"welcome \" + name)\n...\npy> greetings('Blake')\nwelcome Blake\npy>")
    prompt='def '
    if prompt.find('def ')==-1:
        pass
        #CONTINUE WORK HERE LATER BRO



def BL_tutorial(*args):
    clear()
    print("Here, we'll teach you about special stuff!\nThis is what makes BlakeLang unique!")
    




def interactive_tutorial(*args):
    if not(tutorial_at_startup):
        print("Auto tutorial is off.")
        return
    print('''
Hi and welcome to BlakeLang. This is the interactive tutorial.
For help on any particular aspect of coding, please call
function support with any parameters you wish to learn about.
Interactive built-in python help still functions in BL.
If you have not viewed this tutorial before, please continue.
You can also re-open this any time with interactive_tutorial()''')
    prompt=input('continue? (Y/N T/F yes/no true/false) ')
    if prompt.lower()=='n' or prompt.lower()=='f' or prompt.lower()=='no' or prompt.lower()=='false':
        print('\nOk, we get it! You can turn tutorial_at_startup to False in editing.\nIt\'s really easy.')
        return
    
    if not(prompt.lower()=='y' or prompt.lower()=='t' or prompt.lower()=='yes' or prompt.lower()=='true'):
        print("\nBecause you couldn't even answer that correctly, you get to take the tutorial!")
    print("\nWelcome to the tutorial! This'll help you get started\nand explain some features of both python and BlakeLang!")
    prompt=input("First off, do you know python? (Y/N T/F yes/no true/false) ")
    if prompt.lower()=='y' or prompt.lower()=='t' or prompt.lower()=='yes' or prompt.lower()=='true':
        print('\nOk, great! we\'ll skip over to BL_tutorial() now.')
        BL_tutorial()
        return
    
    if not(prompt.lower()=='n' or prompt.lower()=='f' or prompt.lower()=='no' or prompt.lower()=='false'):
        print("\nNext time, try just putting a y or n, because that's all we need!")
    print("\nGreat! Thanks for choosing to learn python with BlakeLang!\nWe'll learn some python first in python_tutorial(), and then switch\nover to what makes BlakeLang special.")
    python_tutorial()
    return

    





#HEART AND SOUL OF THE PROGRAM

#PLEASE DO NOT EDIT BELOW THIS POINT IF YOUR NAME ISN'T BLAKE JOHNSON


functions=[]

def exe():
    using_temp=False
    interactive_tutorial()
    code=input('py> ')
    while code!='exit' and code!='kill' and code!='close':
        
        if code.find('def ')!=-1 or code.find('class ')!=-1:
            function=code
            #print(using_temp)
            write(code, using_temp)
            while code != '':
                code=input('... ')
                if code !='':

                    function=function +'\n' + code
                    write(code, using_temp)
                else:
                    if not(using_temp):
                        if function.find('def ')==0:
                            functions.append(function)
                        try:
                            exec(function, globals())
                        except:
                            print('error')
                            error_message=sys.exc_info()
                            print(str(error_message[0]) + '\n' + str(error_message[1]) + '\n' + str(error_message[2]))
                            #print('sorry, you done did bad. Your function doesn\'t work. Try again, stupid.')
                            
        try:
            exec(code)
            #code=input('py> ')
        except:
            try:
                exec(read() + '\n' + code, globals())
                #code=input('py> ')
            except:
                print('error')
                error_message=sys.exc_info()
                print(str(error_message[0]) + '\n' + str(error_message[1]) + '\n' + str(error_message[2]))
        #print(using_temp)
        code=input('py> ')
    return "You have exited BlakeLang!"
print('''Welcome to BlakeLang ''' + version + "!" + version_functionality + '\n' + version_goal + '\nThank you for choosing BlakeLang!')
print(exe())


#YOU CAN EDIT BELOW HERE

#ANYTHING WRITTEN DOWN HERE WON'T WORK UNLESS YOU EXIT EXE() AND THEN REBOOT IT!

def willthiswork():
    return 'yes'#SPOILER ALERT: IT DIDN'T
