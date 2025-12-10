import unittest


def mn(N):
    if not isinstance(N, int) or N <= 0:
        return "Введите натуральное число!"
    if N == 1:
        return "Это число нельзя разложить на простые множители."

    result = []
    while N != 1:
        c = 2
        for _ in range(N):
            if N % c == 0:
                N = N // c
                result.append(c)
                break
            else:
                c += 1
    return result


class OrdinaryTest(unittest.TestCase):
    def test_mn(self):
        self.assertEqual(mn(10), [2, 5])


class FloatTest(unittest.TestCase):
    def test_mn(self):
        msg = "Введите натуральное число!"
        self.assertEqual(mn(2.1), msg)


class ZeroTest(unittest.TestCase):
    def test_mn(self):
        msg = "Введите натуральное число!"
        self.assertEqual(mn(0), msg)


class FloatLessOneTest(unittest.TestCase):
    def test_mn(self):
        msg = "Введите натуральное число!"
        self.assertEqual(mn(0.5), msg)


class OneTest(unittest.TestCase):
    def test_mn(self):
        msg = "Это число нельзя разложить на простые множители."
        self.assertEqual(mn(1), msg)


class SimpleTest(unittest.TestCase):
    def test_mn(self):
        self.assertEqual(mn(29), [29])


class IncorrectDataTest(unittest.TestCase):
    def test_mn(self):
        with self.assertRaises(TypeError):
            mn(2, 1)


if __name__ == "__main__":
    # Запускаем тесты
    unittest.main(exit=False)

    # Затем ввод данных
    x = input().strip()

    if len(x.split()) != 1:
        print("Введите одно число!")
        exit()

    if not x.isdigit():
        print("Введите натуральное число.")
        exit()

    num = int(x)
    if num <= 0:
        print("Введите натуральное число.")
        exit()

    simples = mn(num)
    if isinstance(simples, list):
        print(*simples)
    else:
        print(simples)
