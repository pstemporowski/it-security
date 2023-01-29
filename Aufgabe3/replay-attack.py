Zx = 551735025
start = 1664653896

def lfsr(start, Zx):
  reg = start
  counter = 0
  checkVal = 0
  while counter < 17000000:
 
    bit = (reg  ^
        (reg>> 1) ^
       (reg >> 2) ^
       (reg >> 4) ^
       (reg >> 5) ^
       (reg >> 7) ^
       (reg >> 10) ^
       (reg >> 11) ^
       (reg >> 14) ^
       (reg >> 15) ^
       (reg >> 17) ^
       (reg >> 21) ^
       (reg >> 22) ^
       (reg >> 23)) & 0b1

    reg = (reg >> 1) | (bit << 23)

    checkVal = (checkVal >> 1) | (bit << 31)
    counter += 1
  
    if checkVal == Zx:        
        print("Found")
        return counter - 32
    
  return -1

result = lfsr(start, Zx)
print(result);