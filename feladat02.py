kutyanevek=[]

def beolvasas():
    f=open("kutyusok.txt", encoding="utf-8")
    for sor in f:
        sor.upper()
        kutyanevek.append(sor)

def hanynev():
    nevekszama=len(kutyanevek)
    print(f"{nevekszama} darab név szerepel a listában.")

def iveguek():
    lista=[]
    for i in range(len(kutyanevek)):
        if len(kutyanevek[i]-1)=="i":
            lista.append(kutyanevek[i])
    print(lista)

def main():
    beolvasas()
    hanynev()
    iveguek()
main()
