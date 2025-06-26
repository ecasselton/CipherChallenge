def decipher(ciphertext, period, key):
    blocks = [ciphertext[i:i+period] for i in range(0, len(ciphertext), period)]
    plaintext = ""
    for block in blocks:
        rect = [[]]
        j = 0
        for char in block:
            value = key.index(char)
            for i in (9, 3, 1):
                rect[j//len(block)].append(value // i)
                value %= i
                j += 1
                if (j % len(block) == 0):
                    rect.append([])


        for i in range(len(block)):
            plaintext += key[rect[0][i] * 9 + rect[1][i] * 3 + rect[2][i]]

    return plaintext

def encipher(ciphertext, period, key):
    blocks = [ciphertext[i:i+period] for i in range(0, len(ciphertext), period)]
    plaintext = ""
    for block in blocks:
        rect = [0] * 3 * period
        for j in range(len(block)):
            char = block[j]
            value = key.index(char)
            for i in range(3):
                rect[i*period+j] = value // 3**(2-i)
                value %= 3**(2-i)

        for i in range(0, len(rect), 3):
            plaintext += key[rect[i] * 9 + rect[i+1] * 3 + rect[i+2]]

    return plaintext

key = [char for char in "KEYWORDABCFGHIJLMNPQSTUVXZ+"]
period = 7
plaintext = "HEWONDEREDIFHESHOULDDISCLOSETHETRUTHTOHISFRIENDSITWOULDBEARISKYMOVEYESTHETRUTHWOULDMAKETHINGSALOTEASIERIFTHEYALLSTAYEDONTHESAMEPAGEBUTTHETRUTHMIGHTFRACTURETHEGROUPLEAVINGEVERYTHINGINEVENMOREOFAMESSTHANITWASNOTTELLINGTHETRUTHITWASTIMETODECIDEWHICHWAYTOGOITREALLYDIDNTMATTERWHATTHEYDIDTOHIMHESALREADYMADEUPHISMINDWHATEVERCAMEHISWAYHEWASPREPAREDFORTHECONSEQUENCESHEKNEWINHISHEARTTHATTHESACRIFICEHEMADEWASDONEWITHLOVEANDNOTHATENOMATTERHOWOTHERSDECIDEDTOSPINITIMSOCONFUSEDBYYOURRIDICULOUSMELTDOWNTHATIMUSTINSISTONSOMESORTOFEXPLANATIONFORYOURBEHAVIORTOWARDSMEITJUSTDOESNTMAKEANYSENSETHERESNOWAYTHATIDESERVEDTHETREATMENTYOUGAVEMEWITHOUTANEXPLANATIONORANAPOLOGYFORHOWOUTOFLINEYOUHAVEBEENDAVEFOUNDJOYINTHEDAILYROUTINEOFLIFEHEAWOKEATTHESAMETIMEATETHESAMEBREAKFASTANDDROVETHESAMECOMMUTEHEWORKEDATAJOBTHATNEVERSEEMEDTOCHANGEANDHEGOTHOMEATPMSHARPEVERYNIGHTITWASWHOHEHADBEENFORTHELASTTENYEARSANDHEHADNOIDEATHATWASALLABOUTTOCHANGESTRANDEDYESSHEWASNOWTHEFIRSTPERSONEVERTOLANDONVENUSBUTTHATWASOFLITTLECONSEQUENCEHERNAMEWOULDBEREADBYMILLIONSINSCHOOLASTHEFIRSTTOLANDHEREBUTTHATCELEBRITYWOULDNEVERACTUALLYBESEENBYHERSHELOOKEDATTHECONTROLPANELANDKNEWTHEREWASNOTHINGTHATWOULDEVERGETITBACKINTOWORKINGORDERSHEWASTHEFIRSTANDITWASNOTCLEARTHISWOULDALSOBEHERLA"

ciphertext = encipher(plaintext, period, key)
plaintext = decipher(ciphertext, period, key)
print(key)
print(ciphertext)
print(plaintext)
