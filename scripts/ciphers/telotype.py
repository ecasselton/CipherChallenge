import cipherchallenge as cc

ciphertext = cc.get_ciphertext()

period = 5

symbols = "|\\/"

def encipher(plaintext, key):
    # Convert to \|/
    trigrams = []
    for char in plaintext:
        num = ord(char)-65
        ternary = []
        for i in (9, 3, 1):
            ternary.append(num // i)
            num %= i

        trigram = []
        for trit in ternary:
            trigram.append(symbols[trit])
        trigrams.append(trigram)

    ciphertext = ""
    key_index = 0
    for trigram in trigrams:
        swaps = key[key_index]
        for i in range(3):
            if swaps[i] and trigram[i] != '|':
                trigram[i] = '/' if trigram[i] == '\\' else '\\'
            ciphertext += trigram[i]
        key_index = (key_index + 1) % len(key)
    
    return ciphertext

def decipher(ciphertext, key):
    blocks = []
    key_index = 0
    for j in range(0, len(ciphertext), 3):
        blocks.append("")
        trigram = [sym for sym in ciphertext[j:j+3]]
        swaps = key[key_index]
        for i in range(3):
            if swaps[i] and trigram[i] != '|':
                trigram[i] = '/' if trigram[i] == '\\' else '\\'
            blocks[j//3] += trigram[i]
        key_index = (key_index + 1) % len(key)

    # Convert from \|/
    plaintext = ""
    for block in blocks:
        num = 0
        for i in range(3):
            num += symbols.index(block[i]) * 3**(2-i)

        char = chr(num+65)
        plaintext += char
    
    return plaintext

message = cc.remove_punctuation( "Stormi is a dog. She is dark grey and has long legs. Her eyes are expressive and are able to let her humans know what she is thinking. Her tongue is long, pink, and wet. Her long legs allow her to sprint after other dogs, people or bunnies. She can be a good dog, but also very bad. Her tail wags when happy or excited and hides between her back legs when she is bad. Stormi is a dog I love. There was a time when he would have embraced the change that was coming. In his youth, he sought adventure and the unknown, but that had been years ago. He wished he could go back and learn to find the excitement that came with change but it was useless. That curiosity had long left him to where he had come to loathe anything that put him out of his comfort zone. Pink ponies and purple giraffes roamed the field. Cotton candy grew from the ground as a chocolate river meandered off to the side. What looked like stones in the pasture were actually rock candy. Everything in her dream seemed to be perfect except for the fact that she had no mouth. The trees, therefore, must be such old and primitive techniques that they thought nothing of them, deeming them so inconsequential that even savages like us would know of them and not be suspicious. At that, they probably didn't have too much time after they detected us orbiting and intending to land. And if that were true, there could be only one place where their civilization was hidden. What was beyond the bend in the stream was unknown. Both were curious, but only one was brave enough to want to explore. That was the problem. There was always one that let fear rule her life. Are you getting my texts??? she texted to him. He glanced at it and chuckled under his breath. Of course he was getting them, but if he wasn't getting them, how would he ever be able to answer? He put the phone down and continued on his project. He was ignoring her texts and he planned to continue to do so. Josh had spent year and year accumulating the information. He knew it inside out and if there was ever anyone looking for an expert in the field, Josh would be the one to call. The problem was that there was nobody interested in the information besides him and he knew it. Years of information painstakingly memorized and sorted with not a sole giving even an ounce of interest in the topic. If you can imagine a furry humanoid seven feet tall, with the face of an intelligent gorilla and the braincase of a man, you'll have a rough idea of what they looked like -- except for their teeth. The canines would have fitted better in the face of a tiger, and showed at the corners of their wide, thin-lipped mouths, giving them an expression of ferocity. It's an unfortunate reality that we don't teach people how to make money (beyond getting a 9 to 5 job) as part of our education system. The truth is there are a lot of different, legitimate ways to make money. That doesn't mean they are easy and that you won't have to work hard to succeed, but it does mean that if you're willing to open your mind a bit you don't have to be stuck in an office from 9 to 5 for the next fifty years o your life. Begin today! That's all the note said. There was no indication from where it came or who may have written it. Had it been meant for someone else? Meghan looked around the room, but nobody made eye contact back. For a brief moment, she thought it might be a message for her to follow her dreams, but ultimately decided it was easier to ignore it as she crumpled it up and threw it away. She had been an angel for coming up on 10 years and in all that time nobody had told her this was possible. The fact that it could ever happen never even entered her mind. Yet there she stood, with the undeniable evidence sitting on the ground before her. Angels could lose their wings. Indescribable oppression, which seemed to generate in some unfamiliar part of her consciousness, filled her whole being with a vague anguish. It was like a shadow, like a mist passing across her soul's summer day. It was strange and unfamiliar; it was a mood. She did not sit there inwardly upbraiding her husband, lamenting at Fate, which had directed her footsteps to the path which they had taken. She was just having a good cry all to herself. The mosquitoes made merry over her, biting her firm, round arms and nipping at her bare insteps. The boxed moved. That was a problem. Peter had packed the box three hours before and there was nothing inside that should make it move. The question now was whether or not Peter was going to open it up and look inside to see why it had moved. The answer to that question was obvious. Peter dropped the package into the mailbox so he would never have to see it again. He knew what he was supposed to do. That had been apparent from the beginning. That was what made the choice so difficult. What he was supposed to do and what he would do were not the same. This would have been fine if he were willing to face the inevitable consequences, but he wasn't. I'm meant to be writing at this moment. What I mean is, I'm meant to be writing something else at this moment. The document I'm meant to be writing is, of course, open in another program on my computer and is patiently awaiting my attention. Yet here I am plonking down senseless sentiments in this paragraph because it's easier to do than to work on anything particularly meaningful. I am grateful for the distraction. ")

key = ((0,1,0),(1,1,1),(0,1,1),(1,1,0),(0,0,1),(0,1,1),(1,0,1))
print(decipher(encipher(message, key), key))
