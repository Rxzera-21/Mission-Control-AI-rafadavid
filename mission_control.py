# =============================================================
# MISSION CONTROL AI
# GS2026.1 - Pensamento Computacional e Automação com Python
# =============================================================

NOME_EQUIPE = "Equipe Ravid"

# Matriz principal: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [23, 95, 91, 98, 93],   # Ciclo 1 — início da missão
    [26, 83, 75, 95, 87],   # Ciclo 2 — estabilização dos sistemas
    [32, 61, 54, 90, 68],   # Ciclo 3 — queda parcial de comunicação
    [37, 40, 35, 85, 52],   # Ciclo 4 — alerta de energia
    [41, 25, 17, 76, 33],   # Ciclo 5 — risco operacional
    [35, 52, 30, 80, 48],   # Ciclo 6 — tentativa de recuperação
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]

# -----------------------------------------------------------
# FUNÇÕES DE ANÁLISE POR SENSOR
# -----------------------------------------------------------

def analisar_temperatura(valor):
    """Classifica a temperatura e retorna (status, pontos, descricao)."""
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    """Classifica a comunicação e retorna (status, pontos, descricao)."""
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    """Classifica a bateria e retorna (status, pontos, descricao)."""
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    """Classifica o oxigênio e retorna (status, pontos, descricao)."""
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    """Classifica a estabilidade e retorna (status, pontos, descricao)."""
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# -----------------------------------------------------------
# FUNÇÕES DE CLASSIFICAÇÃO E RECOMENDAÇÃO
# -----------------------------------------------------------

def classificar_ciclo(pontuacao):
    """Retorna a classificação textual do ciclo com base na pontuação."""
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados_ciclo):
    """
    Gera uma recomendação com base nos sensores em estado crítico ou de atenção.
    resultados_ciclo: lista de (status, pontos, descricao) para cada sensor do ciclo.
    """
    criticos = []
    atencao  = []

    nomes_sensores = [
        "Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"
    ]
    acoes_criticas = {
        "Temperatura" : "verificar controle térmico da missão",
        "Comunicação" : "tentar restabelecer contato com a base",
        "Bateria"     : "ativar modo de economia de energia",
        "Oxigênio"    : "acionar protocolo de suporte à vida",
        "Estabilidade": "reduzir operações não essenciais",
    }

    for i, (status, _, _) in enumerate(resultados_ciclo):
        if status == "CRÍTICO":
            criticos.append(nomes_sensores[i])
        elif status == "ATENÇÃO":
            atencao.append(nomes_sensores[i])

    # Caso 1: tudo dentro do normal
    if not criticos and not atencao:
        return "Manter operação normal e continuar monitoramento."

    # Caso 2: situação grave — 3 ou mais sensores críticos
    if len(criticos) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

    # Caso 3: muitos sensores apenas em atenção, sem nenhum crítico
    if not criticos and len(atencao) >= 3:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    # Caso 4: recomendação detalhada por sensor
    partes = []
    for sensor in criticos:
        partes.append(acoes_criticas[sensor].capitalize())
    for sensor in atencao:
        partes.append(f"Monitorar {sensor.lower()}")

    return "; ".join(partes) + "."


def analisar_tendencia(riscos):
    """Compara risco do primeiro e do último ciclo e retorna string de tendência."""
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos_por_area):
    """Retorna o nome da área com maior pontuação acumulada."""
    maior_pontos = max(pontos_por_area)
    indice = pontos_por_area.index(maior_pontos)
    return areas_monitoradas[indice]


# -----------------------------------------------------------
# FUNÇÃO DE ANÁLISE DE UM CICLO
# -----------------------------------------------------------

def analisar_ciclo(ciclo):
    """
    Recebe uma linha da matriz e retorna lista de resultados por sensor.
    Cada item: (status, pontos, descricao)
    """
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    return [
        analisar_temperatura(temperatura),
        analisar_comunicacao(comunicacao),
        analisar_bateria(bateria),
        analisar_oxigenio(oxigenio),
        analisar_estabilidade(estabilidade),
    ]


# -----------------------------------------------------------
# EXIBIÇÃO DE CADA CICLO
# -----------------------------------------------------------

def exibir_ciclo(numero_ciclo, ciclo, resultados, pontuacao, classificacao, recomendacao):
    """Imprime no terminal as informações detalhadas de um ciclo, com colunas alinhadas."""
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo
    r_temp, r_com, r_bat, r_oxi, r_est = resultados

    # (rótulo, valor formatado, resultado do sensor)
    linhas = [
        ("Temperatura",  f"{temperatura} °C", r_temp),
        ("Comunicação",  f"{comunicacao}%",   r_com),
        ("Bateria",      f"{bateria}%",        r_bat),
        ("Oxigênio",     f"{oxigenio}%",       r_oxi),
        ("Estabilidade", f"{estabilidade}%",   r_est),
    ]

    print(f"\nCICLO {numero_ciclo}")
    print("-" * 60)
    for nome, valor, (status, _, descricao) in linhas:
        print(f"{nome + ':':<13} {valor:>6} | {status:<7} | {descricao}")
    print(f"\nPontuação de risco do ciclo: {pontuacao}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}")


