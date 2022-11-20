DATA = []

# M asse Kg
# L ongeur m
# T emps s
# I intensite de courant Ampere A
# O (omega) temperature Kelvin
# N quantite de matiere mol
# J intensite lumineuse candela en cd

# 30 char taille de l'ecran en largeur 
# majuscule => lettre seul
# nom_de_la_grandeur (abreviation)unite
DATA.append([[0,0,0,0,0,0,0],"rien"])
DATA.append([[1,0,0,0,0,0,0],"masse (kg)Kg"])
DATA.append([[0,1,0,0,0,0,0],"longueur (m)"])
DATA.append([[0,0,1,0,0,0,0],"temps (s)"])
DATA.append([[0,0,0,1,0,0,0],"intensite (A)"])
DATA.append([[0,0,0,0,1,0,0],"temperature (k0)"])
DATA.append([[0,0,0,0,0,1,0],"quantite de matière (n)mol"])
DATA.append([[0,0,0,0,0,0,1],"intensite lumineuse (cn)candela"])
DATA.append([[0,1,-1,0,0,0,0],"vitesse (v-)"])
DATA.append([[0,1,-2,0,0,0,0],"acceleration (a-)"])
DATA.append([[0,3,0,0,0,0,0],"volume (vo)"])
DATA.append([[0,2,0,0,0,0,0],"surface (su)"])
DATA.append([[0,0,-1,0,0,0,0],"frequence (hz)"])
DATA.append([[1,-1,-2,0,0,0,0],"pression (pa)pascal"])
DATA.append([[1,-3,0,0,0,0,0],"masse volumique (mv)"])
DATA.append([[1,2,-2,0,0,0,0],"energie (J)joule"])
DATA.append([[1,1,-1,0,0,0,0],"quantite de mouvement (qm)"])
DATA.append([[1,2,-1,0,0,0,0],"moment angulaire (ma)"])
DATA.append([[1,2,-3,0,0,0,0],"puissance (W)watt"])
DATA.append([[1,1,-2,0,0,0,0],"force (N)newton"])
DATA.append([[1,2,-2,0,0,0,0],"couple (co)joule"])
DATA.append([[1,2,-2,0,0,0,0],"enthalpie (H)joule"])
DATA.append([[1,2,-2,0,-1,0,0],"entropie (S)"])
DATA.append([[1,2,-3,-1,0,0,0],"potentiel electrique (U)volt"])
DATA.append([[0,0,1,1,0,0,0],"charge electrique (q)coulomb"])
DATA.append([[0,-2,0,1,0,0,0],"densite volumique de courant (j)"])
DATA.append([[0,-3,1,1,0,0,0],"densite volumique de charge (p)"])
DATA.append([[0,2,0,1,0,0,0],"moment magnetique (m-)"])
DATA.append([[1,1,-3,-1,0,0,0],"champ electrique (E-)"])
DATA.append([[1,0,-2,-1,0,0,0],"champ magnetique (B-)"])
DATA.append([[-1,-3,3,2,0,0,0],"conductivite electrique (ga)siemens/metre"])
DATA.append([[1,2,-3,-2,0,0,0],"resistance (R)"])
DATA.append([[1,2,-2,-2,0,0,0],"inductance (he)henry"])
DATA.append([[-1,-2,3,2,0,0,0],"admittance (si)siemens"])
DATA.append([[-1,-2,4,2,0,0,0],"capacite (C)farad"])
DATA.append([[-1,-3,4,2,0,0,0],"permittivite dielectrique (ep)farad/metre"])
DATA.append([[1,2,-2,0,-1,-1,0],"cte universelle des gaz parfaits (K)"])
DATA.append([[1,1,-2,-2,0,0,0],"permeabilite (mu)"])
DATA.append([[1,2,-3,-2,0,0,0],"impedance (Z)"])
DATA.append([[1,2,-1,0,0,0,0],"cte de planck (h)joule/seconde"])
DATA.append([[1,2,-2,0,-1,0,0],"cte de boltzmann (kb)"])
DATA.append([[1,3,-4,-2,0,0,0],"cte de coulomb (kc)"])
DATA.append([[1,2,-2,-1,0,0,0],"flux magnetique (fm)"])
DATA.append([[1,3,-3,-1,0,0,0],"flux electrique (fe)"])
DATA.append([[-1,3,-2,0,0,0,0],"cte gravitationnelle (G)"])
DATA.append([[0,-3,0,0,0,1,0],"concentration (M)mol/litre"])
DATA.append([[0,3,0,0,0,0,0],"litre (L)"])
DATA.append([[2,1,-5,-2,0,0,0],"vecteur de poynting (pi-)"])
DATA.append([[0,-1,0,0,0,0,0],"divergent (dv)"])
DATA.append([[0,-1,0,0,0,0,0],"rotationnel (ro)"])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])
#DATA.append([[0,0,0,0,0,0,0],""])

