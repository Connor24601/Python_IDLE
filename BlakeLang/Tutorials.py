
def python_tutorial(*args):
    print("so far")
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
    prompt='something'
    code=''
    while not(lesson_complete):
        code=''
        prompt=input('py> ')
        code = code + prompt
        if prompt.find('def ')==-1:
            clear()
            print("Try defining a function! include 'def' before your function name\nand include all of your paratheses and identations!")
            print("\ndef greetings(name):\n... \treturn \"welcome \" + name\n...\npy> greetings('Blake')\nwelcome Blake\npy>")
        while prompt!='':
            prompt=input("... ")
            code = code + '\n' + prompt
        try:
            #print(code)
            exec(code, globals())
            print('\nCall your function!\n')
            prompt=input('py> ')
            if code[4:code.find('(')] in prompt:
                exec("print(" + prompt + ")", globals())
                lesson_complete=True
            else:
                assert False
        except:
            print("Oops! Something went wrong!")
            print("Try defining a function! include 'def' before your function name\nand include all of your paratheses and identations!")
            print("\ndef greetings(name):\n... \tprint(\"welcome \" + name)\n...\npy> greetings('Blake')\nwelcome Blake\npy>")
    print("Great! Now you know basic python!")
    prompt=input("Press enter to continue to BlakeLang tutorial")
    BL_tutorial()
        
    
        
        



def BL_tutorial(*args):
    clear()
    print("Here, we'll teach you about special stuff!\nThis is what makes BlakeLang unique!")
    print("BlakeLang takes python and tries to make it easier. \nHowever, python makes print statements difficult. \nFor example:")
    print(">>>var=5\n>>>var\n5\n\nIs python in IDLE. However, real python means this:\n\npy> var=5\npy> var\npy> print(var)\n5\n")
    print("BlakeLang cannot fix this. However, we do offer several commands of our own and quite a few built-in functions.")
    print("In BlakeLang, print, echo and report are all synonymous functions. They all use python 3.3.5 documentation.\nAll python in BlakeLang is 3.3.5.\n")
    prompt=input('Press enter to continue...')
    clear()
    print("BlakeLang was built around several concepts, one of them being laziness. \nGlobal variables 'true' and 'false' are assigned to the respective booleans.")
    print
    print("Fortunately, other aspects of BlakeLang are much more interesting.")
    print("BlakeLang was developed to be a perfect IDLE for python.\nThis includes being able to do any one-line python perfectly.")
    print("If, while, for and class statements will all work with multi-line capabilities.")
    print("And, of course, functions work perfectly as well. There are many BlakeLang features for functions.")
    print("\nThe default way for creating functions works perfectly. It copies your text and executes the function definition, defining it.")
    print("The function will then be stored in a dictionary 'functions', which has all functions that you define through the default method.")
    print("functions will have all your function definitions, with the keys being the function names. \nIt will not contain any other multi-line commands.")
    print("Functions can be successfully rewritten. \nPlease note that editing functions[yourfunction] will not change your function definition unless you then run \nexec(functions[yourfunction]), which is the same as redefining it.\nJust re-define it.")
    prompt=input('Press enter to continue...')
    clear()
    print("\nThere's also a second way to run functions in BlakeLang, which can also be used as a writeable file to execute in BL.")
    print("You can write things to execute in BL in temp.py. Be warned that temp.py is wiped at startup.")
    print("You can either start BlakeLang and then write what you want in temp, or use methods discussed below.")
    print("To do this, start running BlakeLang. Then, open your temp.py file and write whatever you want. \nWhen you switch back to BlakeLang, you can use read() and write(textinput, using_temp) to write and read what's in your temp file.")
    print("Then, to execute the cool things you wrote either directly in the temp file or wrote using the built-in write command, run exec(read()).")
    print("BlakeLang also offers a cool feature to combine with this. If you set variable using_temp to True (or true), the following things will happen.")
    print("\n1: All multi-line commands you write from this point on will be written into the temp file. When you have finished writing, it will run exec(read()) automatically.")
    print("\n2: Any functions you write from this point on will not be written into functions, nor will they execute through functions but through the temp file.")
    print("The functions dictionary method and the temp file are mutually exclusive because they are alternatives to each other if one breaks. \n'functions' is more reliable and is the default (using_temp=False).")
    print("However, the temp file does offer a way to write in temp without BlakeLang already started. \nBlakeLang, when executed, rewrites the temp file to make it empty. /nYou can change this by calling set_rewrite_temp_to(True or False) in BlakeLang. \nThen, you can close BlakeLang, write in temp, and execute it by starting BlakeLang again and calling exec(read())")
    print("Unlike changing the value to using_temp, set_rewrite_temp_to() is a change that will be 'remembered'.")
    print("\nPLEASE NOTE: To use any functionality with temp.py AT ALL, you NEED to rewrite the path for where write, read and rewrite find it. \nAll you need to do is change vars path_for_BlakeLang and path_for_temp.\nMy paths are already in there. Please format yours similarly.")
    prompt=input("Press enter to continue...")
    print("To see built-in functions and variables, just call globals()!")
    print("BlakeLang handles errors adeptly. If you write an inifinite loop, don't worry, \nkeyboard interrupts (cntrl + c for pc) will be your friend!")
    print("\nThanks for using BlakeLang! to get here again, just type BL_tutorial()!")
    print("\nNow entering BlakeLang... type exit, kill or close to exit, kill or close.")




def interactive_tutorial(*args):
    global startup
    if not(tutorial_at_startup) and startup:
        print("Auto tutorial is off. Call interactive_tutorial() if you want help.")
        return
    print('''
Hi and welcome to BlakeLang. This is the interactive tutorial.
Interactive built-in python help still functions in BL.
If you have not viewed this tutorial before, please continue.
You can also re-open this any time with interactive_tutorial()''')
    prompt=input('continue? (Y/N T/F yes/no true/false) ')
    if prompt.lower()=='n' or prompt.lower()=='f' or prompt.lower()=='no' or prompt.lower()=='false':
        print('\nOk, we get it! You can turn tutorial_at_startup to False in editing.\nIt\'s really easy.')
        return
    
    if not(prompt.lower()=='y' or prompt.lower()=='t' or prompt.lower()=='yes' or prompt.lower()=='true'):
        print("\nNext time, try just putting a y or n, because that's all we need!")
    print("\nWelcome to the tutorial! This'll help you get started\nand explain some features of both python and BlakeLang!")
    prompt=input("First off, do you know python? (Y/N T/F yes/no true/false) ")
    if prompt.lower()=='y' or prompt.lower()=='t' or prompt.lower()=='yes' or prompt.lower()=='true':
        print('\nOk, great! we\'ll skip over to BL_tutorial() now.')
        prompt=input("Press enter to continue to BlakeLang tutorial")
        BL_tutorial()
        #return
    
    if not(prompt.lower()=='n' or prompt.lower()=='f' or prompt.lower()=='no' or prompt.lower()=='false'):
        print("\nBecause you couldn't even answer that correctly, you get to take the tutorial!")
    print("\nGreat! Thanks for choosing to learn python with BlakeLang!\nWe'll learn some python first in python_tutorial(), and then switch\nover to what makes BlakeLang special.")
    prompt=input("Press enter to continue to python tutorial")
    python_tutorial()
    return
#print(interactive_tutorial())
