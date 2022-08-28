def Decryptor():
    enc_text=input("Enter encrypted text :")
    nb=list(enc_text)
    x_enc_txt=[]
    for i in nb:
        if i==  "a":
            xn="0000"
            x_enc_txt.append(xn)
        elif i=="b":
            xn="0001"
            x_enc_txt.append(xn)
        elif i=="c":
            xn="0010"
            x_enc_txt.append(xn)
        elif i=="d":
            xn="0011"
            x_enc_txt.append(xn)
        elif i=="e":
            xn="0100"
            x_enc_txt.append(xn)
        elif i=="f":
            xn="0101"
            x_enc_txt.append(xn)
        elif i=="g":
            xn="0110"
            x_enc_txt.append(xn)
        elif i=="h":
            xn="0111"
            x_enc_txt.append(xn)
        elif i=="i":
            xn="1000"
            x_enc_txt.append(xn)
        elif i=="j":
            xn="1001"
            x_enc_txt.append(xn)
        elif i=="k":
            xn="1010"
            x_enc_txt.append(xn)
        elif i=="l":
            xn="1011"
            x_enc_txt.append(xn)
        elif i=="m":
            xn="1100"
            x_enc_txt.append(xn)
        elif i=="n":
            xn="1101"
            x_enc_txt.append(xn)
        elif i=="o":
            xn="1110"
            x_enc_txt.append(xn)
        elif i=="p":
            xn="1111"
            x_enc_txt.append(xn)
        elif i=="q":
            xn="000"
            x_enc_txt.append(xn)
        elif i=="r":
            xn="001"
            x_enc_txt.append(xn)
        elif i=="s":
            xn="010"
        elif i=="t":
            xn="011"
            x_enc_txt.append(xn)
        elif i=="u":
            xn="100"
            x_enc_txt.append(xn)
        elif i=="v":
            xn="101"
            x_enc_txt.append(xn)
        elif i=="w":
            xn="110"
            x_enc_txt.append(xn)
        elif i=="x":
            xn="111"
            x_enc_txt.append(xn)
        elif i=="y":
            xn="00"
            x_enc_txt.append(xn)
        elif i=="z":
            xn="01"
            x_enc_txt.append(xn)
        elif i=="A":
            xn="10"
            x_enc_txt.append(xn)
        elif i=="B":
            xn="11"
            x_enc_txt.append(xn)
        elif i=="C":
            xn="0"
            x_enc_txt.append(xn)
        elif i=="D":
            xn="1"
            x_enc_txt.append(xn)
    st_strngt_enb=''.join([str(elem) for elem in x_enc_txt])
    pr_key=input("Enter your private key :")
    pr_keyword=input("Enter secret keyword :")
    text_len=int(input("Enter your text lenghth :"))
  #  pu_key=input("Enter public key :")
    lnm=[]
    try:
       with open("private_key.txt","r",encoding='utf-8') as rd:
          x_rd=rd.read()
          if pr_key==x_rd:

              decry_gen=[]
              count=len(pr_key)
              for ascm in pr_keyword:
                  x=ord(ascm)
                  #print(x)
                  for asv in pr_key:
                      count=count-ord(asv)
                     # if count<0:

                     # print((ord(asv)-ord(ascm)),ord(ascm),ord(asv))
                      xc=ord(asv)-ord(ascm)
                     # print(c)
                     # new_c=x-c
                      lnm.append(xc)
       pub_key=lnm[0:len(pr_key):len(pr_keyword)]
       n_list=[]
       for xm in pub_key:
           vb=chr(xm)
           n_list.append(vb)
       str_pri=''.join([str(elem) for elem in n_list])
       cvx=st_strngt_enb
       bin3 =''.join(format(ord(i), '08b') for i in str_pri)
       while len(cvx)>len(bin3):
          bin3=bin3*len(cvx)
          len2=len(bin3)
       if len(cvx)!=len(bin3):
         binx=bin3[:len(cvx)]
       bin_txt=[str(int(cvx[i])^int(bin3[i])) for i in range(len(cvx))]
       c=''.join(bin_txt)

       d=[c[i:i+8] for i in range(0, len(c), 3)]
       d1=' '.join([c[i:i+8] for i in range(0, len(c), 8)])
       binary_values = d1.split()
       ascii_string = ""
       for binary_value in binary_values:
          an_integer = int(binary_value, 2)
          ascii_character = chr(an_integer)
          ascii_string += ascii_character
       print('decrypted text is : ',ascii_string[:text_len:])




    except:
        print("check your private key/private keyword :")