def affiche(tab):
	print()
	print("Kg",tab[0]," m",tab[1]," s",tab[2]," A",tab[3])
	print("k",tab[4]," mol",tab[5]," j",tab[6])
	print()
	for i in range(len(DATA)):
		if tab == DATA[i][0]:
			cc = "->" + DATA[i][1]
			printt(cc)

def printt(txt):
	L = [""]
	ct = 0
	i=0
	for char in txt:
		ct += 1
		if ct == 29:
			L.append("")
			i+=1
		L[i] = L[i] + char
	for k in range(i+1):
		print(L[k])
def inp_int(txt):
	while True:
		try:
			return int(input(txt))
		except:
			print("erreur")
def inp_str(txt):
	while True:
		try:
			return str(input(txt))
		except:
			print("erreur")

def change(L,n,p):
	for i in range(p):
		if L[i] < n-1:
			L[i] += 1
			break
		else:
			if i == p-1:
				return None
			L[i] = 0
	return L



aff = []
CAL = [0,0,0,0,0,0,0]

print("affichage : 1")
print("reset : 0")
print("exit : -1")
print("equation : 2")
while True:
	print("==============================")
	print()
	cha = inp_str("main->")
	if cha == '-1':
		break
	if cha == '1':
		affiche(CAL)	
	elif cha == '0':
		affiche(CAL)
		CAL = [0,0,0,0,0,0,0]
	elif cha == '2':
		G = []

		limite = inp_int("limite->")
		sel2 = 0
		while True:
			fa = inp_str("recherche_2->")
			if fa == '1':
				break
			res = 0
			sav = 0
			for i in range(len(DATA)):
				if fa in DATA[i][1]:
					printt(DATA[i][1])
					print("-> ",i)
					print()
					res+=1
					sav = i
			if res > 1:
				sel2 = inp_int("select->")
				if sel2 == -1:
					break
			elif res == 1:
				sel2 = sav
			if res > 0:
				G.append([sel2,DATA[sel2][0].copy()])
		size = len(G)
		
		L = [0 for _ in range(size)]
		while True:
			
			L = change(L,2*limite,size)
			if L == None:
				break
			flag = True
			for gran in range(7):
				som = 0
				for k in range(size):
					som += G[k][1][gran]*(L[k]-limite)
				if som != 0:
					flag = False
					break
			if flag:
				print()
				for i in range(size):
					printt(DATA[G[i][0]][1])
					print(L[i] - limite)
				

				break


	else:
		res = 0
		sav = 0
		for i in range(len(DATA)):
			if cha in DATA[i][1]:
				printt(DATA[i][1])
				print("-> ",i)
				print()
				res+=1
				sav = i
		if res > 0:
			if res > 1:
				sel = inp_int("select->")
			else:
				sel = sav
			if sel != -1:
				print("------------------------------")
				print()
				exp = inp_int("exp->")
				for i in range(7):
					CAL[i] += (DATA[sel][0][i]*exp)


