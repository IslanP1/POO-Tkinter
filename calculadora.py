from tkinter import *
import math

class Calculadora():
  
  def __init__(self):
    self.janela = Tk()
    self.iniciar()
    

  def iniciar(self):
  
    self.janela.geometry("600x500")
    self.janela.resizable(False, False)
    self.janela.title("Calculadora")
    
    imagem = PhotoImage(file="designers/Calculadora.png")
    
    self.label = Label(self.janela, image=imagem)
    self.label.pack()

    
    self.label2 = Label(self.label,padx=0.00000000000000000000000000000000000000000001, pady=6, font="Calibri 20")
    self.label2.place(x=26, y=68)

    
    self.menu = Menu(self.janela)
    self.opcoesmenu = Menu(self.menu, tearoff=0)
    self.opcoesmenu.add_command(label= 'Voltar a tela inicial',command=lambda: self.voltartelainicial())
    self.menu.add_cascade(label = 'Opcões', menu= self.opcoesmenu)
    self.janela.config(menu=self.opcoesmenu)
    

    self.num1 = Entry(self.label, width=70, bg='White', font="Calibri 20")
    self.num1.place(x=26, y=172, width= 214, height=64)

    self.num2 = Entry(self.label, width=30, bg='White', font="Calibri 20")
    self.num2.place(x=352, y=172, height=64, width=212)

    adicao = Button(self.janela, text="+", font="Calibri, 12", bg="Gray", padx=20, pady=15, bd=5, command=lambda:self.sinal("+"))
    adicao.place(x=150,y=270)
    
    multiplicacao = Button(self.janela, text="x", font="Calibri, 12", bg="Gray", padx=20, pady=15, bd=5, command=lambda:self.sinal(" x"))
    multiplicacao.place(x=265,y=270)

    raizquadrada = Button(self.janela, text="√", font="Calibri, 12", bg="Gray", padx=20, pady=15, bd=5, command=lambda:self.sinal("√"))
    raizquadrada.place(x=383,y=270)

    subtracao = Button(self.janela, text=" - ", font="Calibri, 12", bg="Gray",padx=20, pady=15, bd=5, command=lambda:self.sinal(" -"))
    subtracao.place(x=150,y=373)

    divisao = Button(self.janela, text=" ÷", font="Calibri, 12", bg="Gray", padx=20, pady=15, bd=5, command=lambda:self.sinal("÷"))
    divisao.place(x=265,y=373)

    potencia = Button(self.janela, text="x²", font="Calibri, 12", bg="Gray", padx=20, pady=15, bd=5, command=lambda:self.sinal("^"))
    potencia.place(x=383,y=373)

    porcentagem = Button(self.janela, text="%", font="Calibri, 12", bg="Gray", padx=24, pady=67, bd=5,command=lambda:self.sinal("%"))
    porcentagem.place(x=29,y=270)
  
    igual = Button(self.janela, text="=", font="Calibri, 12", bg="Gray", padx=23, pady=67, bd=5, command= self.funcsinal)
    igual.place(x=499,y=270)

    self.operacao = Label(self.janela, text=" ", font="Calibri, 12", bg="Gray", padx=15, pady=8, bd=5)
    self.operacao.place(x=275,y=186)

    self.janela.mainloop()

  
  def sinal(self, texto):
    if self.operacao["text"] == str(texto):
      pass 
    
    else:
      self.label2["text"] = ""
      self.num1.delete(0,END)
      self.num2.delete(0,END)
      self.operacao['text'] = texto
      
      if self.operacao['text'] == "√": 
        self.ocultar()
        try:
            self.labnum1.destroy()
            self.labnum2.destroy()
        except:
            pass
      
      elif self.operacao['text'] == "%":
        self.mudarpot()
        try:
            self.lb1.destroy()
            self.lbraiz.destroy()
        except:
            pass
      
      else:
        try:
          self.lb1.destroy()
          self.lbraiz.destroy()
        except: 
          pass
        try:
          self.labnum1.destroy()
          self.labnum2.destroy()
        except:
          pass
          
  def ocultar(self): 
    self.lbraiz = Label(self.janela, width=30, text="Raiz",foreground='white', font="Calibri 12", bg="#054cab")
    self.lbraiz.place(x=60, y=140, height=30, width=150)
    self.lb1 = Label(self.janela,  font="Calibri 20", bg="#054cab")
    self.lb1.place(x=352, y=140, height=100, width=300)

  def mudarpot(self):
    self.labnum1 = Label(self.janela,  font="Calibri 12", bg="#054cab", text='Porcentagem', foreground='white')
    self.labnum1.place(x=60, y=140, height=30, width=180)

    self.labnum2 = Label(self.janela,  font="Calibri 12", bg="#054cab", text='Valor', foreground='white')
    self.labnum2.place(x=400, y=140, width=150, height=30)
  

  def funcsinal(self):
    try:
      
      if self.operacao["text"] == "+":
        self.adicao()
      elif self.operacao["text"] == " -":
        self.subtracao()
      elif self.operacao["text"] == " x":
        self.multiplicacao()
      elif self.operacao["text"] == "^":
        self.potencia()
      elif self.operacao["text"] == "√":
        self.raiz()
      elif self.operacao["text"] == "÷":
        self.divisao()
      elif self.operacao["text"] == "%":
        self.porcentagem()
        

    except ValueError:
      self.label2['text'] = '[Erro] operação por letras'
      self.operacao['text'] = ' '

      

 
  def adicao(self):
    num1 = self.num1.get()
    num2 = self.num2.get()
    if num1 == '':
      num1 = 0

    if num2 == '':
      num2 = 0
    soma = float(num1) + float(num2)
    self.label2["text"] = f"{(num1)} + {str(num2)} = {str(soma)}"
    self.num1.delete(0,END)
    self.num2.delete(0,END)

  
  def subtracao(self):
    num1 = self.num1.get()
    num2 = self.num2.get()
    if num1 == '':
      num1 = 0
    if num2 == '':
      num2 = 0
    sub = float(num1) - float(num2)
    self.label2["text"] = f"{str(num1)} - {str(num2)} = {str(sub)}"
    self.num1.delete(0,END)
    self.num2.delete(0,END)


  def multiplicacao(self):
    num1 = self.num1.get()
    num2 = self.num2.get()
    if num1 == '':
      num1 = 0
    if num2 == '':
      num2 = 0
    mult = float(num1) * float(num2)
    self.label2["text"] = f"{str(num1)} x {str(num2)} = {str(mult)}"
    self.num1.delete(0,END)
    self.num2.delete(0,END)


  def divisao(self):

     num1 = self.num1.get()
     num2 = self.num2.get()
     
     if num1 == '':
        num1 = 0
     if num2 == '':
        num2 = 0
     
     try:
        div = float(num1) / float(num2)
        self.label2["text"] = f"{str(num1)} ÷ {str(num2)} = {str(div)}"


     except ZeroDivisionError:
        self.label2['text'] = '[Erro] divisão por zero'
        self.operacao['text'] = ' '


     finally:
        self.num1.delete(0,END)
        self.num2.delete(0,END)


  def potencia(self):
    num1 = self.num1.get()
    num2 = self.num2.get()
    if num1 == '':
      num1 = 0
    if num2 == '':
      num2 = 0
    poten = float(num1) ** float(num2)
    self.label2["text"] = f"{str(num1)} elevado a {str(num2)} = {str(poten)}"
    self.num1.delete(0,END)
    self.num2.delete(0,END)


  def raiz(self):
    num1 = self.num1.get()
    if num1 == '':
      num1 = 0
    raizq = math.sqrt(float(num1)) 
    self.label2["text"] = f"A raiz quadrada de {str(num1)} é = {str(raizq)}"
    self.num1.delete(0,END)
    self.num2.delete(0,END)


  def porcentagem(self):
    num1 = self.num1.get()
    num2 = self.num2.get()
    if num1 == '':
      num1 = 0
    if num2 == '':
      num2 = 0
    porcem = (float(num2)/100)*float(num1)
    self.label2['text'] = f'{str(num1)}% de {str(num2)} = {str(porcem)}'
    self.num1.delete(0,END)
    self.num2.delete(0,END)

  def voltartelainicial(self):
    self.janela.destroy()
    from telainicial import Telainicial
    Telainicial()
