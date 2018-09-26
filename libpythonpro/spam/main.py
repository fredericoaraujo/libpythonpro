class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.enviador = enviador
        self.sessao = sessao

    def enviar_emails(self, remetente, assunto, corpo_texto):
        pass
