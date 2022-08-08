import math

def space_stoint(s):
    i = int(s[0])

    if (s[1] == "Mb"):
        m = 1024 * 1024
    elif (s[1] == "MB"):
        m = 1024 * 1024 * 8
    elif (s[1] == "kB"):
        m = 1024 * 8
    elif (s[1] == "kb"):
        m = 1024
    elif (s[1] == "B"):
        m = 8
    elif (s[1] == "b"):
        m = 1
    
    return i * m

def mem_addr_to_bits(s, cpu_bits):
    if (s == "Bit"):
        return 1
    elif (s == "Nibble"):
        return 4
    elif (s == "Byte"):
        return 8
    else:
        return cpu_bits


space = space_stoint(input("Enter space in memory (Mb/MB/kb/kB/B/b): ").split())  #gives you space in bits

#print(math.log(space, 2)) checking if correct, it is

mem_addressing = input("Enter type of memory addressing (Bit/Nibble/Byte/Word): ")

type = input("Enter type of query: ")
    
if type == "1,1":
    inslen = int(input("Enter length of one instruction in bits: "))
    reglen = int(input("Enter length of one register in bits: "))
    
    address_bits = int(math.log(space/mem_addr_to_bits(mem_addressing, 8),2))
    op_code_bits = inslen - reglen - address_bits
    filler_bits = inslen - 2*reglen - op_code_bits

    print("Minimum bits required to represent an address:", address_bits)
    print("Number of bits needed by opcode:", op_code_bits)
    print("Number of filler bits:", filler_bits)
    print("Maximum number of instructions this ISA can support:", pow(2, op_code_bits))
    print("Maximum number of registers it can support:", pow(2, reglen))

elif type == "2,1":
    cpu_bits = int(input("Number of bits in the CPU: "))
    enhanced_mem_addr = input("Enter enhanced memory addressing type (Bit/Nibble/Byte/Memory): ")

    change_pins = mem_addr_to_bits(mem_addressing, cpu_bits) / mem_addr_to_bits(enhanced_mem_addr, cpu_bits)

    print(int(math.log(change_pins, 2)))

elif type == "2,2":
    cpu_bits = int(input("Number of bits in the CPU: "))
    pins = int(input("Enter number of address pins: "))
    mem_addressing_new = input("Enter type of memory addressing (Bit/Nibble/Byte/Word): ")

    m = mem_addr_to_bits(mem_addressing_new, cpu_bits)
    x = int(pow(2, pins)*m/8)
    print(x, "Bytes")
