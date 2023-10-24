import random


argentinaNum = round(random.random() * 100 ,2)
australiaNum = round(random.random() * 100 ,2)
arabiaNum = round(random.random() * 100 ,2)
africaNum = round(random.random() * 100 ,2)
brazilNum = round(random.random() * 100 ,2)
canadaNum = round(random.random() * 100 ,2)
chinaNum = round(random.random() * 100 ,2)
franceNum = round(random.random() * 100 ,2)
germanyNum = round(random.random() * 100 ,2)
indiaNum = round(random.random() * 100 ,2)
indonesiaNum = round(random.random() * 100 ,2)
italyNum = round(random.random() * 100 ,2)
japanNum = round(random.random() * 100 ,2)
koreaNum = round(random.random() * 100 ,2)
mexicoNum = round(random.random() * 100 ,2)
russiaNum = round(random.random() * 100 ,2)
turkeyNum = round(random.random() * 100 ,2)
unitedKingdomNum = round(random.random() * 100 ,2)
unitedStatesNum = round(random.random() * 100 ,2)

class myColors :
            
	ResetAll = "\033[0m"
        
	LightRed     = "\033[91m"
	LightGreen   = "\033[92m"
	LightYellow  = "\033[93m"
	LightBlue    = "\033[94m"
	LightMagenta = "\033[95m"
	LightCyan    = "\033[96m"

countryList = ["Argentina", "Australia", "Brazil", "Canada", "China", "France", "Germany", 
"India", "Indonesia", "Italy", "Japan", "Republic of Korea", "Mexico", "Russia", 
"Saudi Arabia", "South Africa", "Türkiye", "United Kingdom", "United States"]

gender = ["Male","Female"]

class Country:
  def __init__(p, gender,  language, religion, skill, racial, special):
    p.gender = gender
    p.language = language
    p.religion = religion
    p.skill = skill
    p.racial = racial
    p.special = special
  
  def __str__(p):
    return f"{p.gender},{p.language},{p.religion},{p.skill},{p.racial},{p.special}"  

if argentinaNum > 52.83:
    argentinaGender = gender[0]
else:
    argentinaGender = gender[1]

if argentinaNum > 0.5:
    argentinaLanguage = "Spanish"
else:
    argentinaLanguage = "Guarani and Quechua"

if 58.9 > argentinaNum:
    argentinaReligion = "Christian"
elif 98.7 > argentinaNum > 58.9:
    argentinaReligion = "No Religion"
else:
    argentinaReligion = "Jewish"

if 85 > argentinaNum:
    argentinaRacial = "Criollo people"
elif 86 > argentinaNum > 85:
    argentinaRacial = "Amerindians"
elif 88.9 > argentinaNum > 86:
    argentinaRacial = "Asian"
else:
    argentinaRacial = "Mestizo"


Argentina = Country(argentinaGender,argentinaLanguage,argentinaReligion,"selecter skill",argentinaRacial,"iyi bir insan ozelligimi kotumu diye bir liste yap")

print(Argentina)