import os
import json
import random

elenco_comuni=["Abbiategrasso","Albairate","Arconate","Arese","Arluno","Assago","Baranzate","Bareggio","Basiano","Basiglio","Bellinzago Lombardo","Bernate Ticino","Besate","Binasco","Boffalora Sopra Ticino","Bollate","Bresso","Bubbiano","Buccinasco","Buscate","Bussero","Busto Garolfo","Calvignasco","Cambiago","Canegrate","Carpiano","Carugate","Casarile","Casorezzo","Cassano d'Adda","Cassina de' Pecchi","Cassinetta di Lugagnano","Castano Primo","Cernusco sul Naviglio","Cerro al Lambro","Cerro Maggiore","Cesano Boscone","Cesate","Cinisello Balsamo","Cisliano","Cologno Monzese","Colturano","Corbetta","Cormano","Cornaredo","Corsico","Cuggiono","Cusago","Cusano Milanino","Dairago","Dresano","Gaggiano","Garbagnate Milanese","Gessate","Gorgonzola","Grezzago","Gudo Visconti","Inveruno","Inzago","Lacchiarella","Lainate","Legnano","Liscate","Locate di Triulzi","Magenta","Magnago","Marcallo con Casone","Masate","Mediglia","Melegnano","Melzo","Mesero","Milano","Morimondo","Motta Visconti","Nerviano","Nosate","Novate Milanese","Noviglio","Opera","Ossona","Ozzero","Paderno Dugnano","Pantigliate","Parabiago","Paullo","Pero","Peschiera Borromeo","Pessano con Bornago","Pieve Emanuele","Pioltello","Pogliano Milanese","Pozzo d'Adda","Pozzuolo Martesana","Pregnana Milanese","Rescaldina","Rho","Robecchetto con Induno","Robecco sul Naviglio","Rodano","Rosate","Rozzano","San Colombano al Lambro","San Donato Milanese","San Giorgio su Legnano","San Giuliano Milanese","San Vittore Olona","San Zenone al Lambro","Santo Stefano Ticino","Sedriano","Segrate","Senago","Sesto San Giovanni","Settala","Settimo Milanese","Solaro","Trezzano Rosa","Trezzano sul Naviglio","Trezzo sull'Adda","Tribiano","Truccazzano","Turbigo","Vanzaghello","Vanzago","Vaprio d'Adda","Vermezzo","Vernate","Vignate","Villa Cortese","Vimodrone","Vittuone","Vizzolo Predabissi","Zelo Surrigone","Zibido San Giacomo"]

# {"layout":"odd-r","hexes":{
#               "A":{"n":"Hex a","q":0,"r":0},
#               "B":{"n":"Hex b","q":0,"r":1},
#               "C":{"n":"Hex c","q":1,"r":0},
#               "D":{"n":"Hex d","q":1,"r":1},
#               "E":{"n":"Hex e","q":2,"r":0},
#               "F":{"n":"Hex f","q":2,"r":1},
#               "G":{"n":"Hex g","q":0,"r":2},
#               "H":{"n":"Hex h","q":1,"r":2},
#               "I":{"n":"Hex i","q":2,"r":2}
#             }
#}

'\"{}\":\{\"n\":\"Hex {}\",\"q\":{},\"r\":{}\},'

#print(len(elenco_comuni))
#sqr(134) circa 12
#choice + pop
#blog = {'URL': 'datacamp.com', 'name': 'Datacamp'}
#to_json= json.dumps(blog)
comuni_hex=[]
for i in range(3):
    for j in range(3):
        comune = str(random.choice(elenco_comuni))
        comune_hex = '\"'+comune+'\":{\"n\":\"'+comune+'\",\"q\":'+str(i)+',\"r\":'+str(j)+'},'
        comuni_hex.append(comune_hex)
        #print('\"{}\":,{},{},{}'.format(comune,comune,i,j))
        elenco_comuni.remove(comune)
print("###################################")
print('{"layout":"odd-r","hexes":{')
for comune in comuni_hex:
    print(comune)
print('}')