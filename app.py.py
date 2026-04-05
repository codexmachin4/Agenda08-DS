# Programa de Pesquisa de Satisfação - TudoWeb
# Coleta a opinião de 50 clientes sobre o atendimento

print("=" * 50)
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB   ")
print("=" * 50)
print("Opções de avaliação:")
print("1 - EXCELENTE")
print("2 - BOM")
print("3 - RUIM")
print("-" * 50)

# Inicializando os contadores
excelente = 0
bom = 0
ruim = 0

# Estrutura de repetição FOR para 50 entrevistados
for i in range(1, 51):
    print(f"\n--- Entrevistado {i} de 50 ---")
    
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    
    # Validação da opinião
    while True:
        try:
            opiniao = int(input("Digite sua opinião (1-EXCELENTE, 2-BOM, 3-RUIM): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Opção inválida! Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número (1, 2 ou 3).")
    
    # Contabilizando as respostas
    if opiniao == 1:
        excelente += 1
        classificacao = "EXCELENTE"
    elif opiniao == 2:
        bom += 1
        classificacao = "BOM"
    else:
        ruim += 1
        classificacao = "RUIM"
    
    print(f"✓ Avaliação registrada: {classificacao} - Obrigado, {nome}!")

# Exibição dos resultados finais
print("\n" + "=" * 50)
print("             RESULTADOS FINAIS          ")
print("=" * 50)
print(f"a) Quantidade de respostas EXCELENTE: {excelente}")
print(f"b) Quantidade de respostas RUIM: {ruim}")
print(f"c) Quantidade de respostas BOM: {bom} (informação complementar)")
print("=" * 50)
print("Pesquisa encerrada. Obrigado a todos os participantes!")