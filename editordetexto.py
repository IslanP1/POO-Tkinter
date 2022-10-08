from tkinter import *
from tkinter.filedialog import askopenfilename 
from tkinter.filedialog import asksaveasfilename 
from tkinter import messagebox

class Editordetexto():
    def __init__(self):
        self.janela = Tk()
        self.iniciar()
        

    def iniciar(self):
        self.janela.geometry('600x600')
        self.janela.title('Editor de Texto')
        self.janela.resizable(False, False)
        self.label = Label(self.janela)
        self.label.place(x=0,y=0, width=600, height=600)

        self.texto = Text(self.label, font= 'Arial 25')
        self.texto.place(x=10, y=5, width=570, height=585)

        self.menu = Menu(self.janela)
       
        self.opcoesmenu = Menu(self.menu, tearoff=0)
        self.opcoesmenu.add_command(label= 'Abrir',command=lambda: self.abrir())
        self.opcoesmenu.add_command(label= 'Salvar',command=lambda: self.salvar())
        self.opcoesmenu.add_command(label= 'Salvar como',command=lambda: self.salvarComo())
        self.opcoesmenu.add_command(label= 'Novo arquivo',command=lambda: self.novoArquivo())
        self.opcoesmenu.add_command(label= 'Instruções de uso',command=lambda: self.instrucoes())
        self.opcoesmenu.add_command(label= 'Sair para a tela inicial',command=lambda: self.voltartelainicial())
        self.menu.add_cascade(label = 'Opcões', menu= self.opcoesmenu)
        
        self.opcoestamanho = Menu(self.menu, tearoff=0)
        self.opcoestamanho.add_command(label= 'Texto pequeno', command= lambda: self.tamanhoPequeno())
        self.opcoestamanho.add_command(label= 'Texto médio', command= lambda: self.tamanhoMedio())
        self.opcoestamanho.add_command(label= 'Texto grande', command= lambda: self.tamanhoGrande())
        self.menu.add_cascade(label = 'Tamanho', menu= self.opcoestamanho)
        self.janela.config(menu=self.menu)

        self.opcoesfonte = Menu(self.menu, tearoff=0)
        self.opcoesfonte.add_command(label= 'Arial', command= lambda: self.fonteArial())
        self.opcoesfonte.add_command(label= 'Calibri', command= lambda: self.fonteCalibri())
        self.opcoesfonte.add_command(label= 'Georgia', command= lambda: self.fonteGeorgia())
        self.menu.add_cascade(label = 'Fonte', menu= self.opcoesfonte)
        self.janela.config(menu=self.menu)

        self.opcoesedicao = Menu(self.menu, tearoff=0)
        self.opcoesedicao.add_command(label= 'Negrito',command= lambda: self.negrito())
        self.opcoesedicao.add_command(label= 'Preto',command= lambda: self.corPreto())
        self.opcoesedicao.add_command(label= 'Vermelho',command= lambda: self.corVermelho())
        self.opcoesedicao.add_command(label= 'Azul',command=lambda: self.corAzul())
        self.menu.add_cascade(label = 'Destaque', menu= self.opcoesedicao)
        self.janela.config(menu=self.menu)

        self.lista = []
        self.lista1 = []
        self.fonte = ['25', '35', '45']
        self.fonteLetra = ['Arial', 'Calibri', 'Georgia']
        
        self.janela.mainloop()
       

    #Manuseio de documentos
    def abrir(self):
        self.arquivo = askopenfilename()
        self.arquivoTexto = open(self.arquivo, 'r')
        self.textoSalvo = self.arquivoTexto.read()
        # inicio = 1.0, fim = end
        self.texto.insert(1.0, self.textoSalvo)


    def salvar(self):
        self.nomeArquivo = asksaveasfilename()
        self.salvar1 = self.texto.get(1.0, END)
        self.arquivoPadrao = open(f"{self.nomeArquivo}.txt", 'w')
        self.arquivoPadrao.write(self.salvar1)
        self.arquivoPadrao.close()
       

    def salvarComo(self):
        self.tipoArquivo = asksaveasfilename()
        self.salvar1 = self.texto.get(1.0, END)
        self.opcaoArquivo = open(self.tipoArquivo, 'w')
        self.opcaoArquivo.write(self.salvar1)
        self.opcaoArquivo.close()


    def novoArquivo(self):
        self.texto.delete(1.0, END)


    #tamanho da letra
    def tamanhoPequeno(self):
        self.texto['font'] = f'{self.fonteLetra[0]} {self.fonte[0]}'
        self.lista.append(self.fonte[0])

    
    def tamanhoMedio(self):
        self.texto['font'] = f'{self.fonteLetra[0]} {self.fonte[1]}'
        self.lista.append(self.fonte[1])
        
    def tamanhoGrande(self):
        self.texto['font'] = f'{self.fonteLetra[0]} {self.fonte[2]}'
        self.lista.append(self.fonte[2])

      
    #fonte letra
    def fonteArial(self):
        for k in self.lista:    
            self.lista1.append(self.fonteLetra[0])
            if self.fonte[0] == k:
                self.texto['font'] = f'{self.fonteLetra[0]} {self.fonte[0]}'
            
            if self.fonte[1] == k:
                self.texto['font'] = f'{self.fonteLetra[0]}  {self.fonte[1]}'
    
            if self.fonte[2] == k:
                self.texto['font'] = f'{self.fonteLetra[0]}  {self.fonte[2]}'
            
                
    def fonteCalibri(self):
       for k in self.lista:
            self.lista1.append(self.fonteLetra[1])
            if self.fonte[0] == k:
                self.texto['font'] = f'{self.fonteLetra[1]} {self.fonte[0]}'
            
            if self.fonte[1] == k:
                self.texto['font'] = f'{self.fonteLetra[1]}  {self.fonte[1]}'
    
            if self.fonte[2] == k:
                self.texto['font'] = f'{self.fonteLetra[1]}  {self.fonte[2]}'
                

    def fonteGeorgia(self):
        for k in self.lista:
            self.lista1.append(self.fonteLetra[2])
            if self.fonte[0] == k:
                self.texto['font'] = f'{self.fonteLetra[2]} {self.fonte[0]}'
            
            if self.fonte[1] == k:
                self.texto['font'] = f'{self.fonteLetra[2]}  {self.fonte[1]}'
    
            if self.fonte[2] == k:
                self.texto['font'] = f'{self.fonteLetra[2]}  {self.fonte[2]}'


    #cor da letra
    def corPreto(self):
        self.texto['fg'] = 'Black'

    def corVermelho(self):
        self.texto['fg'] = 'Red'

    def corAzul(self):
        self.texto['fg'] = 'Blue'


    #Negrito
    def negrito(self):
        for k in self.lista:
            if k == self.fonte[0]:
                self.apagar = len(self.lista1)
                self.ultimoElemento = self.lista1[self.apagar-1]
                self.lista.clear()
            

                if self.fonteLetra[0] == self.ultimoElemento:
                    self.texto['font'] = f'{self.fonteLetra[0]} {self.fonte[0]} bold'
                    self.lista1.clear()
                   
                if self.fonteLetra[1] == self.ultimoElemento:
                    self.texto['font'] = f'{self.fonteLetra[1]} {self.fonte[0]} bold'
                    self.lista1.clear()
            
                if self.fonteLetra[2] == self.ultimoElemento:
                    self.texto['font'] = f'{self.fonteLetra[2]} {self.fonte[0]} bold'
                    self.lista1.clear()
                   

            if k == self.fonte[1]:
                self.apagar1 = len(self.lista1)
                self.ultimoElemento1 = self.lista1[self.apagar1-1]
                self.lista.clear()


                if self.fonteLetra[0] == self.ultimoElemento1:
                    self.texto['font'] = f'{self.fonteLetra[0]} {self.fonte[1]} bold'
                    self.lista1.clear()
                    
                if self.fonteLetra[1] == self.ultimoElemento1:
                    self.texto['font'] = f'{self.fonteLetra[1]} {self.fonte[1]} bold'
                    self.lista1.clear()
                    
                if self.fonteLetra[2] == self.ultimoElemento1:
                    self.texto['font'] = f'{self.fonteLetra[2]} {self.fonte[1]} bold'
                    self.lista1.clear()
                    

            if k == self.fonte[2]:
                self.apagar2 = len(self.lista1)
                self.ultimoElemento2 = self.lista1[self.apagar2-1]
                self.lista.clear()
          
                
                if self.fonteLetra[0] == self.ultimoElemento2:
                    self.texto['font'] = f'{self.fonteLetra[0]} {self.fonte[2]} bold'
                    self.lista1.clear()
                  
                if self.fonteLetra[1] == self.ultimoElemento2:
                    self.texto['font'] = f'{self.fonteLetra[1]} {self.fonte[2]} bold'
                    self.lista1.clear()
                   
                if self.fonteLetra[2] == self.ultimoElemento2:
                    self.texto['font'] = f'{self.fonteLetra[2]} {self.fonte[2]} bold'
                    self.lista1.clear()


    def instrucoes(self):
        messagebox.showinfo("Intruções de uso!", "Passo 1: Escolha o tamanho da letra\n \nPasso 2: Escolha sua fonte\n \nPasso 3: Escolha os detalhes que preferir\n \nObservação: Só é possível selecionar a fonte se escolher o tamanho do texto. O negrito também só é acionado se escolher a fonte.")

    def voltartelainicial(self):
      self.janela.destroy()
      from telainicial import Telainicial
      Telainicial()