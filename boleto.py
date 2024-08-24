#questao1
boleto1=float(input("Digite o valor do primeiro boleto?"))
boleto2=float(input ("Digite o valor do segundo boleto"))
boleto3=float(input('Digite o valor do terceiro boleto'))
boleto4=float(input('Digite o valor do quarto boleto '))


salario_liquido=float(input('Digite o valor do  seu salario liquido ?'))

total_contas=boleto1+boleto2+boleto3+boleto4

valorrestantes=salario_liquido-total_contas 

print(f'valor do salario lquido e {salario_liquido}')

print(f'O valor que sobrou do salario restante e {valorrestantes}')

#questao 2
boleto1=float(input("Digite o valor do primeiro boleto?"))
boleto2=float(input ("Digite o valor do segundo boleto"))
boleto3=float(input('Digite o valor do terceiro boleto'))
boleto4=float(input('Digite o valor do quarto boleto '))


salariob=float(input('Digite o valor do  seu salario bruto ?'))
salario_liquido=salariob*(1-0.14)


total_contas=boleto1+boleto2+boleto3+boleto4

valorrestantes=salario_liquido-total_contas 

print(f'valor do salario lquido e {salario_liquido}')


print(f'O valor dos boletos para pagar{total_contas}')

print(f'O valor que sobrou do salario restante e {valorrestantes}')


