#For darkroom level 2 have it so that the level you get depends on the password you enter
  
def abandonHope():
  f=open('abandonHope.txt','r+')
  AHList = []
  line=f.readline()
  while line:
    AHList.append(str(line))
    line=f.readline()
  f.close()

  print('\n'+AHList[0]+AHList[1])
  while True:
    print(GList[20]+AHList[14]+AHList[16]+AHList[17])
    aban = input(GList[3])+'\n'
    if aban==AHList[16]:
      findLightSwitch()
    elif aban==AHList[14]:
      print('\n'+AHList[2])
      while True:
        print(GList[20]+AHList[19]+AHList[17])
        murder = input(GList[3])+'\n'
        if murder==AHList[19]:
          print('\n'+AHList[5])
          while True:
            print(GList[20]+AHList[25])
            if input(GList[3])+'\n'==AHList[25]:
              print('\n'+AHList[6]+AHList[7])
              while True:
                print(GList[20]+AHList[20]+AHList[21]+AHList[22])
                naked = input(GList[3])+'\n'
                if naked==AHList[20]:
                  sitDown()
                elif naked==AHList[21]:
                  touchWall()
                elif naked==AHList[22]:
                  pray()
                else:
                  print(GList[4])
                  continue
            else:
              print(GList[4])
              continue
        elif murder==AHList[17]:
          while True:
            print('\n'+AHList[3]+AHList[4])
            print(GList[20]+AHList[26]+AHList[27]+AHList[28]+AHList[29])
            steal = input(GList[3])+'\n'
            if steal==AHList[26]:
              print('\n'+AHList[8])
              while True:
                print(GList[20]+AHList[25])
                if input(GList[3])+'\n'==AHList[25]:
                  darkRoom98()
                else:
                  print(GList[4])
                  continue
            elif steal==AHList[27]:
              print('\n'+AHList[9]+GList[0])
              quit()
            elif steal==AHList[28]:
              print('\n'+AHList[10]+AHList[11]+GList[0])
              quit()
            elif steal==AHList[29]:
              print('\n'+AHList[9]+GList[0])
              quit()
            else:
              print(GList[4])
              continue
        else:
          print(GList[4])
          continue
    elif aban==AHList[17]:
      print('\n'+AHList[3]+AHList[4])
      while True:
        print(GList[20]+AHList[26]+AHList[27]+AHList[28]+AHList[29])
        steal = input(GList[3])+'\n'
        if steal==AHList[26]:
          print('\n'+AHList[8])
          while True:
            print(GList[20]+AHList[25])
            if input(GList[3])+'\n'==AHList[25]:
              darkRoom98()
            else:
              print(GList[4])
              continue
        elif steal==AHList[27]:
          print('\n'+AHList[9]+GList[0])
          quit()
        elif steal==AHList[28]:
          print('\n'+AHList[10]+AHList[11]+GList[0])
          quit()
        elif steal==AHList[29]:
          print('\n'+AHList[9]+GList[0])
          quit()
        else:
          print(GList[4])
          continue
    else:
      print(GList[4])
      continue

def clickHeels():
  f=open('clickHeels.txt','r+')
  CHList = []
  line=f.readline()
  while line:
    CHList.append(str(line))
    line=f.readline()
  f.close()

  print('\n'+CHList[0]+CHList[1])
  while True:
    if input(' ')+'\n'==CHList[2]:
      print('\n'+CHList[3])
      break
    else:
      print(GList[4])
      continue
  counter=0
  while counter<2:
    if input('Again!\n')+'\n'==CHList[2]:
      counter+=1
    else:
      print(GList[4])
      continue
  print('\n'+CHList[4]+CHList[5]+GList[0])
  name='Comrade Darren'
  namecaps=str.upper(name)
  darkRoomLevel1()

def czechPockets():
  f=open('czechPockets.txt','r+')
  CPList = []
  line=f.readline()
  while line:
    CPList.append(str(line))
    line=f.readline()
  f.close()

  print(CPList[0])
  while True:
    kind = input(GList[20]+CPList[1] + '\n' + GList[3])
    if kind + '\n' == CPList[1]:    
      input('\n'+CPList[2]+CPList[3])
      darkRoomLevel1()
    else:
      print(GList[4])
      continue

