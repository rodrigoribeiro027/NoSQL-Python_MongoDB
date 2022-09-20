import Produto.deletar as DeletarUsuario
import Usuario.deletar  as DeletarUsuario
import Usuario.update as AtualizacaoUsuario
import Usuario.CadastroCliente as CadastroCliente
import Usuario.FindQuery as BuscarUsuario
import Produto.Cadastro as CadastroProduto
import Produto.FindQuery as BuscarProdutos
import Produto.update as AtualizarProdutoByID
import Produto.deletar
import Compra.Cadastro as ComprarProduto

def CaseUsuario(mydb):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]CadastrarUsuario\n
        - [2]PegarUsuarios\n
        - [3]UsuariobyID\n
        - [4]DeletarUsuarioID testar\n
        - [5]Atualizar Usuario\n
        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                return
            case '1':
                CadastroCliente.CadastrarUsuario(mydb)
            case '2':
                BuscarUsuario.PegarUsuarios(mydb)
            case '3':
                BuscarUsuario.UsuariobyID(mydb)
            case '4':
                DeletarUsuario.DeletarUsuarioID(mydb)
            case '5':
                AtualizacaoUsuario.AtualizarUsuarioID(mydb)


def CaseProduto(mydb):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]CadastrarProduto\n
        - [2]Pegar Produtos\n
        - [3]buscar Produto por ID\n
        - [4]Atualizar Produto por ID\n
        - [5]Deletar Produto\n
        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                break
            case '1':
                CadastroProduto.CadastrarProduto(mydb)
            case '2':
                BuscarProdutos.PegarProdutos(mydb)
            case '3':
                BuscarProdutos.ProdutosbyID(mydb)
            case '4':
                AtualizarProdutoByID.AtualizarProdutoID(mydb)
            case '5':
                DeletarUsuario.DeletarUsuarioID(mydb)
                


def CaseCompra(mydb):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]ComprarProduto\n
        - [2]Deletar Compra\n
        - [3]buscar Compra\n
        - [4]Atualizar Compra\n
        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                break
            case '1':
                ComprarProduto.Compra(mydb)