import sys

token = ''                          # current token
src = ''                            # source code string
index = pre_index = 0               # pointer to source code string
poolsize = 0                        # default size of text/data/stack
line = 0                            # line number

# get next token
def next():
    global token,index
    # prevent index out of range
    if  index < len(src):
        token = src[index]
        index = index + 1
        return True
    return False

# do nothing yet
def expression(level):
    pass

def program():
    while next():
        print("token is: ", token)

# do nothing yet
def eval():
    pass

if __name__=="__main__":
    poolsize = 256 * 1024   # arbitrary size
    line = 1 
    try:
        with open(sys.argv[1], 'r') as f:
            src = f.read()
    except IOError as err:
        print("Error: "+str(err))
    except Exception as err:
        print("Error: "+str(err))
    else:
        print("File read successful")
        program()
        eval()