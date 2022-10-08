from tkinter import *
import webbrowser

class Navegador():
  def __init__(self):
    self.janela = Tk()
    self.iniciar()

  def pesquisar(self, site):
    lista = [
      ['google', 'https://www.google.com.br/search?q='],            ['yahoo','https://br.search.yahoo.com/search?p='],            ['youtube','https://www.youtube.com/search?q='],              ['twitter','https://twitter.com/']]
    for k in lista:
        if self.pesquisa.get() == '':
          return 'nada'
        elif site == k[0]:
            webbrowser.open(k[1]+self.pesquisa.get())
    if site == 'instagram':
      webbrowser.open(f'https://www.instagram.com/{self.pesquisa.get()}/')
        

  def barradepesquisa(self):  
    pesquisa = ('https://www.google.com.br/search?q='+str(self.pesquisa.get()))
    webbrowser.open(pesquisa)
    
  def iniciar(self):
    self.janela.geometry('600x600')
    self.janela.title('Navegador')
    self.janela.resizable(False, False)

    imagem = PhotoImage(file='designers/Navegador.png')
    self.label = Label(self.janela, image=imagem)
    self.label.pack()

    self.pesquisa = Entry(self.label)
    self.pesquisa.place(x=106, y=274, width=400, height=50)

    imagemgoogle = PhotoImage(file='imagensnavegador/google.png')
    self.google = Button(self.label,padx=20, pady=12,image=imagemgoogle, command=lambda:self.pesquisar('google'))
    self.google.place(x=450, y=351)


    imagemyaroo = PhotoImage(file='imagensnavegador/yaroo.png')
    
    self.yahoo = Button(self.label,padx=20, pady=12, image = imagemyaroo, command=lambda: self.pesquisar('yahoo'))
    self.yahoo.place(x=106, y=351) 
    
    imagemyoutube = PhotoImage(file='imagensnavegador/youtube.png')
   
    self.youtube = Button(self.label,padx=20, pady=12,image=imagemyoutube, command=lambda:self.pesquisar('youtube'))
    self.youtube.place(x=194, y=351) 

    imagemtwitter = PhotoImage(file='imagensnavegador/twitter.png')
    self.twitter = Button(self.label,padx=20, pady=12,image=imagemtwitter, command=lambda:self.pesquisar('twitter'))
    self.twitter.place(x=277, y=351) 


    imageminsta = PhotoImage(file='imagensnavegador/insta.png')
    self.insta = Button(self.label,padx=20, pady=12,image=imageminsta, command=lambda:self.pesquisar('instagram'))
    self.insta.place(x=362, y=351) 
    
    self.menu = Menu(self.janela)
    self.opcoesmenu = Menu(self.menu, tearoff=0)
    self.opcoesmenu.add_command(label= 'Voltar a tela inicial',command=lambda: self.voltartelainicial())
    self.menu.add_cascade(label = 'Opcões', menu= self.opcoesmenu)
    self.janela.config(menu=self.opcoesmenu)

    self.janela.mainloop()

  def voltartelainicial(self):
      self.janela.destroy()
      from telainicial import Telainicial
      Telainicial()

