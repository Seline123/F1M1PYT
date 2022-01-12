print("je wekker gaat, sta je op of snooze je hem ? ")
choice = input()
if choice == 'opstaan':
    print("je staat op vanuit je bed en je voelt je goed!")
elif choice == 'snooze':
    print("zzzzzzzzzzzzz")
else:
    print(choice, "wasnt a valid choice")


print("je loopt naar je kledingkast, ga je eerst douchen of niet ?")
choice = input()
if choice == 'eerst douchen':
    print("Je loopt naar de douche en zet hem aan")
elif choice == 'niet douchen':
    print("je pakt kleding uit je kast en je stinkt")
else:
    print(choice, "wasnt a valid choice")

print("je bent klaar met douchen en je loopt naar beneden, ontbijt je of niet ? ")
choice = input()
if choice == 'ontbijt':
    print("je hebt een lekker eitje gegeten en hebt veel energie")
elif choice == 'niet':
    print("je hebt je ontbijt geskipt, je voelt een beetje misselijk")
else: 
    print(choice, "wasnt a valid choice")

print("je loopt naar buiten onderweg naar school, pak je de fiets of ga je skateboarden ?")
choice = input()
if choice == 'de fiets':
    print("je fietst naar het station en haalt de bus")
elif choice == 'skateboarden':
    print("je skateboard naar het station en bent 5 min te laat voor de bus")
else:
    print(choice, "wasnt a valid choice")

print("je bent op school aangekomen maar je ziet niemand die je kent, loop je naar je les of ga je wachten ?")
choice = input()
if choice == 'lopen naar de  les':
    print("Je loopt naar de les en bent optijd.")
elif choice == 'wachten':
    print("je wacht en ziet je beste vriend aankomen, jullie lopen samen naar de les")
else:
    print(choice, "wasnt a valid choice")

    