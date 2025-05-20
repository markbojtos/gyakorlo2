import datetime
miregyujt=input("Mire gyűjti Anna a pénzt? ")
hanykutya=int(input("Hány kutyát sétáltatott Anna? "))
print(f"Anna {hanykutya*20//60}:{hanykutya*20%60}-t töltött kutyasétáltatással.")
osszpenz=hanykutya*700
if osszpenz>=5000:
    print(f"Anna {hanykutya} kutyát sétáltatott {hanykutya*20//60}:{hanykutya*20%60} alatt, ezért {osszpenz} Ft-ot kapott. Ez elég a {miregyujt} megvásárlásához.")
else:
    print(f"Anna {hanykutya} kutyát sétáltatott {hanykutya*20//60}:{hanykutya*20%60} alatt, ezért {osszpenz} Ft-ot kapott. Ez még nem elég a {miregyujt} megvásárlásához.")