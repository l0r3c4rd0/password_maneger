import customtkinter as gui
#servirà in modo tale che invece di scrivere customtkinter scrivo gui
from PIL import Image
#necessario pk customthinker nn gestisce bene le immagini e devo prendere la libreria Image
finestra=gui.CTk()
#serve per creare la finestra
finestra.title("cardelli management")
finestra.geometry("736x460")
#dimensioni su stringa e non su intero con 736 larghezza e 460 altezza
sfondo=Image.open("immagini/sfondo.jpg")
sfondo=gui.CTkImage(sfondo,size=(736,460))
#ora devo trasformarlo in gui
sfondo=gui.CTkLabel(finestra,image=sfondo)
sfondo.place(x=0,y=0)
testo_1=gui.CTkLabel(finestra,text="Password amministratore richiesta",text_color="#6366F1",font=("consolas",20),)
#creo il mio testo con colore cyan e gestendo il font con la dimensione in pixel
accedi=gui.CTkButton(finestra,text="ACCEDI",fg_color="#7C3AED",hover_color="#2563EB",width=200,height=60,corner_radius=15)
#pulsante con colore se nn ci sei sopra(fg color) e quando ci sei (hover color) e il raggio degli arrotondamenti dei angoli(corner radius)
accedi.place(x=260,y=340)
testo_1.pack(pady=120)
#comando per mostrare il testo
piattaforma_login=gui.CTkEntry(finestra,width=300,height=50)
#crea la casella
piattaforma_login.pack()
#mostra la piattaforma
finestra.mainloop()
#istruzione che va sempre per ultima pk prende le funzioni precedenti e le mette nella finestra tutto quello che e sotto nn lo considera
