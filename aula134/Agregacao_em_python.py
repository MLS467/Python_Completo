# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).


class Carrinho:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self,produto):
        self.produtos.append(produto)
        return True
    
    def valor_total(self):
        total = sum([
            produto.preco
            for produto in self.produtos 
        ])
        print(f"Valor total: R${total:.2f}")
        return
    
    def lista_produtos(self):
        for index,produto in enumerate(self.produtos):
            print(f"{index+1}--> Produto: {produto.nome} Preço: R${produto.preco:.2f}")

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

p1,p2 = Produto("Batata",1.5), Produto("Feijao", 20.75)
p3 = Produto("Fusca",500)
p4 = Produto("Brasilia",1500)

carrinho = Carrinho()

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)


carrinho.lista_produtos()

carrinho.valor_total()

