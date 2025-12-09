#1
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))
#2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

print(*sorted([u['name'] for u in users if u['phone'].endswith('8')]))
#3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]


print(*sorted([u['name'] for u in users if not u.get('email')]))
#4
num = input()
d = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
print(*[d[c] for c in num])
#5
c = input()
d = {
    'CS101': ['3004','Хайнс','8:00'],
    'CS102': ['4501','Альварадо','9:00'],
    'CS103': ['6755','Рич','10:00'],
    'NT110': ['1244','Берк','11:00'],
    'CM241': ['1411','Ли','13:00']
}
a,b,t = d[c]
print(f"{c}: {a}, {b}, {t}")

#6
s = input().upper()
d = {
    **{c:'1'*i for i,c in enumerate(".,?!:",1)},
    **{c:'2'*i for i,c in enumerate("ABC",1)},
    **{c:'3'*i for i,c in enumerate("DEF",1)},
    **{c:'4'*i for i,c in enumerate("GHI",1)},
    **{c:'5'*i for i,c in enumerate("JKL",1)},
    **{c:'6'*i for i,c in enumerate("MNO",1)},
    **{c:'7'*i for i,c in enumerate("PQRS",1)},
    **{c:'8'*i for i,c in enumerate("TUV",1)},
    **{c:'9'*i for i,c in enumerate("WXYZ",1)},
    ' ':'0'
}
print(''.join(d[c] for c in s if c in d))

#7
s = input().upper()
d = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
     'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
     'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
     'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
     '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
print(' '.join(d[c] for c in s if c in d))

#8
result = {i: i*i for i in range(11,16)}

#9
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict1.copy()
for k,v in dict2.items():
    result[k] = result.get(k,0) + v

#10
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for c in text:
    result[c] = result.get(c,0) + 1

#11
d = {}
for w in s.split():
    d[w] = d.get(w,0) + 1
m = max(d.values())
print(sorted([k for k,v in d.items() if v==m])[0])

#12
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

for dog,name,sur,age in pets:
    key = (name,sur,age)
    if key not in result:
        result[key] = []
    result[key].append(dog)

#13
text = input().lower()

symbols = '.,!?:;-'
for s in symbols:
    text = text.replace(s, ' ')

words = text.split()

d = {}
for w in words:
    if w not in d:
        d[w] = 1
    else:
        d[w] += 1

min_count = min(d.values())

rare_words = []
for key in d:
    if d[key] == min_count:
        rare_words.append(key)

rare_words.sort()

print(rare_words[0])

#14
ids = input().split()
d = {}
res = []
for x in ids:
    if x not in d:
        d[x] = 0
        res.append(x)
    else:
        d[x] += 1
        res.append(f"{x}_{d[x]}")
print(*res)
