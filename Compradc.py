print("Os planos são: 100mb, 200mb, 250mb, 500mb, 1gb, 2gb, 5gb")

credito = 0

vez = [0,0,0,0,0,0,0]

mais = "sim"

saldo = int(input("digite a quantidade de dinheiro que você irá gastar "))

while mais == "sim":
	quero = input("Qual plano vc quer ativar? 1, 2, 3, 4, 5, 6, 7\n")

	if quero == "1":
		print("o valor é: 5R$")
		pagou = input("digite o valor a ser pago ")
		if pagou == "5" :
			if int(saldo) - 5 >= 0:
				credito += 100
				saldo -= 5
				vez[0] += 1
				if vez[0] == 5:
					credito += 100 * 0.25
					print("Bônus de 25% adicionado")
					print("Obrigado, compra efetuada de 100mb e bônus de",int(100 * 0.25),"mb")
				else:
					print("Obrigado, compra efetuada de 100mb")
			else:
				print("Compra de 100mb não efetuada, dinheiro insuficiente")
		else:
			print("Compra de 100mb não efetuada")

	if quero == "2":
		print("o valor é: 8R$")
		pagou = input("digite o valor a ser pago ")
		if pagou == "8" :
			if int(saldo) - 8 >= 0:
				credito += 200
				saldo -= 8
				vez[1] += 1
				if vez[1] == 5:
					credito += 200 * 0.25
					print("Bônus de 25% adicionado")
					print("Obrigado, compra efetuada de 200mb e bônus de",int(200 * 0.25),"mb")
				else:
					print("Obrigado, compra efetuada de 200mb")
			else:
				print("Compra de 200mb não efetuada, dinheiro insuficiente")
		else:
			print("Compra de 200mb não efetuada") 

	if quero == "3":
		print("o valor é: 13R$")		
		pagou = input("digite o valor a ser pago ")
		if pagou == "13" :
			if int(saldo) - 13 >= 0:
				credito += 250
				saldo -= 13
				vez[2] += 1
				if vez[2] == 5:
					credito += 250 * 0.25
					print("Bônus de 25% adicionado")
					print("Obrigado, compra efetuada de 250mb e bônus de",int(250 * 0.25),"mb")
				else:
					print("Obrigado, compra efetuada de 250mb")
			else:
				print("Compra de 250mb não efetuada, dinheiro insuficiente")
		else:
			print("Compra de 250mb não efetuada")

	if quero == "4":
		print("o valor é: 18R$")
		pagou = input("digite o valor a ser pago ")
		if pagou == "18" :
			if int(saldo) - 18 >= 0:
				credito += 500
				saldo -= 18
				vez[3] += 1
				if vez[3] == 5:
					credito += 250 * 0.25
					print("Bônus de 25% adicionado")
					print("Obrigado, compra efetuada de 500mb e bônus de",int(500 * 0.25),"mb")
				else:
					print("Obrigado, compra efetuada de 500mb")
			else:
				print("Compra de 500mb não efetuada, dinheiro insuficiente")
		else:
			print("Compra de 500mb não efetuada")

	if quero == "5":
		print("o valor é: 20R$")
		pagou = input("digite o valor a ser pago ")
		if pagou == "20" :
			if int(saldo) - 20 >= 0:
				credito += 1000
				saldo -= 20
				vez[4] += 1
				if vez[4] == 5:
					credito += 250 * 0.25
					print("Bônus de 25% adicionado")
					print("Obrigado, compra efetuada de 1gb e bônus de",int(1000 * 0.25),"mb")
				else:
					print("Obrigado, compra efetuada de 1gb")
			else:
				print("Compra de 1gb não efetuada, dinheiro insuficiente")
		else:
			print("Compra de 1gb não efetuada")

	if quero == "6":
		print("o valor é: 22R$")
		pagou = input("digite o valor a ser pago ")
		if pagou == "22" :
			if int(saldo) - 22 >= 0:
				credito += 2000
				saldo -= 22
				vez[5] += 1
				if vez[5] == 5:
					credito += 250 * 0.25
					print("Bônus de 25% adicionado")
					print("Obrigado, compra efetuada de 2gb e bônus de",int(2000 * 0.25),"mb")
				else:
					print("Obrigado, compra efetuada de 2gb")
			else:
				print("Compra de 2gb não efetuada, dinheiro insuficiente")
		else:
			print("Compra de 2gb não efetuada")

	if quero == "7":
		print("o valor é: 25R$")
		pagou = input("digite o valor a ser pago ")
		if pagou == "25" :
			if int(saldo) - 25 >= 0:
				credito += 5000
				saldo -= 25
				vez[6] += 1
				if vez[6] == 5:
					credito += 250 * 0.25
					print("Bônus de 25% adicionado")
					print("Obrigado, compra efetuada de 5gb e bônus de",int(5000 * 0.25),"mb")
				else:
					print("Obrigado, compra efetuada de 5gb")
			else:
				print("Compra de 5gb não efetuada, dinheiro insuficiente")
		else:
			print("Compra de 5gb não efetuada")

	mais = input("quer fazer mais uma compra? ")
	quero = 0

if credito > 1000:
	credito = credito / 1000
	print("Seu crédito total é",credito,"gb")
else:
	print("Seu crédito total é",credito,"mb")

print("Sobrou",saldo,"R$")
