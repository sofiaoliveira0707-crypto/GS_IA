"""Regras de alerta e decisão automática do EnviroSat."""


def avaliar(dados):
    """Avalia os dados de telemetria e retorna alertas."""

    alertas = []
    acoes = []

    if dados["temperatura_sensor"] > 75:
        alertas.append("Temperatura crítica no sensor térmico.")
        acoes.append("Reduzir operação do sensor e ativar modo de resfriamento.")

    if dados["energia"] < 25:
        alertas.append("Energia abaixo do nível seguro.")
        acoes.append("Ativar modo de economia de energia.")

    if dados["comunicacao"] == "perdida":
        alertas.append("Perda de comunicação com a estação terrestre.")
        acoes.append("Tentar reconexão automática e priorizar telemetria essencial.")

    if dados["buffer_imagens"] > 80:
        alertas.append("Buffer de imagens quase cheio.")
        acoes.append("Priorizar downlink das imagens ambientais mais recentes.")

    if dados["precisao_geolocalizacao"] > 10:
        alertas.append("Baixa precisão de geolocalização.")
        acoes.append("Recalibrar sistema de posicionamento orbital.")

    if not alertas:
        alertas.append("Nenhum alerta crítico detectado.")
        acoes.append("Manter operação normal da missão.")

    return {
        "alertas": alertas,
        "acoes": acoes
    }