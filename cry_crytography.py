from key_generator import Generate_key
from encryptor import Encryptor
from decryptor import Decryptor
print("select one option")
print("1 - Generate a key")
print("2 - Encrypt your text")
print("3 - Decrypt your text")
try:
    get=input('>>>')
    if get=="1":
        Generate_key()
    elif get=="2":
        Encryptor()
    elif get=="3":
        Decryptor()
    else:
        print("please enter a valid choice")
except:
    print("please enter a valid option")


