davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim',
    'Niderland':"	Amsterdam",
    "Andorra":"  	Andorra-la-Velya",
    "Yunoniston":"	Afina",
    "Serbiya":"	Belgrad",
    "Germaniya":"	Berlin",
    "Shveysariya":"	Bern",
    "Slovakiya":"	Bratislava",
    "Belgiya":"	Brussel",
    "Mojariston":"	Budapesht",
    "Ruminiya":"	Buxarest",
    "Irlandiya":"	Dublin",
    "Ukraina":"	Kiyev",
    "Moldova":"	Kishinyov",
    "Daniya":"	Kopengagen",
    "Portugaliya":"	Lissabon",
    "Byuk Britaniya":"	London",
    "Sloveniya":"	Lyublyana",
    "Lyuksemburg":"	Lyuksemburg",
    "Ispaniya":"Madrid",
    "Belarus":"	Minsk",
    "Monako":"	Monako",
    "Rossiya":"	Moskva",
    "Norvegiya":"	Oslo",
    "Fransiya":"	Parij",
    "Chexiya":"	Praga",
    "Islandiya":"	Reykyavik",
    "Latviya":"	Riga",
    "Italiya":"	Rim",
    "San Marino	":"San-Marino",
    "Gertsogovina":"	Sarayevo",
    "Makedoniya":"	Skopye",
    "Bolgariya":"	Sofiya",
    "Shvetsiya":"	Stokgolm",
    "Estoniya":"	Tallin",
    "Albaniya":"	Tirana",
    "Lixtenshteyn":"	Vaduts",
    "Malta	":"Valletta",
    "Polsha":"	Varshava",
    "Vatikan":"	Vatikan",
    "Avstriya":"	Vena",
    "Litva":"	Vilnyus",
    "Finlandiya":"	Helsinki",
    "Xorvatiya":"	Zagreb",
    "Malta ordeni":"	Malta qasri*",
    "Chernogoriya":"	Podgoritsa/Setine*[1]",
    "Kosovo[2]":"	Prishtina*",
    "Transnistria[3]":"	Tiraspol*"}

#print('Dunyo davlatlari:')
#for davlat in sorted(davlatlar):
    #print(davlat.upper())

#print('\nDavlatlarning poytaxtlari')
#for poytaxt in sorted(davlatlar.values()):
 #   print(poytaxt.title())

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:\n >>>')
capital = davlatlar.get(country)
if country in davlatlar:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
else:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