def darkRoom98():
  f=open('darkRoom98.txt','r+')
  DR98List = []
  line=f.readline()
  while line:
    DR98List.append(str(line))
    line=f.readline()
  f.close()

  print('\n'+GList[20]+DR98List[0]+DR98List[1])
  while True:
    DR98 = input(GList[3]) +'\n'
    if DR98 == DR98List[0]:   
      sitDown() 
    elif DR98 == DR98List[1]:
      touchWall()
    else:
      print(GList[4])
      continue

def darkRoomLevel1():
  f=open('darkRoomLevel1.txt','r+')
  DRL1List = []
  line=f.readline()
  while line:
    DRL1List.append(str(line))
    line=f.readline()
  f.close()

  while True:
    print(namecaps+ ', ' +GList[1])
    print(GList[20]+DRL1List[0]+DRL1List[1]+DRL1List[2]+DRL1List[3])
    room = input(GList[3])+'\n'
    if room == DRL1List[0]:
      print('\n'+DRL1List[11])
      while True:
        print(GList[20]+DRL1List[1]+DRL1List[4]+DRL1List[5])
        why = input(GList[3])+'\n'
        if why == DRL1List[1]:
          print('\n'+GList[2])
          break
        elif why == DRL1List[4]:
          print('\n'+DRL1List[12])
          while True:
            print(DRL1List[13])
            print(GList[20]+DRL1List[6]+DRL1List[7]+DRL1List[2])
            on = input(GList[3])+'\n'
            if on == DRL1List[6]:
              while True:
                print('\n'+DRL1List[14])
                print(GList[20]+DRL1List[3]+DRL1List[1]+DRL1List[8])
                look = input(GList[3])+'\n'
                if look == DRL1List[3]:
                  findLightSwitch()
                elif look == DRL1List[1]:
                  print('\n'+GList[2]+GList[1])
                  while True:
                    print(GList[20]+DRL1List[5])
                    answer = input(GList[3])+'\n'
                    if answer == DRL1List[5]:
                      czechPockets()
                    else:
                      print(GList[4])
                      continue  
                elif look == DRL1List[8]:
                  print(DRL1List[15])
                  break
                else:
                  print(GList[4])
                  continue
            elif on == DRL1List[7]:
              withMyFinger()
            elif on == DRL1List[2]:
              northFD()
            else:
              print(GList[4])
              continue
            break
        elif why == DRL1List[5]:
          czechPockets()
        else:
          print(GList[4])
          continue
        break
    elif room == DRL1List[1]:
      print(GList[2])
      continue
    elif room == DRL1List[2]:
      goNorth()
    elif room == DRL1List[3]:
      findLightSwitch()
    else:
      print(GList[4])
      continue
    continue

def findLightSwitch():
  f=open('findLightSwitch.txt','r+')
  FLSList = []
  line=f.readline()
  while line:
    FLSList.append(str(line))
    line=f.readline()
  f.close()

  while True:
    print(FLSList[7])
    print(GList[20]+FLSList[0]+FLSList[1]+FLSList[2])
    see=input(GList[3])+'\n'
    if see == FLSList[0]:
      print('\n'+FLSList[8])
      while True:
        print(GList[20]+FLSList[4]+FLSList[5]+FLSList[2])
        do=input(GList[3])+'\n'
        if do == FLSList[4]:
          break
        elif do == FLSList[5]:
          touchWall()
        elif do == FLSList[2]:
          czechPockets()
        else:
          print(GList[4])
          continue
      continue    
    elif see == FLSList[1]:
      print('\n'+FLSList[9])
      continue
    elif see == FLSList[2]:
      czechPockets()
    else:
      print(GList[4])
      continue

def goNorth():
  f=open('goNorth.txt','r+')
  GNList = []
  line=f.readline()
  while line:
    GNList.append(str(line))
    line=f.readline()
  f.close()

  print(GNList[0]+'\n'+GNList[1]+'\n'+GNList[2]+GList[0])
  quit()

