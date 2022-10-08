from tkinter import *
class Galeria():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('600x500')
        self.janela.title('Fotos')
        self.janela.resizable(False, False)
        self.lista = ['imagensgaleria/im2.png','imagensgaleria/IMG01.png', 'imagensgaleria/IMG02.png', 'imagensgaleria/paris.png', 'imagensgaleria/ferrari2022.png','imagensgaleria/mercedes2022.png']
        self.imagem = PhotoImage(file='imagensgaleria/im2.png')
        self.iniciar()
    
    def iniciar(self):
        
        self.label = Label(self.janela, bg='green', image=self.imagem,  text='', width=600, height=500)
        self.label.pack()
        
        
        self.menu = Menu(self.janela)
        self.opcoesmenu = Menu(self.menu, tearoff=0)
        self.opcoesmenu.add_command(label= 'Voltar a tela inicial',command=lambda: self.voltartelainicial())
        self.menu.add_cascade(label = 'Opcões', menu= self.opcoesmenu)
        self.janela.config(menu=self.opcoesmenu)
  
        self.botaoesq = Button(self.janela, text='<', padx=5, pady=5, command=lambda:self.mudaesq())
        self.botaoesq.place(x=0, y=450)

        self.botaodir = Button(self.janela, text='>', padx=5, pady=5, command=lambda:self.mudadir())
        self.botaodir.place(x=565, y=450)

      
        self.janela.mainloop()

    
    def mudaesq(self):
      imagemvelha = self.imagem['file'] 
      indice = self.lista.index(imagemvelha)
      
      if indice == 0:
        indice = 5
        file = self.lista[indice]        
        self.imagem['file'] = file
      
      else:
        indice -= 1
        file = self.lista[indice]
        self.imagem['file'] = file

    def mudadir(self):
      imagemvelha = self.imagem['file'] 
      indice = self.lista.index(imagemvelha)
      if indice == 5:        
        indice = 0
        file = self.lista[indice]
        self.imagem['file'] = file
      else:
        indice += 1
        file = self.lista[indice]
        self.imagem['file'] = file

    def voltartelainicial(self):
      self.janela.destroy()
      from telainicial import Telainicial
      Telainicial()

