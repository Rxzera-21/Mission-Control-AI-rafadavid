# 🚀 Mission Control AI
### GS2026.1 — Pensamento Computacional e Automação com Python

Sistema inteligente de monitoramento de missão espacial desenvolvido em Python puro.

---

## 📋 Descrição

O **Mission Control AI** simula o acompanhamento de uma missão espacial experimental chamada **Prometheus Deep Scan**. O sistema analisa 6 ciclos de monitoramento, cada um com 5 sensores, classifica o nível de risco de cada ciclo, identifica tendências e gera um relatório final completo no terminal.

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

---

## 📊 Estrutura dos dados

A matriz principal `dados_missao` contém 6 linhas (ciclos) e 5 colunas (sensores):

| Posição | Sensor       | Unidade |
|---------|--------------|---------|
| 0       | Temperatura  | °C      |
| 1       | Comunicação  | %       |
| 2       | Bateria      | %       |
| 3       | Oxigênio     | %       |
| 4       | Estabilidade | %       |

---

## 🔔 Regras de alerta

### Temperatura (°C)
| Condição             | Classificação |
|----------------------|---------------|
| < 18                 | ATENÇÃO       |
| 18 a 30              | NORMAL        |
| > 30 até 35          | ATENÇÃO       |
| > 35                 | CRÍTICO       |

### Comunicação (%)
| Condição   | Classificação |
|------------|---------------|
| < 30       | CRÍTICO       |
| 30 a 59    | ATENÇÃO       |
| ≥ 60       | NORMAL        |

### Bateria (%)
| Condição   | Classificação |
|------------|---------------|
| < 20       | CRÍTICO       |
| 20 a 49    | ATENÇÃO       |
| ≥ 50       | NORMAL        |

### Oxigênio (%)
| Condição   | Classificação |
|------------|---------------|
| < 80       | CRÍTICO       |
| 80 a 89    | ATENÇÃO       |
| ≥ 90       | NORMAL        |

### Estabilidade (%)
| Condição   | Classificação |
|------------|---------------|
| < 40       | CRÍTICO       |
| 40 a 69    | ATENÇÃO       |
| ≥ 70       | NORMAL        |

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

---

## 🔧 Funções implementadas

| Função                        | Descrição                                               |
|-------------------------------|---------------------------------------------------------|
| `analisar_temperatura()`      | Classifica a temperatura do ciclo                       |
| `analisar_comunicacao()`      | Classifica a qualidade do sinal                         |
| `analisar_bateria()`          | Classifica o nível de bateria                           |
| `analisar_oxigenio()`         | Classifica o nível de oxigênio                          |
| `analisar_estabilidade()`     | Classifica a estabilidade operacional                   |
| `analisar_ciclo()`            | Agrupa a análise dos 5 sensores de um ciclo             |
| `classificar_ciclo()`         | Retorna a classificação com base na pontuação total     |
| `gerar_recomendacao()`        | Gera recomendação automática baseada nos alertas        |
| `analisar_tendencia()`        | Compara primeiro e último ciclo para inferir tendência  |
| `identificar_area_mais_afetada()` | Identifica o sensor com maior acúmulo de risco      |
| `exibir_ciclo()`              | Exibe no terminal os dados detalhados de um ciclo       |
| `gerar_relatorio_final()`     | Consolida e exibe o relatório final da missão           |
| `main()`                      | Função principal que orquestra toda a execução          |

---

## 👨‍🚀 Equipe

**Missão:** Horizon Escape  
**Equipe:** Equipe Ravid
