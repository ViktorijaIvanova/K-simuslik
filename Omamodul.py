import random


def kusimus_vastused_2(n):
    print(f"Tere, {n}! Alustame küsitlust.")
    punktid = 0
    
    with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        kus_vas = {}
        for i in range(0, len(lines), 2):
            kus_vas[lines[i].strip()] = lines[i+1].strip()
        
        kusimused = list(kus_vas.keys())
        random.shuffle(kusimused)
        kusimused = kusimused[:5]
    for kusimus in kusimused:
        vastus = kus_vas[kusimus]
        input(f"{kusimus} ")
        
        kasutaja_vastus = input("Kas vastasite õigesti? (jah/ei) ")
        if kasutaja_vastus.lower() == "jah":
            print("Tubli!")
            punktid += 1
    else:
            print("Vale vastus!")    
    if punktid > 3:
        print(f"Tubli töö, {n}! Teie skoor oli {punktid}/5.")
        with open("oiged.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
    else:
        print(f"Pole paha, {n}. Teie skoor oli {punktid}/5.")
        with open("valed.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")



"""
def kusimus_vastused_2(n):        
    print(f"Tere, {n}! Alustame küsitlust.")
    punktid=0    
    for kusimus, vastus in kus_vas.items():
        kasutaja_vastus=input(kusimus)
        if kasutaja_vastus.lower()==vastus.lower():
            print("Õige vastus!")
            punktid+=1
        else:
            print("Vale vastus!")    
    if punktid > 3:
        print(f"Tubli töö, {n}! Teie skoor oli {punktid}/5.")
        with open("oiged.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
    else:
        print(f"Pole paha, {n}. Teie skoor oli {punktid}/7.")
        with open("valed.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
"""
