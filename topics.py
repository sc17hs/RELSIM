topics = []
quran = ['allah', 'people', 'lord', 'messenger', 'surely', 'believe', 'day', 'believer', 'earth', 'chastisement',
         'truth', 'prophet', 'sign', 'heaven', 'fear', 'indeed', 'heart', 'world', 'deed', 'unbeliever', 'evil',
         'life', 'fire', 'moses', 'whatever', 'sent', 'reward', 'faith', 'god', 'follow', 'lie', 'created', 'knowledge',
         'witness', 'none', 'forth', 'cause', 'revealed', 'tell', 'prayer', 'nothing', 'favour', 'deny', 'jinni', 'call',
         'power', 'mercy', 'twain', '"except"', 'hand', 'garden', 'set', 'bring', 'servant', 'night', 'joseph', 'muhammad',
         'woman', 'time', 'seek', 'guidance', 'worship', 'true', 'verily', 'righteous', 'child', 'pharaoh', 'forgive', 'heed',
         'nay', 'sin', 'noah', 'moon', 'abraham', 'angel', 'water', 'hell', 'bestowed', 'eye', 'quran']

bible = ['lord', 'son', 'god', 'king', 'day', 'child', 'father', 'israel', 'people', 'offering', 'hand', 'house', 'servant',
         'city', 'david', 'heart', 'land', 'jesus', 'saying', 'word', 'love', 'behold', 'hundred', 'time', 'name', 'judah',
         'amongst', 'jerusalem', 'moses', 'forever', 'altar', 'holy', 'priest', 'egypt', 'commanded', 'woman', 'sin', 'sea',
         'water', 'sent', 'called', 'brother', 'earth', 'spirit', 'heard', 'set', 'brought', 'nation', 'army', 'prophet', 'law',
         'daniel', 'gold', 'life', 'heaven', 'soul', 'tent', 'eye', 'spoke', 'gate', 'cubit', 'blood', 'enemy', 'eat', 'fire',
         'thousand', 'voice', 'body', 'righteousness', 'righteous', 'glory', 'head', 'burnt', 'saul', 'answered', 'mountain', 'daughter',
         'wife', 'jew', 'faith', 'evil', 'flesh', 'lamb', 'seven', 'world', 'christ', 'stone', 'multitude', 'kingdom', 'wisdom', 'iniquity',
         'friend', 'jacob', 'covenant', 'drink', 'tree', 'lamp', 'philistine']

shared  = []
print("Quran topics: ", quran)
print("Bible topics: ", bible)
print("Quran unique topics: ", len(quran))
print("Bible unique topics: ", len(bible))

crossover = 0
for x in quran:
    for z in bible:
        if x == z:
            crossover = crossover +1
            shared.append(x)
    else:
        pass
    
print("The crossover in the two sets: ", crossover)
print("The shared topics are: ",shared)
