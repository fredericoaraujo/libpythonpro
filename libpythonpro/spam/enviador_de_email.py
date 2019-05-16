class Enviador:

    def enviar(self, remetente, destinatario, assunto, corpo_texto):
        if '@' not in remetente:
            raise EmailInvalido(f'E-mail de remetente inválido [{remetente}]')
        return remetente


class EmailInvalido(Exception):
    pass
