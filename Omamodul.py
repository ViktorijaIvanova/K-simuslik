kus_vas={"﻿Mis suvi on kuud?":"juuni, juuli, august", "Milline taim sümboliseerib suve?":"päevalill", "Mis püha on suve algus?":"suvine pööripäev", "Mis on suvel õues mängitava mängu nimi?":"lasertag", "Millist puuvilja peetakse suve sümboliks?":"arbuusi"}

def kusimus_vastused_1(n):
    """
    """    
    print(f"Tere, {n}! Alustame küsitlust.")
    punktid=0    
    for kusimus, vastus in kus_vas.items():
        kasutaja_vastus=input(kusimus)
        if kasutaja_vastus.lower()==vastus.lower():
            print("Õige vastus!")
            punktid+=1
        else:
            print("Vale vastus!")    
    if punktid>3:
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
