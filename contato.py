from tkinter import *
import sqlite3 as sq
from tkinter import ttk

class Contato():
  
  def __init__(self):
    self.janela = Tk()
    self.iniciar()


  def iniciar(self):
    
    self.janela.geometry("700x600")
    self.janela.resizable(False, False)
    self.janela.title("Contato")
    
    imagem = PhotoImage(file='designers/Contatos.png')
    self.label = Label(self.janela, image=imagem)
    self.label.pack()
    
    self.lb = Label(self.janela,  font="Calibri 12", bg="Red", foreground='white')
    self.lb.place(x=313, y=426, height=173, width=400)
    
    self.adicionar = Button(self.janela, text='Adicionar', font="Calibri, 12", command=lambda:self.inserir(), padx=20, pady=3, bd=5)
    self.adicionar.place(x=171, y=132)
    
    self.emailadd = Entry(self.janela, bg='White', font="Calibri, 12")
    self.emailadd.place(x=12, y=132, width=126.5, height=40)

    self.nome = Entry(self.label, bg='White', font="Calibri, 12")
    self.nome.place(x=12, y=58, height=40, width=126.5)
    
    self.numero = Entry(self.label, bg='White', font="Calibri, 12")
    self.numero.place(x=170, y=58, height=40, width=126.5)
   
    
    self.menu = Menu(self.janela)
    self.opcoesmenu = Menu(self.menu, tearoff=0)
    self.opcoesmenu.add_command(label= 'Voltar a tela inicial',command=lambda: self.voltartelainicial())
    self.menu.add_cascade(label = 'Opcões', menu= self.opcoesmenu)
    self.janela.config(menu=self.opcoesmenu)
    
    
    self.excluir = Button(self.janela, text="Excluir", font="Calibri, 12", bg="Gray", padx=32, pady=4, bd=5, command=lambda: self.deletar())
    self.excluir.place(x=93,y=310)

    
    self.resetar = Button(self.janela, text="Resetar", font="Calibri, 12", bg="Gray", padx=30, pady=5, bd=5, command=self.resetar)
    self.resetar.place(x=93,y=520)
    
   

    self.listacontatos = ttk.Treeview(self.janela, columns=('nome', 'email', 'numero'), show='headings' )
    
    self.listacontatos.column('nome', minwidth=0, width=100)
    self.listacontatos.column('email', minwidth=0, width=130)
    self.listacontatos.column('numero', minwidth=0, width=130)
    
    self.listacontatos.heading('nome', text='Nome')
    self.listacontatos.heading('email', text='Email')
    self.listacontatos.heading('numero', text='Número')

    self.listacontatos.place(x=313, y=0, height=425, width=390)
    self.banco()
    self.janela.mainloop()

  
    
  def inserir(self): 
    self.bd = sq.connect('banco_contatos')
    self.cursor = self.bd.cursor()
  
    self.cursor.execute("SELECT * FROM contatos")
    ctt = self.cursor.fetchall()
    
    for i in ctt:
      email = i[1]
      numero = i[2]
      
      if self.emailadd.get() == email or self.numero.get() == numero:
        self.lb['text'] = '[Erro] Esse valor já existe'
        self.bd.close()
        return 'nada'
          
        
    
    if not self.numero.get().isnumeric():
        self.lb['text'] = '[Erro] Numero não pode ser uma letra'
        self.bd.close()
        return 'nada'

            
    if self.nome.get()=='' or self.emailadd.get() ==''or self.numero.get()=='':
          self.lb['text'] = '[Erro] não deixe casas vazias'
          self.bd.close()
          return 'nada'
    else:
      self.listacontatos.insert("", "end", values=(self.nome.get(), self.emailadd.get(), self.numero.get()))
      self.inserirbanco()    
      self.nome.delete(0, END)
      self.emailadd.delete(0, END)
      self.numero.delete(0, END)
      self.lb['text'] = ''
      self.bd.close()
          
  
      
  def deletar(self):
    if self.listacontatos.selection() == ():
        self.lb['text'] = '[ERRO] Selecione algum contato para excluir '
        return 'nada'
    item = self.listacontatos.selection()[0]
    
    self.bd = sq.connect('banco_contatos')
    self.cursor = self.bd.cursor()

    valores = self.listacontatos.item(item, 'values')
    email = valores[1]
    print(email)
    
    sql = f"delete from contatos where email='{email}'"
    self.cursor.execute(sql)
    self.bd.commit()
    
    self.cursor.execute("SELECT * FROM contatos")
    print(self.cursor.fetchall())
    item = self.listacontatos.selection()[0]
    self.listacontatos.delete(item)
    self.bd.close()
 
  def resetar(self):
    self.lb['text'] = ''
    self.listacontatos.destroy()
    self.bd = sq.connect('banco_contatos')
    self.cursor = self.bd.cursor()
  
    self.listacontatos = ttk.Treeview(self.janela, columns=('nome', 'email', 'numero'), show='headings' )

    self.listacontatos.column('nome', minwidth=0, width=100)
    self.listacontatos.column('email', minwidth=0, width=130)
    self.listacontatos.column('numero', minwidth=0, width=130)
    
    self.listacontatos.heading('nome', text='Nome')
    self.listacontatos.heading('email', text='Email')
    self.listacontatos.heading('numero', text='Número')

    self.listacontatos.place(x=313, y=0, height=598, width=390)

    self.lb = Label(self.janela,  font="Calibri 12", bg="Red", foreground='white')
    self.lb.place(x=313, y=426, height=173, width=400)

    
    self.cursor.execute("DELETE FROM contatos")
    self.bd.commit()
    self.bd.close()
    
    
  def banco(self):
    
    self.bd = sq.connect('banco_contatos')
    self.cursor = self.bd.cursor()
    self.cursor.execute("CREATE TABLE if not exists contatos (nome text, email text unique primary key, numero intereger)")
    
    self.bd.commit()
  
    self.cursor.execute("SELECT * FROM contatos")
    ctt = self.cursor.fetchall()
   
    for k in ctt:
      nome = k[0]
      email = k[1]
      numero = k[2]
      self.listacontatos.insert("", "end", values=(nome, email, numero))
    self.bd.close()

  def inserirbanco(self):
      self.bd = sq.connect('banco_contatos')
      self.cursor = self.bd.cursor()
      self.cursor.execute("INSERT INTO contatos VALUES ('"+self.nome.get()+"','"+self.emailadd.get()+"','"+self.numero.get()+"')")
      self.bd.commit()
      self.cursor.execute("SELECT * FROM contatos")
      print(self.cursor.fetchall())

  def voltartelainicial(self):
    self.janela.destroy()
    from telainicial import Telainicial
    Telainicial()
