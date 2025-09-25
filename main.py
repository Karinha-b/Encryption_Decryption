from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()
    #Define senha
    if password=='123456':
        #Configuração da janela de criptografia
        screen2=Toplevel(screen)
        screen2.title('Decriptografia')
        screen2.geometry('400x200')
        screen2.configure(bg="#ad81e0")

        #Criptografa o texto
        message=text1.get(1.0,END)
        decode_message=message.encode('ascii')
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode('ascii')

        #Configuração do texto
        Label(screen2,text='Decriptografar', font='arial', fg='white', bg='#ad81e0').place(x=10,y=10)
        text2=Text(screen2, font='Robote 10', bg='white', relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40, width=380, height=150)

        text2.insert(END, decrypt)
    #Verificação de senha
    elif password=='':
        messagebox.showerror('Decriptografia','Insira a senha')
    elif password!='123456':
        messagebox.showerror('Decriptografia','Senha Incorreta')

def encrypt():
    password=code.get()
    #Define senha
    if password=='123456':
        #Configuração da janela de criptografia
        screen1=Toplevel(screen)
        screen1.title('Encryption')
        screen1.geometry('400x200')
        screen1.configure(bg="#e081b9")

        #Criptografa o texto
        message=text1.get(1.0,END)
        encode_message=message.encode('ascii')
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode('ascii')

        #Configuração do texto
        Label(screen1,text='Criptografar', font='arial', fg='white', bg='#e081b9').place(x=10,y=10)
        text2=Text(screen1, font='Robote 10', bg='white', relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40, width=380, height=150)

        text2.insert(END, encrypt)
    #Verificação de senha
    elif password=='':
        messagebox.showerror('Criptografia','Insira a senha')
    elif password!='123456':
        messagebox.showerror('Criptografia','Senha Incorreta')


def main_screen():

    global screen
    global code
    global text1

    #Configurações da janela
    screen=Tk()
    screen.geometry('540x400')

    screen.configure(bg="#8E8E92")

    #icon
    image_icon=PhotoImage(file='key.png')
    screen.iconphoto(False,image_icon)

    def reset():
        code.set('')
        text1.delete(1.0,END)

    #Titulo da aba
    screen.title('EDcryption APP')

    #Texto de instrução
    Label(text='Entre o texto que deseja encriptografar ou descriptografar', 
          fg='black', bg="#8E8E92", font=('calibri', 15)).place(x=10, y=10)
    
    #Caixa de texto para digitação
    text1=Text(font='Robote 20', bg='white', relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=40, width=520, height=150)

    #Campo para inserir a senha
    Label(text='Entre a palavra-chave', fg='black', bg="#8E8E92", font=('calibri', 15)).place(x=10, y=190)
    code=StringVar()
    entry = Entry(textvariable=code, font=('Robote', 20), show='☆', bd=0)
    entry.place(x=10, y=220, width=520, height=50)

    #Botões
    Button(text='CRIPTOGRAFAR', height='2',width=35, bg='#ed3833', fg='white', bd=0, command=encrypt).place(x=10, y=280)
    Button(text='DECRIPTOGRAFAR', height='2',width=35, bg='#00bd56', fg='white', bd=0, command=decrypt).place(x=278, y=280)
    Button(text='RESET', height='2', width=73, bg="#4431f3", fg='white', bd=0, command=reset).place(x=11, y=322)



    screen.mainloop()



main_screen()