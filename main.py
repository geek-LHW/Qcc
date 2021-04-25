import sys
from enum import Enum

token = ''                          # current token
src = ''                            # source code string
index = pre_index = 0               # pointer to source code string
poolsize = 0                        # default size of text/data/stack
line = 0                            # line number
text = []                           # text segment
pc = 0                              # program counter
stack = []                          
sp = 0                              # stack pointer

'''
ax is the general purpose register used to store the result of an instruction execution
'''
ax = 0   

# instructions
class INS(Enum):
    LEA = 0 
    IMM = 1 
    JMP = 2 
    CALL = 3 
    JZ  = 4 
    JNZ = 5 
    ENT = 6 
    ADJ = 7
    LEV = 8
    LI  = 9
    LC  = 10
    SI  = 11
    SC  = 12  
    PUSH = 13
    OR  = 14 
    XOR = 15 
    AND = 16 
    EQ  = 17 
    NE  = 18 
    LT  = 19 
    GT  = 20 
    LE  = 21  
    GE  = 22 
    SHL = 23 
    SHR = 24 
    ADD = 25 
    SUB = 26 
    MUL = 27 
    DIV = 28 
    MOD = 29
    OPEN = 30
    READ = 31 
    CLOS = 32 
    PRTF = 33
    MALC = 34 
    MSET = 35
    MCMP = 36 
    EXIT = 37


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
    op = 0
    global pc,ax,sp
    while 1:
        op = text[pc]    #get next operation code
        pc = pc + 1 
        if  op == INS.IMM.value :
            ax = text[pc]
            pc = pc + 1 
        elif op == INS.PUSH.value :
            sp = sp - 1 
            stack[sp] = ax
        elif op == INS.ADD.value :
            ax = stack[sp] + ax
            sp = sp + 1    
        elif op == INS.EXIT.value :  
            print("exit(%d)" %stack[sp]) 
            return stack[sp]
        else:
            print("unknown instruction:%d" %op)
            return -1
    
    return 0

if __name__=="__main__": 
    poolsize = 1024   # arbitrary size
    line = 1
    for i in range(1024):
        stack.append(0)
    sp = poolsize
    try:
        with open(sys.argv[1], 'r') as f:
            src = f.read()
    except IOError as err:
        print("Error: "+str(err))
    except Exception as err:
        print("Error: "+str(err))
    else:
        print("File read successful")
        # test
        text.append(INS.IMM.value)
        text.append(10)
        text.append(INS.PUSH.value)
        text.append(INS.IMM.value)
        text.append(20)
        text.append(INS.ADD.value)
        text.append(INS.PUSH.value)
        text.append(INS.EXIT.value)  
        program()
        eval()