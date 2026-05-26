"""Motor de análise da Mission Control AI."""

import os
from pathlib import Path
from ollama import Client
from dotenv import load_dotenv

from src.telemetria import coletar
from src.alertas import avaliar

load_dotenv()

TRILHA = "EnviroSat"

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")
    }
)


def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud."""

    messages = []

    if system:
        messages.append({
            "role": "system",
            "content": system
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        resposta = client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={
                "num_predict": max_tokens,
                "temperature": temperature
            },
            stream=False
        )

        return resposta["message"]["content"].strip()

    except Exception as erro:
        return f"⚠️ Erro ao consultar IA: {erro}"


def load_system_prompt():
    """Lê o system prompt do projeto."""

    path = Path("prompts/system_prompt.md")

    if path.exists():
        return path.read_text(encoding="utf-8")

    return "Você é um assistente de missão espacial."


class MissionEngine:
    """Motor de análise do EnviroSat."""

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
        self.ultima_telemetria = None
        self.ultimos_alertas = None

    def is_ready(self):
        return True

    def status_snapshot(self):
        """Mostra um resumo da telemetria atual."""

        dados = coletar()
        resultado_alertas = avaliar(dados)

        self.ultima_telemetria = dados
        self.ultimos_alertas = resultado_alertas

        texto = f"""
STATUS DA MISSÃO — {self.trilha}

Temperatura do sensor: {dados["temperatura_sensor"]} °C
Energia disponível: {dados["energia"]}%
Comunicação: {dados["comunicacao"]}
Buffer de imagens: {dados["buffer_imagens"]}%
Precisão de geolocalização: {dados["precisao_geolocalizacao"]} m

ALERTAS:
- """ + "\n- ".join(resultado_alertas["alertas"]) + """

AÇÕES AUTOMÁTICAS:
- """ + "\n- ".join(resultado_alertas["acoes"])

        return texto

    def analyze(self, pergunta_usuario):
        """Analisa a missão usando telemetria, alertas e IA."""

        dados = coletar()
        resultado_alertas = avaliar(dados)

        if self.ultima_telemetria:
            if self.ultima_telemetria:
                dados = self.ultima_telemetria
            else:
                dados = coletar()

            resultado_alertas = avaliar(dados)
        prompt = f"""
            Usuário perguntou:
            {pergunta_usuario}

Dados atuais da telemetria do satélite EnviroSat:
- Temperatura do sensor térmico: {dados["temperatura_sensor"]} °C
- Energia disponível: {dados["energia"]}%
- Comunicação com estação terrestre: {dados["comunicacao"]}
- Buffer de imagens não transmitidas: {dados["buffer_imagens"]}%
- Precisão de geolocalização: {dados["precisao_geolocalizacao"]} metros

Alertas detectados pelo código Python:
{resultado_alertas["alertas"]}

Ações automáticas sugeridas pelo sistema:
{resultado_alertas["acoes"]}

Responda em português brasileiro.
Explique:
1. Estado atual da missão.
2. Riscos técnicos.
3. Ações recomendadas.
4. Impacto terrestre para monitoramento ambiental, incêndios e desmatamento.
"""

        return llm(
            prompt,
            system=self.system_prompt,
            max_tokens=900,
            temperature=0.3
        )