from main import Jar


def test_str():
    jar1 = Jar(20)
    assert str(jar1) == 'The jar is empty'
    jar1.deposit(4)
    assert str(jar1) == '🍪🍪🍪🍪'
    jar1.withdraw(2)
    assert str(jar1) == '🍪🍪'


