'Sytax Errors---Program stops execution '
'Logical Errors(Exception)-- Unexpected behavior'

'Common exceptions' \
'. ValueError' \
'EOFError'
'ImportError'
'IOError'
'KeyboardinterruptError'

'Try, except, else, finally'



import sys  # for excetions
class Join:
    def __init__(self):
        print('Constructor function....joined fullstack classes today')


    def welcom(self):
        print('welcome to fullstack program ')

    def __del__(self):
        print('Destructor')

    def members(self):
        try:
            members = ['Raj', 'Venket', 'Ramu']
            print(members[3])


        #except IndexError:
         #   errorInfo = sys.exc_info()
         #   print(errorInfo[0], errorInfo[1])
            # print('exception occurred')

        except IOError:
            print('IOError')
        except ImportError:
            print('ImportError')

        else:
            print('Everything went fine')

        finally:
            print("doesn't matter what  i will execute")



j1 = Join()
j1.welcom()
j1.members()

