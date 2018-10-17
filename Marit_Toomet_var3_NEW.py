#ÜL Palindroom
#funktsioon palindrom jagab lause tühikute järgi nö sõnadeks ja kontrollib kas sõna on võrdne sama sõnaga kui ta on ümber pööratud
def palindrom(argument1):
    tulemus_list= []
    #jagab sõnadeks
    tulemus_list=argument1.split(" ")
    i=0
    for i in range(len(tulemus_list)) :
  
        #kontrollib tingimust (kas sõna= ümber pööratud sõnaga)
        if tulemus_list[i]==tulemus_list[i][::-1]:
            vastus=[]
            vastus.append(tulemus_list[i])
            i=i+1
        elif len(vastus) <= 0:
            print("Polegi palindroome!")
    return vastus

print(palindrom("otto mis teed siis"))

#ÜL Population
# funktsioon leiab naiste ja laste arvu ja liidab need meeste arvuga
def population(x):
    meeste_arv= x
    #iga mehe kohta on ka sama arv (x) naisi
    naiste_arv = meeste_arv*x
    #iga naise kohta on sama arv (x) lapsi
    laste_arv= naiste_arv*x
    #kogu populatsioon = mehed + naised + lapsed
    vastus= meeste_arv + naiste_arv + laste_arv
    return vastus
print(population(5))


      







