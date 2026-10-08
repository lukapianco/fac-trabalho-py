#Variaveis
pecas_aprovadas = []
pecas_reprovadas = []

def cadastrar_peca():
    print("\n--- CADASTRAR NOVA PEÇA ---")
    id_peca = input("ID da peça: ")
    
    try:
        peso = float(input("Peso (g): "))
        cor = input("Cor: ").strip().lower()
        comprimento = float(input("Comprimento (cm): "))
    except ValueError:
        print("Erro: Digite números válidos para peso e comprimento.")
        return

    motivos_reprovacao = []
    
    #Criterios de qualidade
    if not (95 <= peso <= 105):
        motivos_reprovacao.append("Peso fora do padrão (95g - 105g)")
    if cor not in ["azul", "verde"]:
        motivos_reprovacao.append("Cor inválida (permitido: azul, verde)")
    if not (10 <= comprimento <= 20):
        motivos_reprovacao.append("Comprimento fora do padrão (10cm - 20cm)")

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    if motivos_reprovacao:
        peca["motivos"] = motivos_reprovacao
        pecas_reprovadas.append(peca)
        print("\n=> Peça REPROVADA e registrada.")
    else:
        pecas_aprovadas.append(peca)
        print("\n=> Peça APROVADA e armazenada.")
        
        #fechamento de caixas
        if len(pecas_aprovadas) % 10 == 0:
            print(f"*** ALERTA: Uma nova caixa foi fechada com 10 peças! Total de caixas fechadas: {len(pecas_aprovadas) // 10} ***")

def listar_pecas():
    print("\n--- PEÇAS APROVADAS ---")
    if not pecas_aprovadas:
        print("Nenhuma peça aprovada.")
    for p in pecas_aprovadas:
        print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm")

    print("\n--- PEÇAS REPROVADAS ---")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada.")
    for p in pecas_reprovadas:
        print(f"ID: {p['id']} | Motivo(s): {', '.join(p['motivos'])}")

def remover_peca():
    id_remover = input("\nDigite o ID da peça a ser removida: ")
    removida = False

    for peca in pecas_aprovadas:
        if peca['id'] == id_remover:
            pecas_aprovadas.remove(peca)
            print(f"Peça {id_remover} removida da lista de APROVADAS.")
            removida = True
            break

    if not removida:
        for peca in pecas_reprovadas:
            if peca['id'] == id_remover:
                pecas_reprovadas.remove(peca)
                print(f"Peça {id_remover} removida da lista de REPROVADAS.")
                removida = True
                break

    if not removida:
        print("Peça não encontrada no sistema.")

def listar_caixas_fechadas():
    total_caixas = len(pecas_aprovadas) // 10
    print(f"\n--- CAIXAS FECHADAS: {total_caixas} ---")
    
    for i in range(total_caixas):
        inicio = i * 10
        fim = inicio + 10
        caixa = pecas_aprovadas[inicio:fim]
        print(f"\nCaixa {i + 1}:")
        for p in caixa:
            print(f"  - ID: {p['id']}")

def gerar_relatorio():
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    caixas_fechadas = total_aprovadas // 10
    
    print("\n" + "="*30)
    print("RELATÓRIO CONSOLIDADO FINAL")
    print("="*30)
    print(f"Total de peças produzidas: {total_aprovadas + total_reprovadas}")
    print(f"Total de peças aprovadas:  {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Quantidade de caixas utilizadas (completas): {caixas_fechadas}")
    
    if pecas_reprovadas:
        print("\nMotivos das Reprovações:")
        for p in pecas_reprovadas:
            print(f" - ID {p['id']}: {', '.join(p['motivos'])}")
    print("="*30)

def menu():
    while True:
        print("\n" + "-"*30)
        print("SISTEMA DE GESTÃO DE PEÇAS")
        print("-"*30)
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar_peca()
        elif opcao == '2': listar_pecas()
        elif opcao == '3': remover_peca()
        elif opcao == '4': listar_caixas_fechadas()
        elif opcao == '5': gerar_relatorio()
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()