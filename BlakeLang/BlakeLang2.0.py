print("loading...")
version = '2.0'
version_functionality="""Tutorials located in subfolder. \nEverything should work."""
version_goal="""I should get a dict or similar of all these built-ins.
"""



import sys
import time
import math



#WELCOME TO BLAKELANG CODE!
#FEEL FREE TO EDIT THE BELOW VARIABLES THAT ARE USED FOR TESTING.
#FOR A LIST OF ALL VARIABLES, CALL GLOBALS(). TO LEARN ABOUT THEM, PLEASE VIEW BL_TUTORIAL OR INTERACTIVE_TUTORIAL AT STARTUP.

test=4
tutorial_at_startup=False
using_temp=False

path_for_BlakeLang='C:/Users/Blake/Desktop/BlakeLang/BlakeLang2.0.py'
path_for_temp='C:/Users/Blake/Desktop/temp.py'

true=True
false=False
echo=print
report=print

#Thank you for using BlakeLang!

#the following code is imported from AI.py in desktop. this is a test for 1.9.
"""woah"""

def read_self():
    with open(path_for_BlakeLang,"r") as self:
        read=self.read()
        self.close()
    return read

temp="C:/Users/Blake/Desktop/temp.py"
'''def 



'''
'''
class AI(type):
    def __init__(self, path, contents):
        self.path=path
        read(self)
        self.contents=contents
        
    def read(self):
            with open(temp, "r") as intemp:
                oldtemp=intemp
                document.close()
            with open(temp, "w") as doc:
                doc.write("with open('" + path + "', 'r') as doc:\n\t
    

Cyprus=AI#project cyprus is on hold
Cyprus.path="C:/Users/Blake/Desktop/AI.py"
'''
def edit_self(fixedstring,startandendlocation):
    with open(temp, "r") as intemp:
        oldtemp=intemp.read()
        intemp.close()
    with open(temp, "w") as doc:
        doc.write("""
with open('"""+path_for_BlakeLang+"""','r') as self:
    ithat=self.read()
    self.close()
with open('"""+path_for_BlakeLang+"""','w') as self:
    self.write(ithat[:""" + str(startandendlocation[0]) + '] + """' + fixedstring + '''""" + ithat[''' + str(startandendlocation[1]) + ':])\n    self.close()')
        doc.close()
    with open(temp,"r") as code:
        exec(code.read())
        code.close()
    with open(temp, "w") as done:
        done.write(oldtemp)
        done.close()
    return read_self()

def replace(good,bad):
    return edit_self(good, (read_self().find(bad), read_self().find(bad) + len(bad)))

def add_to_self(newcode):
	return edit_self(newcode,(-1,-1))


#now we return to native blakelang code
def read():
    with open(path_for_temp, 'r') as doc:
        #echo(type(doc))
        mytesttext = doc.read()
        doc.close()
    return (mytesttext)



def write(python, using_temp):
    #print(using_temp)
    if using_temp:
        in_doc=read()
        with open(path_for_temp,'w') as doc:
            doc.write(in_doc +'\n'+ str(python))
            doc.close()
        return read()
    return "not using temp"
        


def clear():#Clears screen, mostly used in Tutorials
    i=0
    while i<25:
        print('\n\n')
        i+=1
    return



#NOTE: YOU CAN EDIT THE TRUE/FALSE BELOW
#IT IS THE BOOLEAN RESPONSIBLE FOR REWRITING TEMP
#BUT FOR THE LOVE OF GOD, DON'T TAKE OUT THE COMMENTS, AND ANYTHING YOU WRITE IN BETWEEN THOSE COMMENTS WILL BE DELETED
#WHEN set_rewrite_temp_to() IS RUN

#key
if False:#endkey
    try:
        with open(path_for_temp,'w') as doc:
                doc.write('#placeholder')
                doc.close()
    except:
        print("Oops! Something's wrong, and it's probably your path_for_temp.")

def set_rewrite_temp_to(boolean):
    global using_temp
    current_temp=read()
    temp_using_temp=using_temp
    using_temp=True
    write("with open('"+path_for_BlakeLang+"','r') as doc:\n\tBlakeLang=doc.read()\n\tdoc.close()\nwith open(path_for_BlakeLang,'w') as doc:\n\tdoc.write(BlakeLang[:BlakeLang.find('#key')] + '#key\\nif "+str(boolean)+":' + BlakeLang[BlakeLang.find('#endkey'):])", using_temp)
    exec(read())
    using_temp=temp_using_temp
    with open(path_for_temp, 'w') as doc:
        doc.write(current_temp)
        doc.close()
    return boolean

#tutorials are located here: python, BL, interactive

#END TUTORIALS

with open("C:/Users/Blake/Desktop/BlakeLang/Tutorials.py", "r") as tutorials:
    try:
        exec(tutorials.read())
    except:
        print("Sorry, tutorials are down right now.")
    tutorials.close()





#HEART AND SOUL OF THE PROGRAM

#PLEASE DO NOT EDIT BELOW THIS POINT IF YOUR NAME ISN'T BLAKE JOHNSON


functions={}
startup=True

def exe():
    global using_temp
    
    global startup
    print(interactive_tutorial())
    startup=False
    code=input('py> ')
    while code!='exit' and code!='kill' and code!='close':
        
        if code.find('def ')!=-1 or code.find('class ')!=-1 or code.find('if ')!=-1 or code.find('for ')!=-1 or code.find('while ') != -1:
            function=code
            write(code, using_temp)
            while code != '':
                code=input('... ')
                if code !='':

                    function=function +'\n' + code
                    write(code, using_temp)
                else:
                    if not(using_temp):
                        if function.find('def ')==0:
                            functions[function[4:function.find('(')]]=function
                        try:
                            exec(function, globals())
                        except:
                            print('error')
                            error_message=sys.exc_info()
                            print(str(error_message[0]) + '\n' + str(error_message[1]) + '\n' + str(error_message[2]))
                            #print('sorry, you done did bad. Your function doesn\'t work. Try again, stupid.')
                            
        try:
            exec(code, globals())
        except:
            try:
                if using_temp:
                    exec(read() + '\n' + code, globals())
                else:
                    exec(code, globals())
            except:
                print('error')
                error_message=sys.exc_info()
                print(str(error_message[0]) + '\n' + str(error_message[1]) + '\n' + str(error_message[2]))
        code=input('py> ')
    return "You have exited BlakeLang!"
print('''Welcome to BlakeLang ''' + version + "! \n" + version_functionality + '\n' + version_goal + '\nThank you for choosing BlakeLang!')
print(exe())#LIVE!!! LIVE!!! LIVE!!! MUAHAHAHAHAAHAA...


#YOU CAN EDIT BELOW HERE

#ANYTHING WRITTEN DOWN HERE WON'T WORK UNLESS YOU EXIT EXE() AND THEN REBOOT IT!

def willthiswork():
    return 'yes'#SPOILER ALERT: IT DIDN'T
