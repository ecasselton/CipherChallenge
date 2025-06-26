import cipherchallenge as cc

def o(char):
    return ord(char)-65

def c(num):
    return chr(num+65)

ciphertext = cc.remove_whitespace(cc.get_ciphertext())
# Crib must be exactly as long as the key word
# Certain cribs only work for forwards or backwards (because you subtract in a certain order)
# crib = "PECIFIEDFOR"
# crib = "THEINDIAPAV"
crib = "CJANUSPROJECTFILESPARTHREETHEDETONATORSENCLOSEDINTHESHIPMENTAREOFOUROWNDESIGNANDEACHCANPRODUCEASHOCKWAVEEQUIVALENTTOTHATOFASMALLRIFLECARTRIDGEACCORDINGLYTHEYTAKEUPASIMILARSPACETHOUGHTHEABSENCEOFANYPROJECTILEMEANSTHATMORECANFITINTOTHECRATETHEDEPLOYMENTOFTHOSEDEVICESSHOULDBERELATIVELYROUTINEBEINGSMALLANDUNOBTRUSIVETHEYAREEXTREMELYUNLIKELYTOBEDISCOVEREDUNDERCASUALINSPECTIONESPECIALLYSINCEWEHAVEBEENABLETOCOLOURTHEIRCASESUSINGTHEEXACTPAINTSPECIFIEDFORTHEINDIAPAVILIONSTEELWORKTHISISDUEOFCOURSETOTHEINFLUENCEOFOURPATRONHERRKAISERTOWHOMWEOWEOURDEEPESTTHANKSTHECHARGESARETOOSMALLTOCAUSEMUCHDAMAGETOTHESTEELWORKITSELFBUTSINCEITISNOTOURINTENTIONTODESTROYTHEPAVILIONBUTONLYTOCLEARITTHISISNOTASIGNIFICANTISSUEASUITABLYCOORDINATEDDISCHARGESHOULDACHIEVEOURAIMSANDTHEINGENIOUSNEWTIMINGMECHANISMSEMPLOYINGTHEMARVELLOUSMINIATURISEDCLOCKMECHANISMSDEVELOPEDBYTHECOMPANYWILLENSUREMAXIMUMIMPACT"

# index = 450

for i in range(0, 1, 1):
    word = ""
    for j in range(len(crib)):
        word += c((o(ciphertext[i+j])-o(crib[j]))%26)

    print(f"{i}: {word}", end="  ")
    # print(ciphertext[i:i+len(crib)])

plainlist = []

# print(crib, end="")
# Go forwards
# for i in range(index, len(ciphertext), len(crib)):
#     new_crib = ""
#     length = min(len(crib), len(ciphertext) - i)
#     for j in range(length):
#         new_crib += c((o(ciphertext[i+j])-o(crib[j]))%26)
#     crib = new_crib
#     print(crib, end="")

# Go backwards
# for i in range(index, 0, -len(crib)):
#     new_crib = ""
#     length = min(len(crib), i)
#     for j in range(length):
#         new_crib += c((o(ciphertext[i+j])-o(crib[j]))%26)
#     crib = new_crib
#     plainlist.insert(0, crib)
#     print(crib, end="\n")

# print("".join(plainlist))
# print(plaintext)
