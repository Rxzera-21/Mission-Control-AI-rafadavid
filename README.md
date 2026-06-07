# 🚀 Mission Control AI
### GS2026.1 — Pensamento Computacional e Automação com Python

Sistema inteligente de monitoramento de missão espacial desenvolvido em **Python puro**, sem bibliotecas externas.

---

## 📋 Descrição

O **Mission Control AI** simula o acompanhamento de uma missão espacial experimental. Ao iniciar, o operador informa o **nome da missão** (ex.: *Prometheus Deep Scan*). O sistema então analisa **6 ciclos de monitoramento**, cada um com **5 sensores**, classifica o nível de risco de cada ciclo, gera recomendações automáticas, identifica a tendência geral da missão, aponta a área mais afetada e exibe um **relatório final completo** no terminal.

A "inteligência" do sistema é baseada inteiramente em **regras lógicas** (estruturas condicionais), conforme permitido pelo enunciado.

---

## 🗂️ Estrutura do repositório

```
mission-control-ai/
├── README.md
└── mission_control.py
```

---

## ▶️ Como executar

Pré-requisito: Python 3.x instalado (sem dependências externas).

```bash
python mission_control.py
```

Ao rodar, o programa pede o nome da missão e, em seguida, exibe a análise ciclo a ciclo e o relatório final.

---

## 📊 Estrutura dos dados

A matriz principal `dados_missao` contém **6 linhas (ciclos)** e **5 colunas (sensores)**. Cada linha segue exatamente a ordem `[temperatura, comunicacao, bateria, oxigenio, estabilidade]`.

| Posição | Sensor       | Unidade | Área monitorada            |
|---------|--------------|---------|----------------------------|
| 0       | Temperatura  | °C      | Temperatura interna        |
| 1       | Comunicação  | %       | Comunicação com a base     |
| 2       | Bateria      | %       | Sistema de energia         |
| 3       | Oxigênio     | %       | Suporte de oxigênio        |
| 4       | Estabilidade | %       | Estabilidade operacional   |

### Dados simulados utilizados neste projeto

```python
dados_missao = [
    [23, 95, 91, 98, 93],   # Ciclo 1 — início da missão
    [26, 83, 75, 95, 87],   # Ciclo 2 — estabilização dos sistemas
    [32, 61, 54, 90, 68],   # Ciclo 3 — queda parcial de comunicação
    [37, 40, 35, 85, 52],   # Ciclo 4 — alerta de energia
    [41, 25, 17, 76, 33],   # Ciclo 5 — risco operacional
    [35, 52, 30, 80, 48],   # Ciclo 6 — tentativa de recuperação
]
```

---

## 🔔 Regras de alerta

> Os limites abaixo seguem a sugestão do enunciado e estão implementados exatamente assim no código.

### Temperatura (°C)
| Condição             | Classificação |
|----------------------|---------------|
| menor que 18         | ATENÇÃO       |
| de 18 a 30           | NORMAL        |
| maior que 30 até 35  | ATENÇÃO       |
| maior que 35         | CRÍTICO       |

### Comunicação (%)
| Condição     | Classificação |
|--------------|---------------|
| menor que 30 | CRÍTICO       |
| de 30 a 59   | ATENÇÃO       |
| 60 ou mais   | NORMAL        |

### Bateria (%)
| Condição     | Classificação |
|--------------|---------------|
| menor que 20 | CRÍTICO       |
| de 20 a 49   | ATENÇÃO       |
| 50 ou mais   | NORMAL        |

### Oxigênio (%)
| Condição     | Classificação |
|--------------|---------------|
| menor que 80 | CRÍTICO       |
| de 80 a 89   | ATENÇÃO       |
| 90 ou mais   | NORMAL        |

### Estabilidade (%)
| Condição     | Classificação |
|--------------|---------------|
| menor que 40 | CRÍTICO       |
| de 40 a 69   | ATENÇÃO       |
| 70 ou mais   | NORMAL        |

---

## ⚠️ Pontuação de risco

| Classificação | Pontos |
|---------------|--------|
| NORMAL        | 0      |
| ATENÇÃO       | 1      |
| CRÍTICO       | 2      |

Pontuação máxima por ciclo: **10 pontos** (5 sensores × 2 pontos).

---

## 🏷️ Classificação do ciclo

| Pontuação total | Classificação        |
|-----------------|----------------------|
| 0 a 2           | MISSÃO ESTÁVEL       |
| 3 a 5           | MISSÃO EM ATENÇÃO    |
| 6 a 10          | MISSÃO CRÍTICA       |

A **classificação final da missão** usa o mesmo critério, aplicado ao **risco médio** dos ciclos.

---

## 📈 Tendência da missão

O sistema compara o risco do **primeiro** ciclo com o do **último**:

- último > primeiro → *tendência de piora*
- último < primeiro → *tendência de melhora*
- último = primeiro → *permaneceu estável*

---

## 🤖 Recomendações automáticas

Geradas a cada ciclo conforme o estado dos sensores:

- **3 ou mais sensores críticos** → ativar modo de segurança e priorizar suporte à vida, energia e comunicação;
- **vários sensores em atenção (sem críticos)** → monitorar sistemas em atenção e preparar plano de contingência;
- **caso geral** → recomendação detalhada por sensor (ex.: *Verificar controle térmico da missão; Monitorar bateria.*);
- **tudo normal** → manter operação normal e continuar monitoramento.

---

## 🔧 Funções implementadas

| Função                            | Descrição                                               |
|-----------------------------------|---------------------------------------------------------|
| `analisar_temperatura()`          | Classifica a temperatura do ciclo                       |
| `analisar_comunicacao()`          | Classifica a qualidade do sinal                         |
| `analisar_bateria()`              | Classifica o nível de bateria                           |
| `analisar_oxigenio()`             | Classifica o nível de oxigênio                          |
| `analisar_estabilidade()`         | Classifica a estabilidade operacional                   |
| `analisar_ciclo()`                | Agrupa a análise dos 5 sensores de um ciclo             |
| `classificar_ciclo()`             | Retorna a classificação com base na pontuação total     |
| `gerar_recomendacao()`            | Gera recomendação automática baseada nos alertas        |
| `analisar_tendencia()`            | Compara primeiro e último ciclo para inferir tendência  |
| `identificar_area_mais_afetada()` | Identifica o sensor com maior acúmulo de risco          |
| `exibir_ciclo()`                  | Exibe no terminal os dados detalhados de um ciclo       |
| `gerar_relatorio_final()`         | Consolida e exibe o relatório final da missão           |
| `interface_inicial()`             | Tela de boas-vindas e leitura do nome da missão         |
| `main()`                          | Função principal que orquestra toda a execução          |

---

## 👨‍🚀 Equipe

**Nome da missão:** Prometheus Deep Scan
**Nome da equipe:** Equipe Ravid

**Integrantes:**
- Rafael Marinucci Peres – RM: 569729
- David dos Reis Cardoso – RM: 568938