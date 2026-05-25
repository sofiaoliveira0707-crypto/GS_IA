"""Geração de dados simulados de telemetria do EnviroSat."""

import random


def coletar():
    """Simula a coleta de dados do satélite ambiental."""

    dados = {
        "trilha": "EnviroSat",
        "temperatura_sensor": random.randint(20, 95),
        "energia": random.randint(5, 100),
        "comunicacao": random.choice(["estavel", "instavel", "perdida"]),
        "buffer_imagens": random.randint(0, 100),
        "precisao_geolocalizacao": round(random.uniform(1.0, 15.0), 2)
    }

    return dados