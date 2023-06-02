from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    'Deve retornar um erro se a mensagem não for uma string'
    with pytest.raises(TypeError):
        encrypt_message(123, 1)
    'Deve retornar um erro se a chave não for um inteiro'
    with pytest.raises(TypeError):
        encrypt_message("abc", "1")
    'Deve retornar a mensagem invertida se a chave for válida'
    assert encrypt_message("abc", 0) == "cba"
    assert encrypt_message("abc", 4) == "cba"
    'Verifica funcionamento com chave ímpar'
    assert encrypt_message("zbcefgp", 3) == "cbz_pgfe"
    'Verifica funcionamento com chave par'
    assert encrypt_message("zbcdefgp", 4) == "pgfe_dcbz"
