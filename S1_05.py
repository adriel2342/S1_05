while True:
    print("---CADASTROS DE ATIVOS DE TI---")
    nome_do_ativo = input("===NOME DO ATIVO===(ex: SERVIDOR WEB): ").strip().lower()
    ip_do_ativo = input("===IP DO ATIVO===(ex: 192.168.100.1): ").strip()
    risco_do_ativo = input("===RISCO DO ATIVO===(ex: Alto,Médio,Baixo,Crítico,Nenhum): ").strip().upper()
    print("===REVISÃO DOS ATIVOS CADASTRADOS===")
    print(f"===ATIVO CADASTRADO COM SUCESSO==={nome_do_ativo} - {ip_do_ativo} - {risco_do_ativo}")
    confirmação = input("As informações acima estão corretas? (Sim/Não):").strip().lower()
    if confirmação == "sim" or confirmação == "s":
        print("===Cadastro confirmado com sucesso!===")
        print("===Identificação dos tipos de variáveis===")
        print(f" tipo ->nome do ativo<-: {type(nome_do_ativo)}")
        print(f" tipo ->ip do ativo<-: {type(ip_do_ativo)}")
        print(f" tipo ->risco do ativo<-: {type(risco_do_ativo)}")
        novo_cadastro = input("Deseja cadastrar outro ativo? (Sim/Não):").strip().lower()   
        if novo_cadastro == "sim" or novo_cadastro == "s":
            print("===Iniciando novo cadastro!===")
        elif novo_cadastro == "não" or novo_cadastro == "n":
            print("===Nenhum novo cadastro iniciado!===")
            break
        else:
            print("===opçãao inválida encerrando o cadastro até logo.===")
            break
    elif confirmação == "não" or confirmação == "n":
        print("===Cadastro cancelado!===")
    else:
        print("===Opção inválida. Por favor, responda com 'Sim' ou 'Não'.===").lower() .strip()

          
