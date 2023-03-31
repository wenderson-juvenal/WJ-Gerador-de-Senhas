import random
import string
import pyperclip

def generatePassword(window, QMessageBox, label, passSize, upperCase, lowerCase, num, specialChar):
    # caso usuário não digite o tamanho da senha
    if not passSize:
        QMessageBox.warning(window, "Erro", "Adicione o tamanho da senha")
        return
    
    # caso usurário digite algo diferente de números inteiros no tamanho da senha
    try:
        passSize = int(passSize)
    except:
        QMessageBox.warning(window, "Erro", "Tamanho da senha deve conter apenas números inteiros")
        return
    
    # caso usuário não marque nenhuma das opções de caracteres
    charOptions = {
        'upper': upperCase,
        'lower': lowerCase,
        'num': num,
        'special': specialChar
    }
    if not any(charOptions.values()):
        QMessageBox.warning(window, "Error", "Selecione pelo menos uma opção de caracteres.")
        return
    
    # adicionando os caracteres de acordo com as opções marcadas pelo usuário
    upperCase = string.ascii_uppercase if upperCase==True else ""
    lowerCase = string.ascii_lowercase if lowerCase==True else ""
    num = string.digits if num==True else ""
    specialChar = string.punctuation if specialChar==True else ""

    # criando a senha
    password = "".join(random.choice(upperCase + lowerCase + num + specialChar) for _ in range(passSize))
    
    # quebrando o texto da senha
    label.setText("\n".join([password[i:i+27] for i in range(0, len(password), 27)]))


def copyText(label):
    pyperclip.copy(label.text())
