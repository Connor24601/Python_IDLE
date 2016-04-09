
version = '1.2'
version_functionality=""" This version contains functional Python."""
version_goal="""This version will handle the switch away from temp, also
attempting to make it optional in global var using_temp."""





test=4
true=True
false=False

import sys
import time
import math









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
        








with open('C:/Users/Blake/Desktop/temp.py','w') as doc:
        doc.write('#placeholder')
        doc.close()










functions=[]

def exe():
    using_temp=False
    code=input('py> ')
    while code!='exit':
        
        if code.find('def ')!=-1:
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
                        functions.append(function)
                        try:
                            exec(function, globals())
                        except:
                            pass
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
                print(sys.exc_info())
        #print(using_temp)
        code=input('py> ')
    return "You have exited BlakeLang!"
print('''Welcome to BlakeLang ''' + version + "!" + version_functionality + '\n' + version_goal + '\nThank you for choosing BlakeLang!')
print(exe())



def willthiswork():
    return 'yes'