def northFD():
  f=open('northFD.txt','r+')
  NFDList = []
  line=f.readline()
  while line:
    NFDList.append(str(line))
    line=f.readline()
  f.close()

  print('\n'+NFDList[0]+NFDList[1])
  while True:
    print(GList[20]+NFDList[18]+NFDList[19]+NFDList[20]+NFDList[21])
    hope = input(GList[3])+"\n"
    if hope==NFDList[21]:
      findLightSwitch()
    elif hope==NFDList[20]:
      abandonHope()
    elif hope==NFDList[18]:
      print(NFDList[2])
      while True:
        print(GList[20]+NFDList[18]+NFDList[22]+NFDList[23]+NFDList[24])
        rhyme = input(GList[3])+'\n'
        if rhyme==NFDList[22]:
          print('\n'+NFDList[4]+GList[0])
          quit()
        elif rhyme==(NFDList[23]):
          print('\n'+NFDList[5]+GList[2]+GList[1]+NFDList[6])
          darkRoomLevel1()
        elif rhyme==(NFDList[18]):
          while True:
            print('\n'+GList[20]+NFDList[25])
            if input(NFDList[3])+'\n'==NFDList[25]:
              print('\n'+NFDList[16]+GList[0])
              quit()
            else:
              print(GList[4])
              continue
        elif rhyme==(NFDList[24]):
          print('\n'+NFDList[10])
          while True:
            print(GList[20]+NFDList[28])
            if input(NFDList[11])+'\n'==NFDList[28]:
              while True:
                print('\n'+GList[20]+NFDList[29])
                if input(NFDList[12])+'\n'==NFDList[29]:
                  while True:
                    print('\n'+GList[20]+NFDList[30])
                    if input(NFDList[13])+'\n'==NFDList[30]:
                      print(NFDList[14]+NFDList[15]+GList[2])
                      darkRoomLevel1()
                    else:
                      print(GList[4])
                      continue
                else:
                  print(GList[4])
                  continue
            else:
              print(GList[4])
              continue
        else:
          print(GList[4])
          continue
    elif hope==NFDList[19]:
      print('\n'+NFDList[7])
      while True:
        print(GList[20]+NFDList[26]+NFDList[21]+NFDList[27])
        hint = input(GList[3])+'\n'
        if hint==NFDList[26]:
          print('\n'+NFDList[9]+NFDList[10])
          while True:
            print(GList[20]+NFDList[27])
            if input(GList[3])+'\n'==NFDList[27]:
              clickHeels()
            else:
              print(GList[4])
              continue
        elif hint==NFDList[21]:
          findLightSwitch()
        elif hint==NFDList[27]:
          clickHeels()
        else:
          print(GList[4])
          continue
    else:
      print(GList[4])
      continue

def pray():
  f=open('pray.txt','r+')
  PList = []
  line=f.readline()
  while line:
    PList.append(str(line))
    line=f.readline()
  f.close()

  print(PList[6])
  while True:
    print(GList[20]+PList[0]+PList[1]+PList[2]+PList[3])
    prey = input(GList[3])+'\n'
    if prey == PList[0]:
      print('\n'+PList[11])
      while True:
        if input(PList[12])+'\n'==PList[4]:
          print('\n'+PList[13])
          while True:
            if input(PList[12])+'\n'==PList[4]:
              print('\n'+PList[14]+GList[1]+PList[15])
              quit()
            else:
              print(GList[4])
              continue
        else:
          print(GList[4])
          continue
    elif prey == PList[1]:
      print('\n'+PList[7]+PList[8]+GList[0])
      quit()
    elif prey == PList[2]:
      while True:
        print(PList[17]+'\n'*40)
        print(GList[20]+PList[2])
        if input(GList[3])+'\n'==PList[17]:
          quit()
        else:
          print(GList[4])
          continue
    elif prey == PList[3]:
      print('\n'+PList[9]+'\n'+GList[20]+PList[10])
      while True:
        if input(GList[3])+'\n'==PList[10]:
          findLightSwitch()
        else:
          print(PList[8]+GList[0])
          quit()
    else:
      print(GList[4])
      continue

def sitDown():
  f=open('sitDown.txt','r+')
  SDList = []
  line=f.readline()
  while line:
    SDList.append(str(line))
    line=f.readline()
  f.close()

  print('\n'+SDList[3]+SDList[4])
  while True:
    print(GList[20]+SDList[0]+SDList[1])
    sit=input(SDList[5])+'\n'
    if sit==SDList[0]:
      print('\n'+SDList[7]+GList[0]) 
      quit()
    elif sit==SDList[1]:
      print(SDList[9])
      while True:
        print('\n'*35+SDList[3]+SDList[4])
        print(GList[3])
        if input(SDList[8])+'\n'==SDList[9]:
          quit()
        else:
          print(GList[4])
          continue
    else:
      print(GList[4])
      continue

