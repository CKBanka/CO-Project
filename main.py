pc = 0

def check_variable_name(var_name, lineno):
    #must be alphanumeric
    #must not be an instruction, register, label
    if (not(var_name.isalnum())):
        print("Variable name must be alphanumeric, Error in line:", lineno+1)
    elif var_name in OPCODES.keys():
        print("Variable name cannot be an , Error in line: ",lineno+1)
    elif var_name in REG_Names.keys():
        print("Variable name cannot be a register, Error in line:", lineno+1)
    elif var_name in mem_address.keys():
        print("Variable name cannot be a label, Error in line:", lineno+1)
    elif var_name in variables.keys():
      print("Cannot redefine variables, Error in line:", lineno+1)
   
def check_label_name(label_name, lineno):
    #must be alphanumeric
    #must not be an instruction, register, variable
    if (not(label_name.isalnum())):
        print("Label name must be alphanumeric, Error in line:", lineno+1)
    elif label_name in OPCODES.keys():
        print("Label name cannot be an , Error in line: ",lineno+1)
    elif label_name in REG_Names.keys():
        print("Label name cannot be a register, Error in line:", lineno+1)
    elif label_name in variables.keys():
        print("Label name cannot be a variable, Error in line:",lineno+1)
    elif label_name in mem_address.keys():
      print("Cannot redefine labels, Error in line:", lineno+1)
        
        
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
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()

        if ins[0] == "sub":

            s = OPCODES["sub"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
        
        if ins[0] == "mul":

            s = OPCODES["mul"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
        
        if ins[0] == "xor":

            s = OPCODES["xor"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
        
        if ins[0] == "or":

            s = OPCODES["or"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
        
        if ins[0] == "and":

            s = OPCODES["and"][0] + 2*"0"

            if ins[1] in REG_Names and ins[2] in REG_Names and ins[3] in REG_Names:
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" and ins[3] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]] + REG_Names[ins[3]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
    else:
      print("Invalid Instruction Length")
      exit()
      
                  
        
def typeB(ins):
    global s
    if len(ins) == 3:
        if ins[0] == "mov":

            s = "10010" 

            if ins[1] in REG_Names:
              if ins[1] != "FLAGS":
                s+= REG_Names[ins[1]]
              else:
                print("Invalid use of flags in line "+str(pc+1))
                exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
            
            if int(ins[2][1:])<float(ins[2][1:]):
              print("Float value entered.")
              exit()
            
            imm = int(ins[2][1:])#if float value entered, kya?

            if imm>255 or imm<0:
                REG[-1][0] = 1
            
            bin_imm = bin(imm)[2:]

            if len(bin_imm)<=8:
                n = 8 - len(bin_imm)

            s+= n*"0" + bin_imm
        
        if ins[0] == "ls":
            
            s = "11001"
            if ins[1] in REG_Names:
              if ins[1] != "FLAGS":
                s+= REG_Names[ins[1]]
              else:
                print("Invalid use of flags in line "+str(pc+1))
                exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()

            if int(ins[2][1:])<float(ins[2][1:]):
              print("Float value entered.")
              exit()
            
            imm = int(ins[2][1:])#if float value entered, kya?

            if imm>255 or imm<0:
                REG[-1][0] = 1
            
            bin_imm = bin(imm)[2:]

            if len(bin_imm)<=8:
                n = 8 - len(bin_imm)

            s+= n*"0" + bin_imm
        
        if ins[0] == "rs":
            
            s = "11000"
            if ins[1] in REG_Names:
              if ins[1] != "FLAGS":
                s+= REG_Names[ins[1]]
              else:
                print("Invalid use of flags in line "+str(pc+1))
                exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
            
            if int(ins[2][1:])<float(ins[2][1:]):
              print("Float value entered.")
              exit()
            
            imm = int(ins[2][1:])#if float value entered, kya?
          

            if imm>255 or imm<0:
                REG[-1][0] = 1
            
            bin_imm = bin(imm)[2:]

            if len(bin_imm)<=8:
                n = 8 - len(bin_imm)

            s+= n*"0" + bin_imm
    else:
      print("Invalid Instruction Length")
      exit()
def typeC(ins):
    global s
    if len(ins) == 3:
        if ins[0] == "mov":
            s = "10011" + 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS":
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
        
        if ins[0]=="div":
            s = "10111" + 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" :
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()

        if ins[0]=="not":
            s= "11101"+ 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" :
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()

        if ins[0]=="cmp":
            s= "11110"+ 5*"0"
            if ins[1] in REG_Names and ins[2] in REG_Names :
                if ins[1] != "FLAGS" and ins[2] != "FLAGS" :
                    s += REG_Names[ins[1]] + REG_Names[ins[2]]
                else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
    else:
      print("Invalid Instruction Length")
      exit()
def typeD(ins):
    global s
    if len(ins) == 3:
        if ins[0] == "ld":

            s = "10100" 

            if ins[1] in REG_Names:
              if ins[1] != "FLAGS":
                mem = ins[2]
                if mem in variables:
                    s+= REG_Names[ins[1]]
                    s+=variables[mem]
                else:
                  print("Memory Address not found")
                  exit()
              else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED")
              exit()
                
        if ins[0] == "st":

            s = "10101" 
            if ins[1] in REG_Names:
              if ins[1] != "FLAGS":
                mem = ins[2]
                if mem in variables:
                    s+= REG_Names[ins[1]]
                    s+=variables[mem]
              else:
                  print("Invalid use of flags in line "+str(pc+1))
                  exit()
            else:
              print("UNKNOWN REGISTER IDENTIFIED IN LINE "+str(pc+1))
              exit()
    else:
      print("Invalid Instruction Length")
      exit()
      
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
    else:
      print("Invalid Instruction Length")
      exit()

def typeF(ins):
    global s
    if(len(ins)==1):
        s="01010"+"0"*11
    else:
      print("Invalid Instruction Length")
      exit()


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
    else:
      print("INVALID INSTRUCTION IN LINE"+str(pc+1))
      exit()

f=open("input.txt",'r')
data=f.readlines()
l=len(data)
k=0
flag = 0
varError = 0
output = []



#hlt not last instruction
for j in range(len(data)-1,-1):
  if(j!=[]):
    if j!="hlt":
      print("Halt is not the last instruction, Error in line", data.index("hlt"))
      exit()
    


#multiple halt statements 
hlt_no=0
for i in data:
  if("hlt" in i):
    hlt_no+=1
if(hlt_no>1):
  print("MULTIPLE HLT DETECTED")
  exit()
elif(hlt_no==0):
  print("NO HLT INSTRUCTION DETECTED")
  exit()
  




    

flag=0
for i in data:
  
    if(i[0:3]=="var" and flag==0):
        k+=1
    elif(i[0:3]=="var" and flag==1):
        varError=1
    else:
        flag=1
t=0
if(varError!=1):
    for i in data:
      if(i==[]):
        t+=1
    k=l-k-1-t
    for i in data:
      j=i.split()
      if j == []:
        pc-=1
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
          check_variable_name(j[1],pc)
          variables[j[1]]=s1
          k+=1
      elif i[0][-1]==":":
        check_label_name(i[1],pc)




      
      else:
        errorType="INVALID INSTRUCTION"
        print(errorType)
        exit()
      pc+=1
else:
  print("ALL VARIABLES MUST BE DEFINED AT THE BEGINNING")
  exit()
#variables not mentioned in beginning

#immediate value more than 8 bits
if REG[-1][0]==1:
    print("Illegal Immediate value")
    exit()




     



with open("output.txt", "w") as txt_file:
    for line in output:
        txt_file.write("".join(line) + "\n")




    
