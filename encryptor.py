from bitstring import BitArray
def Encryptor():
    text=input("Enter text to encrypt :")
    publ_key=input("Enter your public key :")
    print("Total length of your text is ",len(text))
    len_t=len(text)
    len_st=str(len_t)
    text_len=''.join(format(ord(i), '08b') for i in len_st)
    bin1 =''.join(format(ord(i), '08b') for i in text)
    bin3 =''.join(format(ord(i), '08b') for i in publ_key)
    while len(bin3)<len(bin1):
         bin3=bin3+bin3
    while len(bin1)<len(bin3):
       bin1=bin1+bin1
    if len(bin1)!=len(bin3):
       x=len(bin3)-len(bin1)
       bin1=bin1[:x]
    bin_txt=[str(int(bin1[i])^int(bin3[i])) for i in range(len(bin1))]
    bin_txt=''.join(bin_txt)
    bin_lst=list(bin_txt)
    st_strng=''.join([str(elem) for elem in bin_lst])
    li_c=[]
    li_o=[]
    c=0
    for i in bin_lst:
        li_c.append(i)
        c=c+1
        if c%4==0:
            li_c.append(' ')
    st_strngt=''.join([str(elem) for elem in li_c])
    st_str=st_strngt.split()
    x_enc_txt=[]
    for i in st_str:
        if i==  "0000":
            xn="a"
            x_enc_txt.append(xn)
        elif i=="0001":
            xn="b"
            x_enc_txt.append(xn)
        elif i=="0010":
            xn="c"
            x_enc_txt.append(xn)
        elif i=="0011":
            xn="d"
            x_enc_txt.append(xn)
        elif i=="0100":
            xn="e"
            x_enc_txt.append(xn)
        elif i=="0101":
            xn="f"
            x_enc_txt.append(xn)
        elif i=="0110":
            xn="g"
            x_enc_txt.append(xn)
        elif i=="0111":
            xn="h"
            x_enc_txt.append(xn)
        elif i=="1000":
            xn="i"
            x_enc_txt.append(xn)
        elif i=="1001":
            xn="j"
            x_enc_txt.append(xn)
        elif i=="1010":
            xn="k"
            x_enc_txt.append(xn)
        elif i=="1011":
            xn="l"
            x_enc_txt.append(xn)
        elif i=="1100":
            xn="m"
            x_enc_txt.append(xn)
        elif i=="1101":
            xn="n"
            x_enc_txt.append(xn)
        elif i=="1110":
            xn="o"
            x_enc_txt.append(xn)
        elif i=="1111":
            xn="p"
            x_enc_txt.append(xn)
        elif i=="000":
            xn="q"
            x_enc_txt.append(xn)
        elif i=="001":
            xn="r"
            x_enc_txt.append(xn)
        elif i=="010":
            xn="s"
        elif i=="011":
            xn="t"
            x_enc_txt.append(xn)
        elif i=="100":
            xn="u"
            x_enc_txt.append(xn)
        elif i=="101":
            xn="v"
            x_enc_txt.append(xn)
        elif i=="110":
            xn="w"
            x_enc_txt.append(xn)
        elif i=="111":
            xn="x"
            x_enc_txt.append(xn)
        elif i=="00":
            xn="y"
            x_enc_txt.append(xn)
        elif i=="01":
            xn="z"
            x_enc_txt.append(xn)
        elif i=="10":
            xn="A"
            x_enc_txt.append(xn)
        elif i=="11":
            xn="B"
            x_enc_txt.append(xn)
        elif i=="0":
            xn="C"
            x_enc_txt.append(xn)
        elif i=="1":
            xn="D"
            x_enc_txt.append(xn)
    st_strngt_en=''.join([str(elem) for elem in x_enc_txt])


    print("Encrypted text is :",st_strngt_en)



    with open("encry.txt","w+") as p_key:
            p_key.truncate(0)
            p_key.write(str(st_strngt_en))
    bv=len(text)
    with open('text_length.txt','w+') as key:
        key.truncate(0)
        key.write(str(bv))

