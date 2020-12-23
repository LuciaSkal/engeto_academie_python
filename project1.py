# project 1 : Text Analyzer

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

ODDELOVAC = '-' * 50
uzivatele = {'bob': '123', 'ann': 'pass123',
                'mike': 'password123', 'liz': 'pass123'}
print(ODDELOVAC)
print(
    'WELCOME TO THE APP!'.center(50, ' '),
    ODDELOVAC,
    'Please log in...',
    sep='\n'
)

user = input('USERNAME: ')
password = input('PASSWORD: ')
print(ODDELOVAC)

if uzivatele.get(user) == password:
    print('ACCESS GRANTED')
else:
    print('ACCESS DENIED!')
    print('Incorrect password or username...')
    quit()
print(ODDELOVAC)
print(ODDELOVAC)

print(('We have 3 texts to be analyzed').center(50, ' '))
print(ODDELOVAC)

vyber = int(input('Enter a number 1,2,3 to select text: '))
if vyber not in (1, 2, 3,):
    print('INCORRECT NUMBER!')
    quit()
print(ODDELOVAC)

text = TEXTS[vyber - 1]

ciste_slova = text.split()
slova = []
while ciste_slova:
    slovo = ciste_slova.pop().strip('.,:/;')
    if slovo:
        slova.append(slovo)
print(f'There are {(len(slova))} words in the selected text.')

titlecase = 0
lowercase = 0
uppercase = 0
numeric = []
suma_numeric = 0

for slovo in slova:
    if slovo.istitle():
        titlecase += 1
    elif slovo.islower():
        lowercase +=1
    elif slovo.isupper():
        uppercase += 1
    elif slovo.isnumeric():
        numeric.append(slovo)

for cislo in numeric:
    if cislo.isdigit():
        suma_numeric += int(cislo)

print(f'There are {titlecase} titlecase words.')
print(f'There are {uppercase} uppercase words.')
print(f'There are {lowercase} lowercase words.')
print(f'There are {len(numeric)} numeric strings.')
print(ODDELOVAC)

print(('BAR CHART OF WORDS LENGHTS ').center(50, ' '))
print(ODDELOVAC)

spolu = {}
for slovo in slova:
    delka = len(slovo)
    if delka not in spolu:
        spolu[delka] = 1
    else:
        spolu[delka] += 1
sd = sorted(spolu.items())
for sl, frekv in sd:
    print(sl, ('*' * frekv), frekv)


print('-' * 63)
print(f'If we summed all the numbers in this text we would get: {suma_numeric}')
print('-' * 63)
print('THANK YOU FOR USSING THIS APP'.center(63, ' '))

