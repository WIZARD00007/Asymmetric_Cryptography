import string
import random

def Generate_key():
  #   text= input('Enter text to encrypt ')
  #   text2list=list(text)
  # #  bin1 =  ''.join(format(ord(i), '08b') for i in text)
  #   pub_lst=[]
  #   pub_key=[]
  #   count,lent=0,0
  #   for chri in text2list:
  #       pub_lst.append((ord(chri),chri))
  #
  #   sort_lst=sorted(pub_lst,reverse=True)
  #   for asc,chre in pub_lst:
  #      if asc%2==0:
  #
  #         count+=len(text)
  #         sc=(asc+len(chre))+count
  #         lent=lent+asc
  #         pub_key.append((chr(lent),chr(sc)))
  #      else:
  #         count=len(text)-count
  #         sc=(asc+len(chre))+count
  #         lent=lent+asc
  #         pub_key.append((chr(lent),chr(sc)))


     # print(pub_lst)
     # print(pub_key)

     key_generator=[]
     try:
        key_num=int(input("Enter length of public key :"))
        print("Generating your public key.....")
        public_key="".join(random.choices(string.ascii_uppercase+string.ascii_letters+string.ascii_lowercase+string.digits+string.punctuation,k=key_num))
        print("Your public key is ",public_key)
        key_word=input("Enter a keyword to generate your private key :")
        list_pub=list(public_key)
        list_key=list(key_word)
        count=0
        private_key=[]
        dict_str={public_key:private_key}
        for asc in list_pub:
           count=count+ord(asc)
           for asci in list_key:
               new_asc=ord(asc)+ord(asci)
               if len(private_key)<count:
                     private_key.append(chr(new_asc))


        str_pri=''.join([str(elem) for elem in private_key])
        with open("private_key.txt","w+",encoding='utf-8') as p_key:
            p_key.truncate(0)
            p_key.write(str_pri)
        with open("public_key.txt","w+",encoding='utf-8') as pu_key:
            pu_key.truncate(0)
            pu_key.write(public_key)
        print("your private key is :",str_pri)
        print("private key is successfully stored in private_key.txt and public key as public_key.txt")

     except:
         print("Please enter valid number.....")
         exit()

    # key_generator.append(gene_key)
    # bin3= ''.join(format(ord(i), '08b') for i in gene_key)
    # while len(bin3)<len(bin1):
    #     bin3=bin3+bin3
    # while len(bin1)<len(bin3):
    #   bin1=bin1+bin1
    # if len(bin1)!=len(bin3):
    #     x=len(bin3)-len(bin1)
    #     bin1=bin1[:x]
    # bin_txt=[str(int(bin1[i])^int(bin3[i])) for i in range(len(bin1))]
    # bin_txt=''.join(bin_txt)
    # d=[str(int(bin_txt[i])<<2) for i in range(len(bin1))]
    # d=''.join(d)
    #
    # print(bin_txt)
    # print(key_generator)
    # print(len(bin1),  len(bin3))
    # print(bin1)
    # print(len(bin3))
    # print(hash(gene_key))


