import sys

dictionary = {'a': 0,0: 'a', 'b': 1,1:'b', 'c': 2,2:'c', 'd': 3,3:'d', 'e': 4, 4:'e',
         'f': 5, 5:'f', 'g': 6,6:'g', 'h': 7, 7:'h','i': 8,8:'i', 'j': 9,9:'j',
         'k': 10, 10:'k','l': 11,11:'l', 'm': 12,12:'m', 'n': 13,13:'n', 'o': 14,14:'o',
         'p': 15, 15:'p','q': 16,16:'q', 'r': 17, 17:'r','s': 18, 18:'s','t': 19, 19:'t',
         'u': 20, 20:'u', 'v': 21, 21:'v', 'w': 22, 22:'w', 'x': 23, 23:'x', 'y': 24, 24:'y', 'z': 25,25:'z'}     

inFile = sys.argv[1]
outFile = sys.argv[2]
key = sys.argv[3]
selection = sys.argv[4]

if(selection == '1'):
  plainText = open(inFile, "r").read()    
  if(plainText.islower()==False):
     print("Invalid Input")
  else :
    for i in range(len(plainText)):
     if (len(key)>=len(plainText)):
       break
     else:
       key+=plainText[i]
    cipherText=''
    for x in range(len(plainText)):
              x = (dictionary[plainText[x]]+dictionary[key[x]]) % 26
              cipherText+=dictionary[x]
    open(outFile, "w").write(cipherText) 
  

if(selection == '0'):
  cipherText = open(inFile, "r").read()  
  decryptText=''
  for y in range(len(cipherText)):
           y = (dictionary[cipherText[y]]-dictionary[key[y]]+26) % 26
           decryptText+=dictionary[y]
           key+=dictionary[y]
  open(outFile, "w").write(decryptText)

