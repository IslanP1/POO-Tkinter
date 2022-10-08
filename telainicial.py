from tkinter import *
import datetime
import webbrowser
class Telainicial():
  
  def __init__(self):
    self.janela = Tk()
    self.janela.resizable(False, False)
    self.iniciar()
    
  def iniciar(self):
    
    self.janela.geometry("1280x701")
    self.janela.title("Máquina virtual")
  

    imagem = PhotoImage(file = 'imagenstelainicial/aredetrabalho.png')
    self.label = Label(self.janela,image=imagem, width=1280, height=700)
    self.label.pack()

    imeditor = PhotoImage(file='imagenstelainicial/editor.png')
    self.editor = Button(self.label, bg="Gray", padx=20, pady=12,image=imeditor, command=lambda:self.abrireditor())
    self.editor.place(x=25,y=25)

    imcalculadora = PhotoImage(file='imagenstelainicial/calculadora.png')
    self.calculadora = Button(self.label, padx=20, pady=12, bg="Gray",image= imcalculadora, command=lambda:self.abrircalculadora())
    self.calculadora.place(x=25,y=100)

    imgaleria = PhotoImage(file='imagenstelainicial/galeria.png')
    self.galeria = Button(self.label, padx=20, pady=12, bg="Gray",image=imgaleria, command=lambda:self.abrirgaleria())
    self.galeria.place(x=25,y=175)
 
    imquizgame = PhotoImage(file='imagenstelainicial/extremequiz.png')
    self.jogo = Button(self.label, padx=20, pady=12, bg="Gray", image=imquizgame, command=lambda:self.abrirquizgame())
    self.jogo.place(x=25,y=250)
    
    imnavegador = PhotoImage(file='imagenstelainicial/navegador.png')
    self.navegador = Button(self.label, padx=20, pady=12, bg="Gray",image=imnavegador, command=lambda:self.abrirnavegador())
    self.navegador.place(x=25,y=325)
 
    imcontatos = PhotoImage(file='imagenstelainicial/contatos.png')
    self.contatos = Button(self.label, padx=20, pady=12, bg="Gray",image=imcontatos, command=lambda:self.abrircontato())
    self.contatos.place(x=25,y=400)
    
    self.label1 = Label(self.label, width=90, height=10, bg = '#d2e4f0')
    self.label1.place(x=510, y=648)

    self.hora = Label(self.label,width=25, height=3, bg = '#d2e4f0')
    self.hora.place(x=1092, y=648)

    self.pesquisa = Entry(self.janela, font='Arial 20')
    self.pesquisa.place(x=58, y=650, height=50, width=480)
    
    self.iminiciar = PhotoImage(file='imagenstelainicial/botaoiniciar.png')
    self.botaoiniciar = Button(self.label, padx=10, pady=10, bg="Gray",image=self.iminiciar, command=lambda: self.abrirfuncionamento())
    self.botaoiniciar.place(x=-1, y=648)

    self.impesquisa = PhotoImage(file='imagenstelainicial/botaopesquisar.png')
    self.pesquisar = Button(self.janela, padx=10, pady=10, bg="Gray",image=self.impesquisa, command=lambda: self.pesquisarapida())
    self.pesquisar.place(x = 540, y=650)

    
    self.atthora()
    self.janela.mainloop()

  def abrircalculadora(self):
    self.janela.destroy()
    from calculadora import Calculadora
    Calculadora()

  def abrircontato(self):
    self.janela.destroy()
    from contato import Contato
    Contato()
  
  def abrireditor(self):
    self.janela.destroy()
    from editordetexto import Editordetexto
    Editordetexto()
  
  def abrirquizgame(self):
    self.janela.destroy()
    from extremequizgame import ExtremeQuizGame
    ExtremeQuizGame()

  def abrirgaleria(self):
    self.janela.destroy()
    from galeria import Galeria
    Galeria()

  def abrirnavegador(self):
    self.janela.destroy()
    from navegador import Navegador
    Navegador()
    
  def abrirfuncionamento(self):
    self.janela.destroy()
    from funcionamento import Funcionamento
    Funcionamento()

    
  def atthora(self):
    horaatual = datetime.datetime.now()
    horaatualsemmilesimos = horaatual.strftime('%H:%M:%S')
    self.hora['text'] = horaatualsemmilesimos
    self.hora.after(200, self.atthora)
    self.hora['font'] = 'Arial 12 bold'

  def pesquisarapida(self):
     conteudo = self.pesquisa.get()
     x = (f'https://www.google.com.br/search?q={conteudo}')
     webbrowser.open(x)