file = open('4-1-In.txt', 'r') 
passwords = []
currPassword = ""
valPass = 0
passlist = []
char = ''
validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
currPassGood = True
currPass = []
currEntry = ""

while 1: 
    char = file.read(1)          
    if not char:  
        break
    if char == ',':
        passwords.append(currPassword)
        print("Password =",currPassword)
        currPassword = ""
    else:
        currPassword += char

for password in passwords:
    if password.count("byr:") and password.count("iyr:") and password.count("eyr:") and password.count("hgt:") and password.count("hcl:") and password.count("ecl:") and password.count("pid:"):
        #print("sb space", password[password.index(byr):password[password.index(byr)+4])
        passlist = password.split(" ")
        print(passlist)
        for x in xrange(len(passlist)):
            currPass = passlist
            currEntry = currPass[x]
            print(currEntry)
            if "byr" in currEntry:
                #print("byr", currEntry[currEntry.index(":")+1:])

                if int(currEntry[currEntry.index(":")+1:]) > 2002 or int(currEntry[currEntry.index(":")+1:]) < 1920:
                    currPassGood = False

            if "iyr" in currEntry:
                #print("iyr",currEntry[currEntry.index(":")+1:])

                if int(currEntry[currEntry.index(":")+1:]) > 2020 or int(currEntry[currEntry.index(":")+1:]) < 2010:
                    currPassGood = False

            if "eyr" in currEntry:
                #print("eyr",currEntry[currEntry.index(":")+1:])

                if int(currEntry[currEntry.index(":")+1:]) < 2020 or int(currEntry[currEntry.index(":")+1:]) > 2030:
                    currPassGood = False

            if "hgt" in currEntry:
                #print("hgt",currEntry[currEntry.index(":")+1:len(currEntry)-2])
                if "in" in currEntry:
                    if int(currEntry[currEntry.index(":")+1:len(currEntry)-2]) < 59 or int(currEntry[currEntry.index(":")+1:len(currEntry)-2]) > 76:
                        currPassGood = False
                if "cm" in currEntry:
                    if int(currEntry[currEntry.index(":")+1:len(currEntry)-2]) < 150 or int(currEntry[currEntry.index(":")+1:len(currEntry)-2]) > 193:
                        currPassGood = False

            if "hcl" in currEntry:
                print("hcl",currEntry[currEntry.index(":")+1:])
                for z in xrange(currEntry.index(":")+1, len(currEntry)):
                    if len(currEntry) != 11 or (currEntry[z].isdigit() == False and currEntry[z] != '#' and currEntry[z] != 'a' and currEntry[z] != 'b' and currEntry[z] != 'c' and currEntry[z] != 'd' and currEntry[z] != 'e' and currEntry[z] != 'f'):
                        currPassGood = False

            if "ecl" in currEntry:
                #print("ecl",currEntry[currEntry.index(":")+1:])
                if currEntry[currEntry.index(":")+1:] not in validEyeColors:
                    currPassGood = False

            if "pid" in currEntry:
                #print("pid",currEntry[currEntry.index(":")+1:])
                for z in xrange(currEntry.index(":")+1, len(currEntry)):
                    if currEntry[z].isdigit() == False or len(currEntry) != 13:
                        currPassGood = False
            
    else:
        currPassGood = False

    if currPassGood == True:
        print("Good")
        valPass += 1
    currPassGood = True


print("Valid Passwords = ",valPass)    
