test=4


def read():
    with open('C:/Users/Blake/Desktop/temp.py', 'r') as doc:
        mytesttext = doc.read()
        doc.close()
    return (mytesttext)


def write(python):
    in_doc=read()
    with open('C:/Users/Blake/Desktop/temp.py','w') as doc:
        doc.write(in_doc +'\n'+ str(python))
        doc.close()
    #return read()
        
        








with open('C:/Users/Blake/Desktop/temp.py','w') as doc:
        doc.write('#placeholder')
        doc.close()











def exe():
    code=input('py> ')
    functions=[]
    while code!='exit':
        if code.find('def ')!=-1:
            write(code)
            while code != '':
                code=input('... ')
                if code !='':
                    write(code)
        if code=='':
            code=input('py> ')
        try:
            exec(code, globals())
            code=input('py> ')
        except:
            try:
                exec(read() + '\nprint(' + code + ')', globals())
                code=input('py> ')
            except:
                print('error')
                code=input('py> ')
print('''Welcome to BlakeLang! BlakeLang 1.1 includes perfectly functioning python,
with the exception of recursive calls. These will simply error out. To view
errors,simply ^c keyboard interrupt which will show errors. exe() will
re-initialize BL.''')
exe()



def willthiswork():
    return 'yes'
