from tkinter import *
import random

class ExtremeQuizGame():
  
  def __init__(self):
    self.janela = Tk()
    self.numero =0
    self.numerodequestoes = 0
    self.pontos = 0
    self.questoes = [
      ['Matematica', [['Qual o triplo do triplo de 5?' , '45' , '40' , '35' , '50'], 
                      ['André gasta 10 minutos para ir de sua casa até a escola,\n sabendo disso, quantos segundos ele leva para fazer essa caminhada?' , '600' , '660' , '540' , '1000'], 
                      ['Quantos zeros tem o numero 10 Bilhões' , '10' , '11' , '9' , '12']]],
      
      ['Variedades', [['Qual fruto é conhecido no Norte\n e Nordeste como “jerimum”?','Abóbora', 'Caju', 'Chuchu', 'Côco'], 
                      ['Qual é o coletivo de cães?','Matilha', 'Rebanho', 'Alcateia', 'Manada'],
                      ['A compensação por perda é chamada de…', 'Indenização', 'Déficit', 'Indexação', 'Indébito']]],
      
      ['Historia', [['Quem compôs o hino da independência?', 'Dom Pedro I.', 'Manuel Bandeira', 'Castro Alvez', 'Carlos Gomes'],
                    ['Qual foi o último presidente do \nperíodo da ditadura militar no Brasil?', 'João Figueiredo', 'Costa e Silva', 'Ernesto Geisel', 'Emílio Médici'],
                    ['Em que ano foi declarada a \nproclamação da república?', '1889', '1930', '2020', '1500']]],
      
      ['Geografia', [['O Brasil é banhado por qual oceano? ', 'Oceano Atlântico', 'Oceano Ártico', 'Oceano Índico', 'Oceano Pacifico'],
                     ['O Brasil possui quantas regiões?', '5', '4', '6', '7'],
                     ['Onde o Brasil está localizado?', 'America do sul', 'America do norte', 'America central', 'Europa']]],
      
      ['Ingles', [['Qual a tradução de "You shall not pass"?', 'Você não passará!', 'Pode entrar', 'voce não pode levar!', 'nenhuma das alternativas' ],
                  ['O termo "actually" significa: ', 'Na verdade ','atualmente','obviamente','simplesmente'],
                  ['Qual das alternativas responde \ncorretamente a pergunta “How are you?”', 'I am fine, thanks ','I am 10','I am student','I am a police officer']]],
      
      ['Filosofia', [['René Descartes desenvolveu um método \nfilosófico baseado na dúvida para encontrar uma certeza \nna qual possa fundamentar o conhecimento seguro. \nEssa certeza fundamental de Descartes é chamada \nde cogito e sua formulação principal diz:', '"Penso, logo existo"', '"Conhece-te a ti mesmo"', '"Deus sive natura"', '"Só sei que nada sei"'], 
                     ['Quem desses filósofos é considerado o primeiro\n filósofo da tradição ocidental.', 'Tales de Mileto', 'Anaximandro', 'Heráclito de Éfeso', 'Pitágoras de Samos'],
                     ['Qual das frases abaixo é do filósofo Sócrates?', '"Só sei que nada sei"', '“Quem comete uma injustiça é sempre mais infeliz que o injustiçado”', '“Tente mover o mundo – o primeiro passo será mover a si mesmo”', '“Espera de teu filho o que fizeste com teu pai”']]],
      
      ['Portugues', [['Qual é o antônimo de “malograr”?', 'Conseguir', 'Desprezar', 'Fracassar', 'Perder'], 
                    ['O termo índole se trata do...' , 'Carater de alguém','conjunto de numeros','Nome de uma cidade','Cruzamento de uma estrada'],
                    ['Na frase: "Chegou Pedro, Maria e o seu filho dela",\n o pronome possessivo está reforçado para:', 'clareza', 'figura de harmonia', 'elegância e estilo', 'ênfase']]],
      
      ['Ciência', [['Qual bicho transmite Doença de Chagas?', 'Barbeiro', 'Pulga', 'Barata', 'Abelha'], 
                   ['Quais os tipos de ondas ultilizamos \npara receber e fazer telefonemas no celular?', 'Ondas de rádio','Ondas Aquaticas','Ondas sonoras ','Ondas espaciais'],
                   ['Na cadeia alimentar planta → gafanhoto → sapo\n → cobra → fungos e bactérias, o sapo participa\n da transferência de energia como:', 'Consumidor secundário', 'Consumidor de primeira ordem', 'Consumidor primário', 'Consumidor de terceira ordem']]]
    ]

    
    self.telaPrincipal()
    
  def telaPrincipal(self):
    self.janela.geometry('600x500')
    self.janela.title('Extreme Quiz Game')
    self.janela.resizable(False, False)

    self.lb = Label(self.janela, width=600, height=500, bg = 'Red')
    self.lb.pack()
    
    self.menu = Menu(self.janela)
    self.opcoesmenu = Menu(self.menu, tearoff=0)
    self.opcoesmenu.add_command(label= 'Voltar a tela inicial',command=lambda: self.voltartelainicial())
    self.menu.add_cascade(label = 'Opcões', menu= self.opcoesmenu)
    self.janela.config(menu=self.opcoesmenu)

    self.labelmensagem = Label(self.lb, text = 'Extreme Quiz Game', font = 'Calibri 20 bold', bg = 'White', width=43, height=2)
    self.labelmensagem.place(x=0, y=180)

    self.jogar = Button(self.lb, text='Jogar', bg = 'Red', font= 'Calibri 20', foreground= 'White', padx = 15, pady = 2, command=lambda: self.telaMaterias())
    self.jogar.place(x=250, y=300)

    self.janela.mainloop()

  
  def telaMaterias(self):
    ck_mat = IntVar()
    ck_varied = IntVar()
    ck_port = IntVar()
    ck_hist = IntVar()
    ck_cien = IntVar()
    ck_filo = IntVar()
    ck_ing = IntVar()
    ck_geo = IntVar()
    
    
    self.lb.destroy()
    
    self.lb1 = Label(self.janela, width=600, height=500, bg = '#f0f0f0')
    self.lb1.pack()
    
    self.lbescolha = Label(self.lb1,text='Escolha a(s) sua(s) matéria(s) para prosseguir:', font = 'Calibri 15', bg = 'Red', foreground= 'White', width=58, height=5)
    self.lbescolha.place(x=5, y=5)

    self.go = Button(self.lb1, text='Go!', font = 'Calibri 15', bg = 'Red', foreground= 'White', command=lambda: self.perguntaSelecionar(ck_mat,ck_cien, ck_varied, ck_port, ck_hist, ck_filo, ck_geo ,ck_ing))
    self.go.place(x=550, y=455)
    
    self.portugues= Checkbutton(self.lb1, text='Português', font = 'Calibri 15', variable = ck_port, onvalue=1, offvalue=0)
    self.portugues.place(x=75, y=190)

    self.matematica = Checkbutton(self.lb1, text='Matemática', font = 'Calibri 15', variable = ck_mat, onvalue=1, offvalue=0)
    self.matematica.place(x=75, y=270)

    self.variedades = Checkbutton(self.lb1, text='Variedades', font = 'Calibri 15', variable = ck_varied, onvalue=1, offvalue=0)
    self.variedades.place(x=75, y=350)

    self.historia = Checkbutton(self.lb1, text='História', font = 'Calibri 15', variable = ck_hist, onvalue=1, offvalue=0)
    self.historia.place(x=75, y=430)
    
    self.ciencias = Checkbutton(self.lb1, text='Ciências', font = 'Calibri 15', variable = ck_cien, onvalue=1, offvalue=0)
    self.ciencias.place(x=350, y=190)

    self.geografia = Checkbutton(self.lb1, text='Geografia', font = 'Calibri 15', variable = ck_geo, onvalue=1, offvalue=0)
    self.geografia.place(x=350, y=270)

    self.ingles = Checkbutton(self.lb1, text='Inglês', font = 'Calibri 15', variable = ck_ing, onvalue=1, offvalue=0)
    self.ingles.place(x=350, y=350)

    self.filosofia = Checkbutton(self.lb1, text='Filosofia', font = 'Calibri 15', variable = ck_filo, onvalue=1, offvalue=0)
    self.filosofia.place(x=350, y=430)


  def perguntaSelecionar(self, ck_mat,ck_cien, ck_varied, ck_port, ck_hist, ck_filo, ck_geo ,ck_ing):
    self.perguntasSelecionadas = []
    self.numerodequestoes = 0
    if ck_mat.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[0][1][0])
      self.perguntasSelecionadas.append(self.questoes[0][1][1])
      self.perguntasSelecionadas.append(self.questoes[0][1][2])
      self.numerodequestoes+=3
   
    if ck_varied.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[1][1][0])
      self.perguntasSelecionadas.append(self.questoes[1][1][1])
      self.perguntasSelecionadas.append(self.questoes[1][1][2])
      self.numerodequestoes+=3

    if ck_hist.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[2][1][0])
      self.perguntasSelecionadas.append(self.questoes[2][1][1])
      self.perguntasSelecionadas.append(self.questoes[2][1][2])
      self.numerodequestoes+=3

    if ck_geo.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[3][1][0])
      self.perguntasSelecionadas.append(self.questoes[3][1][1])
      self.perguntasSelecionadas.append(self.questoes[3][1][2])
      self.numerodequestoes+=3

    if ck_ing.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[4][1][0])
      self.perguntasSelecionadas.append(self.questoes[4][1][1])
      self.perguntasSelecionadas.append(self.questoes[4][1][2])
      self.numerodequestoes+=3

    if ck_filo.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[5][1][0])
      self.perguntasSelecionadas.append(self.questoes[5][1][1])
      self.perguntasSelecionadas.append(self.questoes[5][1][2])
      self.numerodequestoes+=3

    if ck_port.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[6][1][0])
      self.perguntasSelecionadas.append(self.questoes[6][1][1])
      self.perguntasSelecionadas.append(self.questoes[6][1][2])
      self.numerodequestoes+=3

    if ck_cien.get() == 1:
      self.perguntasSelecionadas.append(self.questoes[7][1][0])
      self.perguntasSelecionadas.append(self.questoes[7][1][1])
      self.perguntasSelecionadas.append(self.questoes[7][1][2])
      self.numerodequestoes+=3
      
    if self.perguntasSelecionadas == []:
      return

    self.embaralhamentoPerguntas()


  def embaralhamentoPerguntas(self):
    self.perguntaEmbaralhada = []
    self.num_perguntas = len(self.perguntasSelecionadas) -1
    
    cont = True
    while cont:
      num_aleatorio = random.randint(0, self.num_perguntas)
      perg = self.perguntasSelecionadas[num_aleatorio]
      if perg not in self.perguntaEmbaralhada:
        self.perguntaEmbaralhada.append(perg)
        if len(self.perguntaEmbaralhada) == self.num_perguntas + 1:
          cont = False
          
    self.embaralhaalternativas()

  def embaralhaalternativas(self):
    numAlternativas = 4
    self.novalista = []

    for j in self.perguntaEmbaralhada:
   
      self.conteudo_tela = []
      self.conteudo_tela.append(j[0])
      self.alternativa = []
     
      cont = True
      while cont:
        numAleatorio = random.randint(1, numAlternativas)
        self.alternativa = j[numAleatorio]
        if self.conteudo_tela not in self.novalista:
          self.novalista.append(self.conteudo_tela)
        
        if self.alternativa not in self.conteudo_tela:
          self.conteudo_tela.append(self.alternativa)  
        elif self.alternativa in self.conteudo_tela:
          pass
        if len(self.conteudo_tela) == len(j):
            cont=False
  
    self.numero=0
    self.pontos=0
    self.telaPerguntas()
    self.colocandoperguntas()
          
  def colocandoperguntas(self):
    
    numero = self.numero
    self.lbpergunta['text'] = self.novalista[numero][0]
    self.rb1['text'] =self.novalista[numero][1]
    self.rb2['text'] =self.novalista[numero][2]
    self.rb3['text'] =self.novalista[numero][3]
    self.rb4['text'] =self.novalista[numero][4]
    
    self.seleccao = self.selecao.get()

    if self.seleccao == 10:
      print(str(self.rb1['text']))
      if str(self.rb1['text']) == self.perguntaEmbaralhada[numero][1] and self.numerodequestoes >= len(self.novalista):
        self.pontos +=1
        self.numero+=1
        numero = self.numero
        print(self.numero)
        if numero>=len(self.novalista):
          self.telaFinal()
        else:
          self.lbpergunta['text'] = self.novalista[numero][0]
          self.rb1['text'] =self.novalista[numero][1]
          self.rb2['text'] =self.novalista[numero][2]
          self.rb3['text'] =self.novalista[numero][3]
          self.rb4['text'] =self.novalista[numero][4]
      else:
        self.telaFinal()
    elif self.seleccao == 20:
      print(str(self.rb2['text']))
      if str(self.rb2['text'])== self.perguntaEmbaralhada[numero][1]and self.numerodequestoes >= len(self.novalista):
        self.pontos +=1
        self.numero+=1
        numero = self.numero
        if numero>=len(self.novalista):
          self.telaFinal()
        else:
          self.lbpergunta['text'] = self.novalista[numero][0]
          self.rb1['text'] =self.novalista[numero][1]
          self.rb2['text'] =self.novalista[numero][2]
          self.rb3['text'] =self.novalista[numero][3]
          self.rb4['text'] =self.novalista[numero][4]
      else:
        self.telaFinal()
    elif self.seleccao ==30:
      print(str(self.rb3['text']))
      if str(self.rb3['text']) == self.perguntaEmbaralhada[numero][1]and self.numerodequestoes >= len(self.novalista):
        self.pontos +=1
        self.numero+=1
        numero = self.numero
        print(self.numero)
        if numero>=len(self.novalista):
          self.telaFinal()
        else:
          self.lbpergunta['text'] = self.novalista[numero][0]
          self.rb1['text'] =self.novalista[numero][1]
          self.rb2['text'] =self.novalista[numero][2]
          self.rb3['text'] =self.novalista[numero][3]
          self.rb4['text'] =self.novalista[numero][4]
    
      else:
        self.telaFinal()
    elif self.seleccao ==40:
      print(str(self.rb4['text']))
      if str(self.rb4['text']) == self.perguntaEmbaralhada[numero][1] and self.numerodequestoes >= len(self.novalista):
        self.pontos +=1
        self.numero+=1
        numero = self.numero
        print(self.numero)
        if numero>=len(self.novalista):
          self.telaFinal()
        else:
          self.lbpergunta['text'] = self.novalista[numero][0]
          self.rb1['text'] =self.novalista[numero][1]
          self.rb2['text'] =self.novalista[numero][2]
          self.rb3['text'] =self.novalista[numero][3]
          self.rb4['text'] =self.novalista[numero][4]
     
      else:
        self.telaFinal()
   
    

  def telaPerguntas(self):

    self.lb1.destroy()

    self.lb2 = Label(self.janela, width=600, height=500, bg = 'Red')
    self.lb2.pack()

    self.lbpergunta = Label(self.lb2, text=self.conteudo_tela, font = 'Calibri 15', bg = 'Red', foreground= 'White', width=58, height=7)
    self.lbpergunta.place(x=5, y=5)

    self.lbalternativa = Label(self.lb2, bg = '#f0f0f0', width=83, height=18)
    self.lbalternativa.place(x=5, y=205)

    self.proxpergunta = Button(self.lbalternativa, text='Próxima pergunta', bg = 'red', foreground='White', font = 'Calibri 12', command=lambda: self.colocandoperguntas())
    self.proxpergunta.place(x=455, y=240)

    self.selecao = IntVar()

    self.rb1 = Radiobutton(self.lbalternativa, text='Alternativa1', font = 'Calibri 15', value = 10, variable= self.selecao)
    self.rb1.place(x=5, y=5)

    self.rb2 = Radiobutton(self.lbalternativa, text='Alternativa2', font = 'Calibri 15', value = 20, variable= self.selecao)
    self.rb2.place(x=5, y=80)

    self.rb3 = Radiobutton(self.lbalternativa, text='Alternativa3', font = 'Calibri 15', value = 30, variable= self.selecao)
    self.rb3.place(x=5, y=155)

    self.rb4 = Radiobutton(self.lbalternativa, text='Alternativa4', font = 'Calibri 15', value = 40, variable= self.selecao)

    self.rb4.place(x=5, y=230)


  def telaFinal(self):
    self.lb2.destroy()

    self.lb3 = Label(self.janela, text = f'Você acertou {int(self.pontos)} questões', font = 'Calibri 20 bold', width=600, height=500, bg = '#f0f0f0')
    self.lb3.pack()

    self.lbfinal = Label(self.lb3, text='Final de Jogo', font = 'Calibri 20 bold', bg = 'Red', width=43, height=2)
    self.lbfinal.place(x=0, y=0)

    self.telainicial = Button(self.lb3, text='Voltar para tela inicial', font = 'Calibri 12', bg = 'red', foreground='White', command= lambda: self.voltar())
    self.telainicial.place(x=438, y=460) 

  
  def voltar(self):
    self.lb3.destroy()
    self.telaPrincipal()
    

  def voltartelainicial(self):
    self.janela.destroy()
    from telainicial import Telainicial
    Telainicial()