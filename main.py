pc = 0

REG_Names = {
    "R0":"000",
    "R1":"001",
    "R2":"010",
    "R3":"011",
    "R4":"100",
    "R5":"101",
    "R6":"110",
    "FLAGS":"111"
}

mem_address={}

variables = {}

REG = [0,0,0,0,0,0,0,[0,0,0,0]] #in the flag list [V (overflow), L, G, E]
OPCODES = {
    "add": ["10000", "A"],
    "sub": ["10001", "A"],
    "mov": ["10010", "B"],
    "ld": ["10100", "D"],
    "st": ["10101", "D"],
    "mul": ["10110", "A"],
    "div": ["10111", "C"],
    "rs": ["01000", "B"],
    "ls": ["01001", "B"],
    "xor": ["11010", "A"],
    "or": ["11011", "A"],
    "and": ["11100", "A"],
    "not": ["01101", "C"],
    "cmp": ["01110", "C"],
    "jmp": ["01111", "E"],
    "jlt": ["10000", "E"],
    "jgt": ["10001", "E"],
    "je": ["10010", "E"],
    "hlt": ["10011", "F"],
}

s = ""

def typeA(ins):
    global s
    if len(ins) == 4:
        if ins[0] == "add":


            s = OPCODES["add"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]

        if ins[0] == "sub":

            s = OPCODES["sub"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
        
        if ins[0] == "mul":

            s = OPCODES["mul"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
        
        if ins[0] == "xor":

            s = OPCODES["xor"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
        
        if ins[0] == "or":

            s = OPCODES["or"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
        
        if ins[0] == "and":

            s = OPCODES["and"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
        
def typeB(ins):
    global s
    if len(ins) == 3:
        if ins[0] == "mov":

            s = "10010" 

            if ins[1] in REG_Names and ins[1] != "FLAGS":
                s+= REG_Names[ins[1]]
            
            imm = int(ins[2][1:])#if float value entered, kya?

            if imm>255 or imm<0:
                REG[-1][0] = 1
            
            bin_imm = bin(imm)[2:]

            if len(bin_imm)<=8:
                n = 8 - len(bin_imm)

            s+= n*"0" + bin_imm
        
        if ins[0] == "ls":
            
            s = "11001"
            if ins[1] in REG_Names and ins[1] != "FLAGS":
                s+= REG_Names[ins[1]]
            
            imm = int(ins[2][1:])#if float value entered, kya?

            if imm>255 or imm<0:
                REG[-1][0] = 1
            
            bin_imm = bin(imm)[2:]

            if len(bin_imm)<=8:
                n = 8 - len(bin_imm)

            s+= n*"0" + bin_imm
        
        if ins[0] == "rs":
            
            s = "11000"
            if ins[1] in REG_Names and ins[1] != "FLAGS":
                s+= REG_Names[ins[1]]
            
            imm = int(ins[2][1:])#if float value entered, kya?

            if imm>255 or imm<0:
                REG[-1][0] = 1
            
            bin_imm = bin(imm)[2:]

            if len(bin_imm)<=8:
                n = 8 - len(bin_imm)

            s+= n*"0" + bin_imm

def typeC(ins):
    global s
    if len(ins) == 3:
        if ins[0] == "mov":
            s = "10011" + 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]
        
        if ins[0]=="div":
            s = "10111" + 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" :
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]

        if ins[0]=="not":
            s= "11101"+ 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" :
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]

        if ins[0]=="cmp":
            s= "11110"+ 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" :
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]

def typeD(ins):
    global s
    if len(ins) == 3:
        if ins[0] == "ld":

            s = "10100" 

            if ins[1] in REG_Names and ins[1] != "FLAGS":
                mem = ins[2]
                if mem in variables:
                    s+= REG_Names[ins[1]]
                    s+=variables[mem]
                
        if ins[0] == "st":

            s = "10101" 
            if ins[1] in REG_Names and ins[1] != "FLAGS":
                mem = ins[2]
                if mem in variables:
                    s+= REG_Names[ins[1]]
                    s+=variables[mem]

def typeE(ins):
    global s
    if len(ins) == 2:
        if ins[0] == "jmp":

            s = "11111" + 3*"0"

            if ins[1] in mem_address:
                mem_addr = mem_address[ins[1]]

            s+= mem_addr

        if ins[0] == "jlt":

            s = "01100" + 3*"0"

            if ins[1] in mem_address:
                mem_addr = mem_address[ins[1]]

            s+= mem_addr

        if ins[0] == "jgt":

            s = "01101" + 3*"0"

            if ins[1] in mem_address:
                mem_addr = mem_address[ins[1]]

            s+= mem_addr
        
        if ins[0] == "je":

            s = "01111" + 3*"0"

            if ins[1] in mem_address:
                mem_addr = mem_address[ins[1]]

            s+= mem_addr


def typeF(ins):
    global s
    if(len(ins)==1):
        s="01010"+"0"*11


def ins_type(ins):
    if(OPCODES[ins[0]][1]=="A"):
        typeA(ins)
    elif(OPCODES[ins[0]][1]=="B"):
        if(ins[0]=="mov"):
          if(len(ins)>2 and ins[2] in REG_Names):
              typeC(ins)
          else:
              typeB(ins)
    # elif(OPCODES[ins[0]][1]=="C"):
    #     typeC(ins)
    elif(OPCODES[ins[0]][1]=="D"):
        typeD(ins)
    elif(OPCODES[ins[0]][1]=="E"):
        typeE(ins)
    elif(OPCODES[ins[0]][1]=="F"):
        typeF(ins)
    

f=open("input.txt",'r')
data=f.readlines()
l=len(data)
k=0
flag = 0
varError = 0
output = []

for i in data:
    if(i[0]=="var" and flag==0):
        k+=1
    elif(i[0]=="var" and flag==1):
        varError=1
    else:
        flag=1
    
if(varError!=1):
    k=l-k-1
    for i in data:
      j=i.split()
      if j == []:
        pass
        
      elif(j[0] in OPCODES.keys()):
          ins_type(j)
          output.append(s)
      elif(j[1] in OPCODES.keys()):
          s1=bin(pc)[2:]
          s1="0"*(8-len(s1))+s1
          mem_address[j[0][:-1]]=s1
          #label store karn ah
          ins_type(j[1:])
          output.append(s)
      elif(j[0]=="var"):
          s1=bin(k)[2:]
          s1="0"*(8-len(s1))+s1
          variables[j[1]]=s1
          k+=1
      else:
        errorType="INVALID INSTRUCTION"
      pc+=1
      
with open("output.txt", "w") as txt_file:
    for line in output:
        txt_file.write("".join(line) + "\n")