def smellRoom():
  f=open('smellRoom.txt','r+')
  SRList = []
  line=f.readline()
  while line:
    SRList.append(str(line))
    line=f.readline()
  f.close()

  print(SRList[0])
  while True:
    smell = input(GList[20]+SRList[1] + '\n' + GList[3])
    if smell + '\n' == SRList[1]:    
      print('\n'+SRList[2])
      print(GList[20]+SRList[3]+SRList[4])
      mum=input(GList[3])+'\n'
      while True:
        if mum == SRList[3]:
          weep()
        elif mum ==SRList[4]:
          abandonHope()
        else:
          print(GList[4])
          continue 
    else:
      print(GList[4])
      continue

def touchWall():
  f=open('touchWall.txt','r+')
  TWList = []
  line=f.readline()
  while line:
    TWList.append(str(line))
    line=f.readline()
  f.close()

  print(TWList[13])
  while True:
    if input(GList[20]+TWList[0]+'\n'+GList[3])+'\n' == TWList[0]:
      print('\n'+TWList[14])
      while True:
        print(GList[20]+TWList[1]+TWList[2])
        wall = input(GList[3])+'\n'
        if wall == TWList[1]:
          print('\n'+TWList[15])
          while True:
            print(GList[20]+TWList[5]+TWList[4])
            another = input(GList[3])+'\n'
            if another == TWList[5]:
              smellRoom()
            elif another == TWList[4]:
              print('\n'+TWList[17])
              while True:
                if input(GList[20]+TWList[10]+'\n'+GList[3])+'\n' == TWList[10]:
                  print('\n'+TWList[19])
                  while True:
                    print(GList[20]+TWList[3]+TWList[9]+TWList[11])
                    ksin = input(GList[3])+'\n'
                    if ksin == TWList[3]:
                      findLightSwitch()
                    elif ksin == TWList[9]:
                      goNorth()
                    elif ksin == TWList[11]:
                      pray()
                    else:
                      print(GList[4])
                      continue
                else:
                  print(GList[4])
                  continue
            else:
              print(GList[4])
              continue
        elif wall == TWList[2]:
          print('\n'+TWList[16])
          while True:
            print(GList[20]+TWList[3]+TWList[4]+TWList[5])
            apol = input(GList[3])+'\n'
            if apol == TWList[3]:
              findLightSwitch()
            elif apol == TWList[4]:
              print('\n'+TWList[17])
              while True:
                print(GList[20]+TWList[3]+TWList[8]+TWList[9]+TWList[6])
                sob = input(GList[3])+'\n'
                if sob == TWList[3]:
                  findLightSwitch()
                elif sob == TWList[8]:
                  czechPockets()
                elif sob == TWList[9]:
                  goNorth()
                elif sob == TWList[6]:
                  print('\n'+TWList[18])
                  while True:
                    if input(GList[20]+TWList[7] + '\n' +GList[3])+'\n' == TWList[7]:
                      darkRoom98()
                    else:
                      print(GList[4]) 
                      continue
                else:
                  print(GList[4])
                  continue
            elif apol == TWList[5]:
              smellRoom()
            else:
              print(GList[4])
              continue
        else:
          print(GList[4])
          continue
    else:
      print(GList[4])
      continue

def weep():
  f=open('weep.txt','r+')
  WList = []
  line=f.readline()
  while line:
    WList.append(str(line))
    line=f.readline()
  f.close()

  print(WList[5]+WList[6])
  while True:
    print(GList[20]+WList[0]+WList[1]+WList[2]+WList[3])
    wep = input(GList[3])+'\n'
    if wep == WList[0]:
      findLightSwitch
    elif wep == WList[1]:
      print('\n'+WList[8]+WList[16]+GList[0])
      quit()
    elif wep == WList[2]:
      print('\n'+WList[9])
      while True:
        print(WList[12])
        if input(GList[3])+'\n'==WList[12]:
          print('\n'+WList[13])
          while True:
            print(WList[14])
            if input(GList[3])+'\n'==WList[14]:
              print('\n'+GList[2])
              darkRoomLevel1()
            else:
              print(GList[4])
              continue
        else:
          print(GList[4])
          continue
    elif wep ==WList[3]:
      print(WList[10])
      darkRoom98()
    else:
      print(GList[4])
      continue

