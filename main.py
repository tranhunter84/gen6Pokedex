#lists to store all the pokemon's data
name=[]
type1=[]
type2=[]
total=[]
hp=[]
attack=[]
defense=[]
sAtk=[]
sDef=[]
speed=[]
generation=[]
legendary=[]

import time

#creates an array for all pokemon data separating VIA commas
#sorts the data into respective lists
def getData():
    text_file=open("folderPath+pokemonDatabase.txt", "r")
    lines=text_file.read().split(',')
    text_file.close()

    lineNum=len(lines)
#variable to specify index of 'lines' array and iterate through the array
    i=0

#variables to specify list indexes
    nameNum=0
    type1Num=0
    type2Num=0
    totalNum=0
    hpNum=0
    attackNum=0
    defenseNum=0
    sAtkNum=0
    sDefNum=0
    speedNum=0
    generationNum=0
    legendaryNum=0

#determines which list to add each 'lines' item into
#sorts and moves everything from the 'lines' array into the lists
    for i in range(lineNum):
        if i==(13+(nameNum*12)): 
            name.append(lines[i])
            nameNum+=1
        elif i==(14+(type1Num*12)): 
            type1.append(lines[i])
            type1Num+=1
        elif i==(15+(type2Num*12)):
            type2.append(lines[i])
            type2Num+=1
        elif i==(16+(totalNum*12)):
            total.append(lines[i])
            totalNum+=1
        elif i==(17+(hpNum*12)):
            hp.append(lines[i])
            hpNum+=1
        elif i==(18+(attackNum*12)):
            attack.append(lines[i])
            attackNum+=1        
        elif i==(19+(defenseNum*12)):
            defense.append(lines[i])
            defenseNum+=1
        elif i==(20+(sAtkNum*12)):
            sAtk.append(lines[i])
            sAtkNum+=1
        elif i==(21+(sDefNum*12)):
            sDef.append(lines[i])
            sDefNum+=1
        elif i==(22+(speedNum*12)):
            speed.append(lines[i])
            speedNum+=1         
        elif i==(23+(generationNum*12)):
            generation.append(lines[i])
            generationNum+=1
        elif i==(24+(legendaryNum*12)):
            legendary.append(lines[i])
            legendaryNum+=1   
#loop ends when all items have been moved into the lists
        elif i==9612:
            break
#moves on to the next item in the list for every iteration of the loop
        i+=1

#calling getData() function
getData()

#lets user search for a pokemon
search=input('Enter a Pokemon Name. ')
searchLength=len(search)
upper=search.upper()
lower=search.lower()
search=upper[0]+lower[1:(searchLength)]
print(search)

#ends program if user does not provide valid pokemon name
if search not in name:
    print('Sorry, I could not find data on that Pokemon.')
#returns the index of the provided pokemon name in list names
#value is set equal to variable 'number'
else:
    number=name.index(search)

#function that finds and provides the data for the pokemon of the determined index
    def printData():
        print('Getting data for '+search+'...')
        time.sleep(2)
        print('[Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation]')
        print('['+name[number]+','+type1[number]+','+type2[number]+','+total[number]+','+hp[number]+','+attack[number]+','+defense[number]+','+sAtk[number]+','+sDef[number]+','+speed[number]+','+generation[number]+']')#','+legendary[number]+']')

#calling printData() function
    printData()
