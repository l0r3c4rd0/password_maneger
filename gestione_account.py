import json
#estensione per lasciare in memoria su python
def creazione_credenziali(piattaforma,nome,password):
    credenziali={
        "servizio":piattaforma,
        "utente":nome,
        "password_utente":password
    }
    accesso=False
    try:
        file=open("credenziali.json","r")
        #cerca di leggere il file se esiste se no va nell except
        lista=json.load(file)
        #legge il contenuto e lo carica in lista
        for elemento in lista:
            if elemento["servizio"]==piattaforma and elemento["utente"]==nome and elemento["password_utente"]==password:
                print("benvenuto")
                azione=input("scrivi ""m"" per modificare credenziali,""v"" per vederle,""d"" per eliminarle e ""n"" se non vuoi fare nulla ").lower()
                while azione!="m" and azione!="v" and azione!="d" and azione!="n":
                    azione=input("scrivi ""m"" per modificare credenziali,""v"" per vederle,""d"" per eliminarle e ""n"" se non vuoi fare nulla ").lower()
                file.close()
                #tutto corretto quindi chiudo la funzione  
                accesso=True            
        if not accesso:
            richiesta=input("hai sbagliato qualcosa devi registrarti?: ").lower()
            while not richiesta=="no" and not richiesta=="si":
                richiesta=input("hai sbagliato qualcosa devi registrarti?: ").lower()
                #finchè nn capiamo pk ha sbagliato
            if richiesta=="si":
                lista.append(credenziali)
                file=open("credenziali.json","w")
                #adesso lo apro come file modificabile per metterci la roba nuova
                json.dump(lista,file)
                #metto il contenuto di lista in file
                file.close()
                #utente nuovo quindi lo registro
            else:
                print("riprova")
                nome=input("dammi il nome dell utente: ")
                password=input("dimmi la password dell utente: ")
                piattaforma=input("in che piattaforma andiamo: ").lower()
                return creazione_credenziali(piattaforma,nome,password)
                #far riprovare per vedere se ci azzecca sta volta
                #risolvere il fatto che se riprovo dopo aver detto di no e faccio corretto me lo considera nuovamente sbagliato
    except:
        file=open("credenziali.json","w")
        #vuol dire che il file nn e stato ancora creato
        lista=[]
        #creo la lista di dizionari
        lista.append(credenziali)
        json.dump(lista,file)
        file.close()
        #serve per far finire il processo chiudendo il file
nome=input("dammi il nome dell utente: ")
password=input("dimmi la password dell utente: ")
piattaforma=input("in che piattaforma andiamo: ").lower()
creazione_credenziali(piattaforma,nome,password)