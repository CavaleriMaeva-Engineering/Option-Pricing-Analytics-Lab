import numpy as np
from core.vanilla import CallOption, PutOption

def main():
  #Création des options
  mon_call=CallOption(100,1,5.0)
  mon_put=PutOption(100,1,5.0)

  #Scénarios de prix à l'échéance (S_T)
  prix_finaux=[80, 90, 100, 110, 120]

  #Calcul des payoffs
  gains_call=mon_call.payoff(prix_finaux)
  gains_put=mon_put.payoff(prix_finaux)
  
  #Affichage des résultats
  print(f"Prix du marché : {prix_finaux}")
  print(f"Gains du Call  : {gains_call}")
  print(f"Gains du Put   : {gains_put}")

if __name__=="__main__":
  main()
