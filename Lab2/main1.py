import math

def encryption(string,key):
    encrypted=""
    result=[0,0]
    matrix=[0,0]
    if len(string)%2!=0:
        string=string+'Z'
    for i in range(0,len(string)//2):
        matrix=[ord(string[i*2])-65,ord(string[i*2+1])-65]
        result[0]=(key[0][0]*matrix[0]+key[0][1]*matrix[1])%26
        result[1]=(key[1][0]*matrix[0]+key[1][1]*matrix[1])%26
        encrypted=encrypted+chr(result[0]+65)+chr(result[1]+65)

    return encrypted

def decryption(string,key):
    decrypted=""
    result=[0, 0]
    detKey=key[0][0]*key[1][1]-key[0][1]*key[1][0]
    invdet=1
    while invdet*detKey%26!=1:
        invdet=invdet+1

    if(math.gcd(26,detKey)!=1):
        return "function is ireversible"
    adjKey=[[0,0],[0,0]]
    adjKey[0][0]=key[1][1]
    adjKey[1][1]=key[0][0]
    adjKey[0][1]=-key[0][1]
    adjKey[1][0]=-key[1][0]
    for i in range(0,2):
        for j in range(0,2):
            adjKey[i][j]=adjKey[i][j]*invdet%26

    for i in range(0,len(string)//2):
        matrix=[ord(string[i*2])-65,ord(string[i*2+1])-65]
        result[0]=(adjKey[0][0]*matrix[0]+adjKey[0][1]*matrix[1])%26
        result[1]=(adjKey[1][0]*matrix[0]+adjKey[1][1]*matrix[1])%26
        decrypted=decrypted+chr(result[0]+65)+chr(result[1]+65)

    return decrypted


string=input("Enter an string: ")
key=[[3,3],[2,5]]
string=string.replace(' ','')




print(string)
print(encryption(string,key))
print(decryption(encryption(string,key),key))