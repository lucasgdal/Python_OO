
class Agenda:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def adicionar_contato(self):
        self.nome = input("Insira seu nome: ")
        self.telefone = input("Insira seu telefone: ")
        self.email = input("Insira seu e-mail: ")

    def mostra_lista(self):
        print("Nome:{} \n"
              "Telefone:{}\n"
              "E-mail: {}\n".format(self.nome, self.telefone, self.email))
