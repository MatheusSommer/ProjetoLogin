import tkinter as tk

""""" PROJETO LOGIN COM INTEFACE GRAFICA"""
" Disponivel no GITHUB de MatheusSommer"



def on_entry_click(event, entry, placeholder):
    """Função para adicionar o placeholder ao campo quando ele estiver vazio e não focado"""
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='gray')

def off_entry_click(event, entry, placeholder):
    """Função para remover o placeholder quando o usuário começar a digitar"""
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')  # Mudando a cor do texto para preto quando o usuário começa a digitar

# Função para mostrar e ocultar a senha
def toggle_senha():
    if entrada_senha.cget('show') == '*':  # Verifica se a senha está oculta
        entrada_senha.config(show='')  # Exibe a senha (remove o asterisco)
        botao_olho.config(text='🔒')  # Muda o texto do botão para cadeado (senha visível)
    else:
        entrada_senha.config(show='*')  # Oculta a senha (coloca o asterisco novamente)
        botao_olho.config(text='👁')  # Muda o texto do botão para o emoji de olho (senha oculta)


# Função de login
def validar_login():
    usuario = entrada_usuario.get()  # Pega o valor do campo de usuário
    senha = entrada_senha.get()      # Pega o valor do campo de senha

    # Verificar se o usuário e a senha são válidos
    """ nessa parte voce pode ultilizar um banco de dados para guardar varias senhas e emails do seu usuario"""
    if usuario == 'matheusduartesommer@gmail.com' and senha == '1234':
        resultado_login.config(text='Login feito com sucesso!', fg='green')
    
    else:
        resultado_login.config(text='Login incorreto', fg='red')


# Criação da janela principal
app = tk.Tk()

# Colocar o título da aplicação
app.title('SISTEMA DE LOGIN')

# Colocar o tamanho da aplicação
app.geometry('400x450')

# Colocar o fundo da aplicação
app.configure(background='black')

# Estilizando as fontes
font_padrao = ("Arial", 12)
font_titulo = ("Arial", 14, "bold")

# Campos utilizados
# Label para o campo de usuário
campo_usuario = tk.Label(app, text='Email', bg='black', fg='white', font=font_titulo)
campo_usuario.pack(pady=10)

# Entry para o campo de usuário
entrada_usuario = tk.Entry(app, bg='white', fg='black', font=font_padrao, bd=2, relief="solid")
entrada_usuario.pack(pady=10, padx=20, ipadx=5)  # Adiciona o padding para alinhar com o campo de senha
placeholder_usuario = "Digite seu Email"
entrada_usuario.insert(0, placeholder_usuario)
entrada_usuario.config(fg='gray')

# Adicionando eventos para o placeholder
entrada_usuario.bind("<FocusIn>", lambda event: off_entry_click(event, entrada_usuario, placeholder_usuario))
entrada_usuario.bind("<FocusOut>", lambda event: on_entry_click(event, entrada_usuario, placeholder_usuario))

# Label para o campo de senha
campo_senha = tk.Label(app, text='Senha', bg='black', fg='white', font=font_titulo)
campo_senha.pack(pady=10)

# Frame para colocar o campo de senha e o botão de mostrar/ocultar juntos
frame_senha = tk.Frame(app, bg='black')
frame_senha.pack(pady=1)

# Entry para o campo de senha
entrada_senha = tk.Entry(frame_senha, bg='white', fg='black', font=font_padrao, bd=2, relief="solid", show="*")
entrada_senha.pack(side=tk.LEFT, padx=10)  # O mesmo padding horizontal para alinhar com o campo de usuário

# Botão para mostrar/ocultar senha com emoji
botao_olho = tk.Button(frame_senha, text='👁', bg='black', fg='white', font=("Arial", 14), relief="solid", command=toggle_senha)
botao_olho.pack(side=tk.LEFT, padx=5)  # Isso vai colocar o botão ao lado do campo de senha

# Adicionando eventos para o placeholder
placeholder_senha = "Digite sua senha"
entrada_senha.insert(0, placeholder_senha)
entrada_senha.config(fg='gray')
entrada_senha.bind("<FocusIn>", lambda event: off_entry_click(event, entrada_senha, placeholder_senha))
entrada_senha.bind("<FocusOut>", lambda event: on_entry_click(event, entrada_senha, placeholder_senha))

# Button para o botão de login
botao_login = tk.Button(app, text='Login', bg='#4CAF50', fg='white', font=("Arial", 14, "bold"), relief="solid", command=validar_login)
botao_login.pack(pady=20, ipadx=20, ipady=10)

# Campo feedback de login
resultado_login = tk.Label(app, text='', bg='black', fg='white', font=("Arial", 12))
resultado_login.pack(pady=10)

# Iniciar a aplicação
app.mainloop()
