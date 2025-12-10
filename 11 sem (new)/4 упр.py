import unittest


class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        if not isinstance(key, int):
            msg = f"Caesar does not support type {type(key)} in arguments"
            raise TypeError(msg)
        self._encode = dict()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        if not isinstance(text, str):
            msg = f"encode does not support type {type(text)} in arguments"
            raise TypeError(msg)
        return "".join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        if not isinstance(line, str):
            msg = f"decode does not support type {type(line)} in arguments"
            raise TypeError(msg)
        return "".join([self._decode.get(char, char) for char in line])


class OrdinaryTest(unittest.TestCase):
    def test_decode(self):
        cipher = Caesar(30)
        msg = "етзуиж"
        dec = "вперёд"
        self.assertEqual(cipher.decode(msg), dec)


class UpperLetters(unittest.TestCase):
    def test_decode(self):
        cipher = Caesar(30)
        msg = "ЕКУЮЕ"
        dec = "ВЗРЫВ"
        self.assertEqual(cipher.decode(msg), dec)


class KeyMoreAlphabetSize(unittest.TestCase):
    def test_decode(self):
        cipher = Caesar(66)
        msg = "Снег"
        self.assertEqual(cipher.decode(msg), msg)


class WrongDataTypeConstructor(unittest.TestCase):
    def test_wrong_key_type(self):
        with self.assertRaises(TypeError):
            Caesar("30")


class WrongDataTypeDecode(unittest.TestCase):
    def test_decode(self):
        cipher = Caesar(0)
        with self.assertRaises(TypeError):
            cipher.decode(3)


class EncodeDecodeCycle(unittest.TestCase):
    def test_cycle(self):
        cipher = Caesar(5)
        original = "привет мир"
        encoded = cipher.encode(original)
        decoded = cipher.decode(encoded)
        self.assertEqual(decoded, original)


class EmptyStringTest(unittest.TestCase):
    def test_empty(self):
        cipher = Caesar(10)
        self.assertEqual(cipher.decode(""), "")
        self.assertEqual(cipher.encode(""), "")


if __name__ == "__main__":
    unittest.main(exit=False)

    print("\n" + "=" * 50)
    print("Тесты завершены. Теперь введите данные для дешифровки.")
    print("=" * 50)

    while True:
        key = input("Введите ключ: ")
        if key.isdigit():
            key = int(key)
            break
        else:
            print("Ключ должен быть целым неотрицательным числом.")

    cipher = Caesar(key)

    print("Введите строки для дешифровки (пустая строка для завершения):")
    while True:
        line = input()
        if not line:
            break
        print(cipher.decode(line))
