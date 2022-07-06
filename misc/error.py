


def check_variable_name(var_name, lineno):
    #must be alphanumeric
    #must not be an instruction, register
    if (not(var_name.isalnum())):
        print("Variable name must be alphanumeric, Error in line:", lineno)
    elif var_name in OPCODE.keys():
        print("Variable name cannot be an , Error in line: ",lineno)
    elif var_name in REG_NAMES.keys():
        print("Variable name cannot be a register, Error in line:", lineno)
    elif var_name in mem_address.keys():
        print("Variable name cannot be a label, Error in line:", lineno)

def check_label_name(label_name, lineno):
    #must be alphanumeric
    #musr not be an instruction, register
    if (not(label_name.isalnum())):
        print("Label name must be alphanumeric, Error in line:", lineno)
    elif label_name in OPCODE.keys():
        print("Label name cannot be an , Error in line: ",lineno)
    elif label_name in REG_NAMES.keys():
        print("Label name cannot be a register, Error in line:", lineno)
    elif label_name in variables.keys():
        printf("Label name cannot be a variable, Error in line:",lineno)
        
        
        
        
#illegal use of flags 
if data[0]!="mov":
    printf("flags cannot be used with this instruction")
    
#hlt not included     
if "hlt" not in data:
    print("Halt has not been mentioned")
    
#hlt not last instruction
if data[-1]!="hlt":
    print("Halt is not the last instruction, Error in line", index("hlt"))

#multiple halt statements 
if "hlt"in data[-2::-1]:
  print("Multiple halt statements ")
    
#variables not mentioned in beginning
if varError=1:
    print("Variables not mentioned in the beginning")

#immediate value more than 8 bits
if REG[-1][0]==1:
    print("Illegal Immediate value")
  

  
    



    
    
    

