import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'renzo@python.pro.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossum criada'
    )

    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'renzo']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'luciano@python.pro.br',
            'Curso Python Pro',
            'Primeira turma Guido Von Rossum criada'
        )
