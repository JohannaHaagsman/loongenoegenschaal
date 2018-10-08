#vraag naam werkgever
werkgever = raw_input("Naam werkgever: ")
print werkgever

#vraag nettoloon per maand per 40 uur
nettoloon = raw_input("Nettoloon per maand voor 40 uur: ")
print nettoloon

#vraag hoeveel uur men werkt
werkuren = raw_input("Aantal werkuren per week: ")
print werkuren

#bereken nettomaandloon voor aantal uren
nettoloon_real = (nettoloon / 40) * werkuren
print "Bij " + str(werkuren) + " werkuren per week, verdien je " + str(nettoloon_real) + " per maand."
