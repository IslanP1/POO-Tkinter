from tkinter import *


class Funcionamento():
  def __init__(self):

    self.janela = Tk()
    self.texto = """                                                                                                                              Projeto máquina virtual com python

                            Nosso projeto constituem as seguintes aplicações: 

              Agenda telefônica
              Calculadora
              Editor de Texto
              Extreme Quiz Game 
              Galeria
              Navegador


                            Nossa máquina virtual realiza diversas funções além da utilização dos apps, como mostrar uma tela inicial parecida com o Windows, contendo uma barra de\n             pesquisa e hora em tempo real. Podemos digitar qualquer texto na barra, que o mesmo será pesquisado em uma aba do navegador, enquanto a hora atualiza\n             constantemente.

              Agenda Telefônica: Realiza cadastro de nomes, telefones e emails e os guarda em um banco de dados.

              Calculadora: Realiza as seguintes operações matemáticas, soma, subtração, multiplicação, divisão, porcentagem, raiz quadrada.

              Editor de Texto: Realiza as funções de um editor comum, aumentando e diminuindo a letra, mudando a fonte, cor, negrito, além de salvar e abrir documentos\n              pelo computador. 

              Extreme Quiz Game: O extreme quiz game é um jogo construído com várias matérias e variadas perguntas, na qual ficam aleatórias conforme o código for\n              executado.

              Galeria: Passa imagens já adicionadas. 

              Navegador: Faz pesquisas na internet, além de levar para sites específicos, como Google, Instagram, Twitter, Youtube e Yahoo.

              Grupo: José Henrique Araujo da Silva, Gustavo Pereira Marcena da Cruz e Islan Pereira de Oliveira.
 
    
    """

    self.janela.geometry('1280x701')
    self.janela.resizable(False, False)
    self.label = Label(self.janela, text=self.texto, justify='left', font='Calibri 13')
    
    self.label.place(x=0, y=0)

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





"""

Referências(imagens e perguntas do jogo):

https://www.escolhaviajar.com/wp-content/uploads/2021/03/fotos-de-paris-museu-do-louvre-3.jpg

https://a.cdn-hotels.com/gdcs/production164/d1916/76adf5d6-a867-49c6-872d-524b3ca73da5.jpg

https://www.soportugues.com.br/secoes/jogos/quiz/

https://buzzfeed.com.br/quiz/estas-perguntas-foram-feitas-no-show-do-milhao-quantas-voce-consegue-acertar

https://www.todamateria.com.br/quiz-de-ingles/

https://www.google.com/url?sa=i&url=https%3A%2F%2Fautoesporte.globo.com%2Fcuriosidades%2Fnoticia%2F2022%2F02%2 Mercedes-mostra-w13-traz-de-volta-a-cor-prata-para-a-f1-2022-e-hamilton-dá-fim-a-polemica.ghtml&psig=AOvVaw2j1wuQNPTqzawgdSrDhylP&ust=1647037870096000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNCp-9bSvPYCFQAAAAAdAAAAABAD

https://www.google.com/url?sa=i&url=https%3A%2F%2Fge.globo.com%2Fmotor%2Fformula-1%2Fnoticia%2Fferrari-revela-f1-75-carro-da-f1-2022-que-homenageia-historia-do-time.ghtml&psig=AOvVaw34Wr9kHomvDv6ETpRJUmyY&ust=1647038032363000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOi_9NXSvPYCFQAAAAAdAAAAABAD

https://blog.nascenteazul.com.br/paisagens-naturais/

https://viagemeturismo.abril.com.br/materias/estas-fotos-sao-do-planeta-terra-sim-mais-especificamente-dos-paises-nordicos/

https://www.todamateria.com.br/exercicios-de-filosofia/#:~:text=Alternativa%20correta%3A%20a)%20"Penso,deveria%20ser%20indubitável%20(inquestionável).

https://www.todamateria.com.br/exercicios-sobre-cadeia-alimentar/

https://www.todamateria.com.br/exercicios-de-pronomes/#:~:text=Alternativa%20d%3A%20clareza.,de%20Pedro%20e%20de%20Maria.

"""