# -----------------------------------------------------------
# RELATÓRIO FINAL
# -----------------------------------------------------------

def gerar_relatorio_final(riscos, pontos_por_area, tendencia, nome_missao):
    """Imprime o relatório consolidado da missão."""
    num_ciclos = len(dados_missao)

    # Média de cada coluna/sensor ao longo dos ciclos
    medias = []
    for col in range(5):
        total = sum(dados_missao[linha][col] for linha in range(num_ciclos))
        medias.append(total / num_ciclos)

    risco_medio   = sum(riscos) / num_ciclos
    ciclo_critico = riscos.index(max(riscos)) + 1
    maior_risco   = max(riscos)
    qtd_criticos  = sum(1 for r in riscos if r >= 6)
    area_afetada  = identificar_area_mais_afetada(pontos_por_area)

    # Classificação final com base na média de risco
    if risco_medio <= 2:
        class_final = "MISSÃO ESTÁVEL"
    elif risco_medio <= 5:
        class_final = "MISSÃO EM ATENÇÃO"
    else:
        class_final = "MISSÃO CRÍTICA"

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {num_ciclos}")
    print(f"\nMédia de temperatura:  {medias[0]:.2f} °C")
    print(f"Média de comunicação:  {medias[1]:.2f}%")
    print(f"Média de bateria:      {medias[2]:.2f}%")
    print(f"Média de oxigênio:     {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%")
    print(f"\nCiclo mais crítico:        Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco:  {maior_risco}")
    print(f"Risco médio da missão:     {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")
    print(f"\nTendência da missão:")
    print(f"  {tendencia}")
    print("\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontos_por_area[i]} pontos")
    print(f"\nÁrea mais afetada:")
    print(f"  {area_afetada}")
    print(f"\nClassificação final da missão:")
    print(f"  {class_final}")
    print("\nConclusão:")
    if class_final == "MISSÃO ESTÁVEL":
        conclusao = ("A missão transcorreu dentro dos parâmetros normais. "
                     "Todos os sistemas se mantiveram operacionais e o monitoramento "
                     "contínuo deve prosseguir como planejado.")
    elif class_final == "MISSÃO EM ATENÇÃO":
        conclusao = ("A missão apresentou instabilidade relevante durante a operação. "
                     "Apesar da tentativa de recuperação no último ciclo, ainda existem "
                     "sistemas em atenção e a equipe deve manter o plano de contingência ativo.")
    else:
        conclusao = ("A missão atingiu níveis críticos em múltiplos sistemas. "
                     "É necessária intervenção imediata, ativação do protocolo de emergência "
                     "e revisão completa dos subsistemas afetados.")
    print(f"  {conclusao}")
    print("=" * 60)


# -----------------------------------------------------------
# INTERFACE INICIAL
# -----------------------------------------------------------

def interface_inicial():
    """Exibe a tela de boas-vindas e solicita o nome da missão ao usuário."""
    print("=" * 60)
    print("        MISSION CONTROL AI")
    print("   Sistema de Monitoramento Espacial")
    print("=" * 60)
    print()
    print("Bem-vindo, Operador.")
    print("Antes de iniciar o monitoramento, precisamos")
    print("registrar as informações desta missão.")
    print()

    while True:
        nome = input(">>> Digite o nome da missão: ").strip()
        if nome:
            break
        print("    [ERRO] O nome da missão não pode estar vazio. Tente novamente.")

    print()
    print(f"    Missão '{nome}' registrada com sucesso.")
    print("    Iniciando sistema de monitoramento...")
    print()
    return nome


# -----------------------------------------------------------
# FUNÇÃO PRINCIPAL
# -----------------------------------------------------------

def main():
    nome_missao = interface_inicial()

    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos          = []
    pontos_por_area = [0] * 5   # acumulador de risco por coluna/sensor

    for i, ciclo in enumerate(dados_missao):
        resultados    = analisar_ciclo(ciclo)
        pontuacao     = sum(r[1] for r in resultados)
        classificacao = classificar_ciclo(pontuacao)
        recomendacao  = gerar_recomendacao(resultados)

        # Acumula pontos por área
        for j, (_, pts, _) in enumerate(resultados):
            pontos_por_area[j] += pts

        riscos.append(pontuacao)
        exibir_ciclo(i + 1, ciclo, resultados, pontuacao, classificacao, recomendacao)

    tendencia = analisar_tendencia(riscos)
    gerar_relatorio_final(riscos, pontos_por_area, tendencia, nome_missao)


if __name__ == "__main__":
    main()