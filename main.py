import sys
import time
def writetohidg0(str): # Easy way to use as a library
    presskeys(getvalueofstr(str))
def presskeys(memkey): # list
    for i in memkey:
        if type(i)==type(0.0):
            time.sleep(i)
        else:
            with open('/dev/hidg0','rb+') as hidg:
                hidg.write(i.encode())
def readconfig(config): # see example.conf
    file=[]
    with open(config) as f:
        for line in f:
            file.append(line)
    return file
repeatnextcommand=1
def getvaluesofstr(string):
    keys={'a': 4, 'b': 5, 'c': 6, 'd': 7, 'e': 8, 'f': 9, 'g': 10, 'h': 11, 'i': 12, 'j': 13, 'k': 14, 'l': 15, 'm': 16, 'n': 17, 'o': 18, 'p': 19, 'q': 20, 'r': 21, 's': 22, 't': 23, 'u': 24, 'v': 25,'w':26,'x':27,'y':28,'z':29,'1':30,'2':31,'3':32,'4':33,'5':34,'6':35,'7':36,'8':37,'9':38,'0':39, ' ':44,'-':45,'=':46,'[':47,']':48,'\':49,";":51,''':52,',':54,'.':55}
    combokeys={'A': (4, 225), 'B': (5, 225), 'C': (6, 225), 'D': (7, 225), 'E': (8, 225), 'F': (9, 225), 'G': (10, 225), 'H': (11, 225), 'I': (12, 225), 'J': (13, 225), 'K': (14, 225), 'L': (15, 225), 'M': (16, 225), 'N': (17,225),'O':(18,225), 'P': (19, 225), 'Q': (20, 225), 'R': (21, 225), 'S': (22, 225), 'T': (23, 225), 'U': (24, 225), 'V': (25, 225), 'W': (26, 225), 'X': (27, 225), 'Y': (28, 225), 'Z': (29, 225),'!':(30,225),'@':(31,225),'#':(32,225),'$':(33,225),'%':(34,225),'^':(35,225),'&':(36,225),'*':(37,225),'(':(38,225),')':(39,225),'_':(45,225),'+':(46,225),'{':(47,225),'}':(48,225),':':(51,225),'"':(52,225),'<':(54,225),'>':(55,225),'?':(56,225)}
    specialkeys={'ENTER':40,'GUI':227,'ESC':41, 'TAB':43,'ALT':226,'CTRL':224,'F1':58,'F2':59,'F3':60,'F4':61,'F5':62,'F6':63,'F7':64,'F8':65,'F9':66,'F10':67,'F11':68,'F12':69,'PS':70,'SL':71,'INS':73,'HM':74,'PU':75,'PD':78,'END':77,'RIGHT':79,'LEFT':80,'DOWN':81,'UP':82}
    NULL_CHAR = chr(0)
    output=[]
    command=string.split()[0]
    string=string.split()[1:]
    if command=='BUTTON':
        for amountrepeat in range(repeatnextcommand):
            for i in string:
                onereport=''
                if i in specialkeys:
                    onereport+=NULL_CHAR+chr(specialkeys[i])
                else:
                    onereport+=NULL_CHAR+chr(keys[i.lower()])
                while len(onereport)!=8:
                    onereport+=NULL_CHAR
                output.append(onereport)
                output.append(NULL_CHAR*8)
        global repeatnextcommand
        repeatnextcommand=1
    elif command=='STRING':
        for amountrepeat in range(repeatnextcommand):
            for i in string:
                for j in i:
                    onereport=''
                    if j in keys:
                        onereport+=NULL_CHAR+chr(keys[j])
                    else:
                        for k in combokeys[j]:
                            onereport+=NULL_CHAR+chr(k)
                    while len(onereport)!=8:
                        onereport+=NULL_CHAR
                    output.append(onereport)
                    output.append(NULL_CHAR*8)
        global repeatnextcommand
        repeatnextcommand=1
    elif command=='SLEEP':
        output.append(float(int(string[0])*repeatnextcommand/100))
        global repeatnextcommand
        repeatnextcommand=1
    elif command=='REPEAT':
        global repeatnextcommand
        repeatnextcommand=int(string[0])
    return output
if __name__ == '__main__':
    for i in readconfig(sys.argv[-1]):
        presskeys(getvaluesofstr(i))
