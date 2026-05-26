# Mission Control AI — EnviroSat

## Integrantes

- Sofia Lima - 567824
- Laura Olivera - 567277

---

## O que o projeto faz

O Mission Control AI é um sistema inteligente de monitoramento espacial desenvolvido na trilha EnviroSat da Global Solution 2026.1.

O projeto simula a operação de um satélite de observação ambiental através da geração de dados de telemetria, incluindo temperatura, energia, comunicação e precisão de geolocalização. A partir desses dados, o sistema detecta automaticamente situações críticas utilizando lógica Python e integra IA generativa via Ollama Cloud para produzir análises contextualizadas em linguagem natural.

Além da análise técnica da missão, a IA também relaciona os problemas detectados aos impactos terrestres, como monitoramento de incêndios, fiscalização ambiental e combate ao desmatamento.

---

## Persona atendida

O sistema foi desenvolvido para operadores de centros de controle ambiental responsáveis pelo monitoramento de satélites de observação terrestre. A IA auxilia esses profissionais na interpretação rápida da telemetria da missão, permitindo identificar riscos operacionais e compreender os impactos que falhas no satélite podem causar em atividades ambientais críticas na Terra.
---

## Tecnologias utilizadas

- Python 3.10+
- Ollama Cloud API
- Modelo gpt-oss:120b
- rich
- pyfiglet
- prompt-toolkit
- python-dotenv

---

## Como executar

1. Clone o repositório

```bash
git clone https://github.com/sofiaoliveira0707-crypto/GS_IA.git
```

2. Crie o ambiente virtual

```bash
python -m venv .venv
```

3. Ative o ambiente virtual

Windows:

```bash
.venv\Scripts\activate
```

4. Instale as dependências

```bash
pip install -r requirements.txt
```

5. Crie um arquivo `.env` com:

```txt
OLLAMA_API_KEY=sua_chave
```

6. Execute o sistema

```bash
python main.py
```

---
# Proposta de Valor e Modelo de Negócio## 
 Qual problema real terrestre esta missão resolve? A missão EnviroSat busca auxiliar no monitoramento ambiental através da análise de dados orbitais relacionados a incêndios florestais, desmatamento e áreas protegidas.O sistema ajuda operadores a identificar rapidamente situações críticas, permitindo respostas mais ágeis em eventos ambientais e reduzindo o tempo de reação diante de anomalias detectadas pelo satélite.
 ---
 ## 2. Quem paga pela solução?
 A solução pode operar em modelo híbrido, envolvendo tanto setor público quanto privado.Órgãos governamentais como INPE, IBAMA e centros estaduais de monitoramento ambiental podem utilizar a plataforma para fiscalização e prevenção de desastres ambientais. Além disso, empresas privadas de análise ambiental, agronegócio e sustentabilidade também podem contratar o serviço para monitoramento de áreas específicas.
 ---
 ## 3. Métrica de impacto
Se o satélite operar de forma saudável por 1 ano, o sistema pode contribuir para o monitoramento contínuo de milhares de hectares de áreas ambientais e de preservação.Com respostas mais rápidas a focos de incêndio e falhas ambientais, estima-se a redução de danos ambientais, emissão de CO₂ e perda de biodiversidade em regiões monitoradas. Além disso, o aumento da confiabilidade operacional melhora a velocidade de tomada de decisão em centros ambientais.
---
## 4. Modelo de negócio
O projeto pode funcionar no modelo SaaS (Software as a Service), oferecendo acesso à plataforma de monitoramento mediante assinatura.Outra possibilidade é o modelo de “dados como serviço”, no qual instituições públicas ou privadas contratam acesso às análises ambientais geradas a partir dos dados orbitais e da IA integrada ao sistema.

## System Prompt

O system prompt utilizado pelo projeto está disponível no arquivo:

`prompts/system_prompt.md`

O prompt foi desenvolvido para orientar a IA a atuar como uma assistente de operações espaciais da trilha EnviroSat, interpretando dados de telemetria, identificando riscos técnicos e relacionando falhas orbitais aos impactos terrestres no monitoramento ambiental.

## Demonstração

![Banner](assets/screenshot_banner.png)

![Análise](assets/screenshot_analise.png)

---

## Cenários testados

1. Operação normal
2. Temperatura crítica
3. Baixa energia
4. Perda de comunicação
5. Buffer de imagens elevado

---

## Limitações conhecidas

- O sistema utiliza dados simulados.
- Não há persistência de histórico da telemetria.
- O projeto não utiliza dados reais de satélites.

---

## Vídeo de demonstração

 Link do video de demonstração funcionando aqui: https://youtu.be/6ELHXwAfLA8