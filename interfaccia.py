import customtkinter as gui
#servirà in modo tale che invece di scrivere customtkinter scrivo gui
finestra=gui.CTk()
#serve per creare la finestra
finestra.title("cardelli manegment")
finestra.geometry("900x700")
#dimensioni su stringa e non su intero con 900 larghezza e 700 altezza
testo_1=gui.CTkLabel(finestra,text="dove vuoi andare?",text_color="cyan")
#creo il mio testo
testo_1.pack()
#comando per mostrare il testo
piattaforma_login=gui.CTkEntry(finestra,width=300,height=50)
#crea la casella
piattaforma_login.pack()
#mostra la piattaforma
finestra.mainloop()
#istruzione che va sempre per ultima pk prende le funzioni precedenti e le mette nella finestra tutto quello che e sotto nn lo considera
