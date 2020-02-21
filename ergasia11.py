
with open('tetrades.txt') as f: #Den esteila to arxeio gia na balete eseis sto arxeio tis diathesimes tetrades pou thelete
    x = [] # LIsta me tetrades sto arxeio .txt (tha prepei oi tetrades na einai mia ana grammi)
    for line in f:
        line = line.split()  # Den symperilambanei ta \n 
        if line:            
            line = [int(j) for j in line]
          
            x.append(line)
print('Dwse 6 arithmous apto 1 ews to 9!')
exada=[] # lista me toys arithmous tis eksadas
for i in range(1,7):
 h= input("")
 exada.append(h)
b = [] # Gia paradeigma b[0]-b[3] einai i prwti tetrada 
a = len(x)
for k in x:
  z = str(k)
  z = z[1:-1]
  for psifio in z:
    b.append(psifio)
counter = 0  
diakopi = 0     # Tha xrisimopoiithei gia na stamatisoun oi elegxoi afou brethei tetrada
for arithmoi in range(0,a*4,4): # Elegxei an oi 4 prwtoi arithmoi protimisis dinoun tetrada 
  counter = 0
  for i in range (arithmoi,arithmoi+4):
    for n in range (0,4):
      if (exada[n]==b[i]):

        counter = counter + 1
      else:
        counter = counter
  if (counter==4):
    print("H τετραδα σου ειναι η:"+b[arithmoi]+","+b[arithmoi+1]+","+b[arithmoi+2]+","+b[arithmoi+3])
    diakopi = 1
if (diakopi==0): # Elegxei an oi 3 prwtoi arithmoi protimisis tairiazoun me kapoion apo mia tetrada  kai ystera dokimazei ton 5o kai to 60 arithmo
  
  for arithmoi in range(0,a*4,4):    
    counter = 0
    for i in range (arithmoi,arithmoi+4):
      for n in range (0,4):
        if (exada[n]==b[i]):
          counter = counter + 1
        else:
          counter = counter
    if (counter==3 and exada[3]!=b[arithmoi] and exada[3]!=b[arithmoi+1] and exada[3]!=b[arithmoi+2] and exada[3]!=b[arithmoi+3]):
      for m in range (arithmoi,arithmoi+4):
        for n in range (4,6):
          if (exada[n]==b[m] and diakopi!=999):
            print("H tetrada sou einai h:"+c[arithmoi]+","+c[arithmoi+1]+","+c[arithmoi+2]+","+c[arithmoi+3])
            diakopi = 1
#Den iksera na kanw tous ypoloipous elegxous alla i idea einai ayti
if (diakopi==0): # Afou teliwsoun oi elegxoi kai den yparxei diathesimi tetrada
  print("Den yparxei diathesimi eleythera")


