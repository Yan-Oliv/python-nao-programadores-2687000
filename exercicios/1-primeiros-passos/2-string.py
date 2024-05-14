resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
print('Var resumo:', resumo)

# Imprima na tela apenas a segunda letra da variável
print('Segunda letra da var resumo:', resumo[1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")
print('Idade Paloma:', 46)

# Imprima na tela o trecho final da variável
print('Trecho final da var resumo:', resumo[30:])

# Converta todos as letras para minúsculo e imprima na tela
print('Var minúscula:', resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela
print('Var maiúscula:', resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print('Var primeiras letras maiúscula:', resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print('Var primeira letra maiúscula:', resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
idade = 46
print(f"Paloma é uma mulher de {idade} anos que deseja mudar de profissão, por isso está estudando 'python'.")
