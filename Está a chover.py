esta_a_chover = input("Está a chover? (sim/nao): ").lower()

if esta_a_chover == "sim":
    tem_chapeu_de_chuva = input("Você tem um guarda-chuva? (sim/nao): ").lower()

    if tem_chapeu_de_chuva == "sim":
        print("Pode sair, mas não se esqueça do guarda-chuva!")
    else:
        print("Deveria pegar um guarda-chuva antes de sair.")
else:
    print("Como não está a chover, você pode sair sem problemas.")
