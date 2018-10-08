werkgever = raw_input("Naam werkgever: ")
nettoloon_fulltime = raw_input("Nettoloon fulltime (40 uur): ")
werkuren = raw_input("Aantal werkuren per week: ")

#bereken werkelijke nettomaandloon bij werkelijk aantal uren
nettoloon_real = float(nettoloon_fulltime) / 40 * int(werkuren)
print "Bij " + str(werkuren) + " werkuren per week, verdien je " + str(nettoloon_real) + " per maand."

reiskostenvergoeding = raw_input("Reiskostenvergoeding per maand: ")
loonincreis = float(nettoloon_real) + float(reiskostenvergoeding)
print "Loon en reiskostenvergoeding per maand is " + str(loonincreis)

aantal_maanden_werk = raw_input("Aantal maanden dat je hier gaat werken: ")
loonxmaanden = float(loonincreis) * float(aantal_maanden_werk)
print "Voor " + str(aantal_maanden_werk) + " maanden werk, ontvang je " + str(loonxmaanden)

vakantiegeld = raw_input("Te ontvangen vakantiegeld over deze periode: ")
dertiende_maand = raw_input("Bedrag evt. dertiende maand (indien niets, vul in 0): ")
bonus = raw_input("In geval van achteraf invoeren, hoeveel was evt. bonus (indien nvt of niets, vul in 0): ")
totaalbedrag = float(loonxmaanden) + float(vakantiegeld) + float(dertiende_maand) + float(bonus)
print "Over de hele werkperiode ontvang je " + str(totaalbedrag) + " !" 

bedrag_per_maand = float(totaalbedrag) / int(aantal_maanden_werk)
reiskosten_per_maand = raw_input("Hoeveel reiskosten ben je per maand kwijt: ")
netto_bedrag_permaand = float(bedrag_per_maand) - float(reiskosten_per_maand)
print "Je houdt dan " + str(netto_bedrag_permaand) + " per maand over."
print "HOERA!"
print "OF NIET."


