# config.py

class Config:
    # Configura o URI de conexão do banco de dados para o motor padrão
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/postgres'

    # Define opções de motor para o motor padrão
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,  # Exemplo de opção de motor
        # 'pool_size': 20,  # Número máximo de conexões no pool
        # 'pool_recycle': 3600,  # Reciclar conexões a cada 1 hora (em segundos)
        # 'pool_timeout': 30,  # Tempo máximo de espera para obter uma conexão (em segundos)
        'echo': True,  # Define se deve mostrar as instruções SQL geradas
        # 'echo_pool': False,  # Define se deve mostrar mensagens de log para o pool de conexões
        # 'pool_pre_ping': True  # Verificar conexão antes de emitir consultas
    }

    # Configura binds adicionais, se necessário
    SQLALCHEMY_BINDS = {
        # Exemplo de bind adicional
        # 'outro_db': 'postgresql://usuario:senha@localhost/outro_bd',
        # Adicione mais binds conforme necessário
    }

    # Habilita/desabilita recursos de debug
    SQLALCHEMY_ECHO = False  # Defina como True para mostrar declarações SQL

    SQLALCHEMY_RECORD_QUERIES = True  # Habilita o registro de consultas durante as requisições

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desabilita o rastreamento de modificações para melhor desempenho

config = Config()