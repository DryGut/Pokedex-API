from tkinter import *
import json
from PIL import ImageTk, Image

class App():

  def __init__(self, master=None, child=None):
    """inicializa o App"""

    self.pokemon = []
    
    self.fonte = ("Verdana", "10")
    
    self.master = Frame(master)
    self.master['padx'] = 20
    self.master['pady'] = 15
    self.master.pack()

 
    self.child = Frame(child)
    self.child['padx'] = 5
    self.child['pady'] = 5
    self.child.pack()
  
  #função do layout para pesquisa do pokemon
  def l_pesquisa(self):
    """ Tela Principal com a opção de busca"""
  
    self.title = Label(self.master, text='Pokesim, Pokenão, Pokesim, Pokemon')
    self.title['pady'] = 5
    self.title['font'] = ('Calibre', '10', 'bold')
    self.title.pack()

    self.lblnome = Label(self.child, text='Nome do Pokemon:', font=self.fonte, width=15)
    self.lblnome.pack()
    self.txtnome = Entry(self.child)
    self.txtnome['width'] = 20
    self.txtnome['font'] = self.fonte
    self.txtnome.pack()

    self.btnBuscar = Button(self.child, text='Buscar', font=self.fonte, width=5)
    self.btnBuscar['command'] = self.exibir_pokemon
    self.btnBuscar.pack()
 
  #função com a estrutura do perfil do pokemon sendo mostrado em um janela pop-up
  def exibir_pokemon(self):
    """ Tela onde será mostrado o Pokemon pesquisado """
    
    top = Toplevel()
    top.title('Eu Escolho Você')
    top.geometry('350x300')

    n = self.txtnome.get()
    self.pokemon = n
    self.txtnome.delete(0, END)

    with open('listapokemon.json', 'r') as arq:
      pokelist = json.load(arq)
      for poke in pokelist:
        if self.pokemon in poke['name']:
          label0 = Label(top, text=poke['name'].title(), fg='red')
          label0.pack()
          
          img = ImageTk.PhotoImage(Image.open(f"sprites/{poke['sprite']}"))
          label1 = Label(top, image=img) 
          label1.image = img  #mantem uma referencia para que a imagem seja mostrada no widget
          label1.pack()
          
          label2 = Label(top, text=[i.title() for i in poke['types']], fg='green')
          label2.pack()
          
          label3 = Label(top, text=[i.title() for i in poke['ability']], fg='blue')
          label3.pack()
          for skill in poke['stats']:
            for key, value in skill.items():
              label4 = Label(top, text=key+' - '+str(value))
              label4.pack()
          
          
          

root = Tk()
app = App(root)
root.title("Pokedex Marota")
root.geometry('450x290')

##### Cria o menu de navegação do Sistema #####

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Buscar Pokemon', command=app.l_pesquisa())

filemenu.add_separator()
filemenu.add_command(label='Sair', command=root.quit)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


root.mainloop()