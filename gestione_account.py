import json
#estensione per lasciare in memoria su python
def creazione_credenziali(piattaforma,nome,password):
    credenziali={
        "servizio":piattaforma,
        "utente":nome,
        "password_utente":password
    }
    file=open("credenziali.json","w")
    #servirà per creare il file se nn esiste o lo richiama se esiste e assegnalo ad una variabile se no si perde tutto
    json.dump(credenziali,file)
    #serve per scrivere le credenziali nel file
    file.close()
    #serve per far finire il processo chiudendo il file
    print("a")
nome=input("dammi il nome dell utente: ")
password=input("dimmi la password dell utente: ")
piattaforma=input("in che piattaforma andiamo: ")
try:
    file=open("credenziali.json","r")
    #prova ad aprire il file in modalità read e assegna il contenuto alla variabile che sarà una lista
    """for elemento in file:
        print(file[elemento])"""
except:
    creazione_credenziali(piattaforma,nome,password)
    #nel caso nn esiste il file invece che andare in errore ti porta alla funzione per creare sia il file che credenziali