def withMyFinger():
  f=open('withMyFinger.txt','r+')
  WMFList = []
  line=f.readline()
  while line:
    WMFList.append(str(line))
    line=f.readline()
  f.close()

  print('\n'+WMFList[15])
  while True:
    print(GList[20]+WMFList[0]+WMFList[1]+WMFList[2])
    finger = input(WMFList[16])+'\n'
    if finger == WMFList[0]:  
      print('\n'+WMFList[17]+WMFList[18])
      while True:
        print(GList[20]+WMFList[3])
        radio = input(GList[3])+'\n'
        if radio == WMFList[3]:
          print('\n'+WMFList[19])
          while True:
            print(GList[20]+WMFList[4])
            if input(GList[3])+'\n'==WMFList[4]:
              print('\n'+WMFList[20])
              while True:
                print(GList[20]+WMFList[5])
                if input(GList[3])+'\n'==WMFList[5]:
                  print('\n'+WMFList[21]+GList[0])
                  quit()
                else:
                  print(GList[4])
                  continue
            else:
              print(GList[4])
              continue
        else:
          print(GList[4])
          continue
    elif finger == WMFList[1]:
      print('\n'+WMFList[29])
      while True:
        print(GList[20]+WMFList[7])
        if input(WMFList[30])+'\n'==WMFList[7]:
          print(WMFList[27])
          while True:
            print(GList[20]+WMFList[8]+WMFList[9]+WMFList[10]+WMFList[11])
            back = input(GList[3])+'\n'
            if back == WMFList[8]:
              print('\n'+WMFList[22]+GList[0])
              quit()
            elif back == WMFList[9]:
              print('\n'+WMFList[23]+GList[0])
              quit()
            elif back == WMFList[10]:
              print('\n'+WMFList[25])
              while True:
                print(GList[20]+WMFList[12]+WMFList[9]+WMFList[11])
                fore = input(GList[3])+'\n'
                if fore == WMFList[12]:
                  print('\n'+WMFList[24]+WMFList[22]+GList[0])
                  quit()
                elif fore == WMFList[9]:
                  print('\n'+WMFList[23]+GList[0]) 
                  quit()
                elif fore == WMFList[11]:
                  print('\n'+WMFList[26])
                  while True:
                    print(GList[20]+WMFList[11])
                    if input(GList[3])+'\n'==WMFList[11]:
                      print(WMFList[26])
                      continue
                    else:
                      print(GList[4])
                      continue
                else:
                  print(GList[4])
                  continue
            elif back == WMFList[11]:
              print('\n'+WMFList[26])
              while True:
                print(GList[20]+WMFList[11])
                if input(GList[3])+'\n'==WMFList[11]:
                  print(WMFList[26])
                  continue
                else:
                  print(GList[4])
                  continue
            else:
              print(GList[4])
              continue
        else:
          print(GList[4])
          continue
    elif finger == WMFList[2]:
      print('\n'+WMFList[28])
      while True:
        print(GList[20]+WMFList[6])
        cry = input(GList[3])+'\n'
        if cry == WMFList[6]:
          weep()
        else:
          print(GList[4])
          continue
    else:
      print(GList[4])
      continue



f=open('general.txt','r+')
GList = []
line=f.readline()
while line:
  GList.append(str(line))
  line=f.readline()
f.close()

print(GList[6] + GList[7])

name=input(GList[8])
if name !='Darren':
  if name =='Dolores':
    print(GList[9])
  
  elif name == 'abandonHope':
    abandonHope()
  elif name == 'clickHeels':
    clickHeels()
  elif name == 'czechPockets':
    czechPockets()
  elif name == 'darkRoom98':
    darkRoom98()
  elif name == 'findLightSwitch':
    findLightSwitch()
  elif name == 'goNorth':
    goNorth()
  elif name == 'northFD':
    northFD()
  elif name == 'pray':
    pray()
  elif name == 'sitDown':
    sitDown()
  elif name == 'smellRoom':
    smellRoom()
  elif name == 'touchWall':
    touchWall()
  elif name == 'weep':
    weep()
  elif name == 'withMyFinger':
    withMyFinger()

  print('\n'+GList[10])
  likename=input(GList[11])
  if likename == 'I liked Dolores':
    print(GList[12])
  else:
    print(GList[13])
elif name == 'Darren':
  print(' ')
name='Darren'
namecaps=str.upper(name)

while True:
  print(GList[20]+GList[16]+GList[17]+GList[18])
  level=input(GList[14])+'\n'
  if level == GList[16]:
    darkRoomLevel1()
  else:
    print(GList[4])
    continue

