import unittest
import numpy as np


def mnk(x, y):
    if not isinstance(x, np.ndarray):
        raise TypeError(f"mnk does not support type {type(x)} in arguments")
    if not isinstance(y, np.ndarray):
        raise TypeError(f"mnk does not support type {type(y)} in arguments")

    if len(x) == 0 or len(y) == 0:
        return "Вы не ввели данные?"

    if len(x) != len(y):
        return "Введите одинаковое число измерений x и y."

    xy = x * y
    x2 = x * x

    if np.allclose(np.mean(x2), np.mean(x) ** 2):
        return "Ваши данные слишком идеальны для МНК"

    b = (np.mean(xy) - np.mean(x) * np.mean(y)) / (np.mean(x2) - np.mean(x) ** 2)
    a = np.mean(y) - b * np.mean(x)

    return f"y = x * {b:.4f} + {a:.4f}"


class OrdinaryTest(unittest.TestCase):
    def test_mnk(self):
        x = np.array([1, 2, 3, 4, 5, 6])
        y = np.array([1, 2, 3, 4, 5, 6])
        res = "y = x * 1.0000 + 0.0000"
        self.assertEqual(mnk(x, y), res)


class PerfectData(unittest.TestCase):
    def test_mnk(self):
        x = np.array([1, 1, 1, 1, 1])
        y = np.array([1, 1, 1, 1, 1])
        msg = "Ваши данные слишком идеальны для МНК"
        self.assertEqual(mnk(x, y), msg)


class EmptyArrays(unittest.TestCase):
    def test_mnk(self):
        x = np.array([])
        y = np.array([])
        msg = "Вы не ввели данные?"
        self.assertEqual(mnk(x, y), msg)


class WrongDataType(unittest.TestCase):
    def test_mnk(self):
        with self.assertRaises(TypeError):
            mnk(1, 2)


class DifferentLengthTest(unittest.TestCase):
    def test_mnk(self):
        x = np.array([1, 2, 3])
        y = np.array([1, 2])
        msg = "Введите одинаковое число измерений x и y."
        self.assertEqual(mnk(x, y), msg)


class RealDataTest(unittest.TestCase):
    def test_mnk(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 5, 4, 5])
        b = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (
            np.mean(x * x) - np.mean(x) ** 2
        )
        a = np.mean(y) - b * np.mean(x)
        expected = f"y = x * {b:.4f} + {a:.4f}"
        self.assertEqual(mnk(x, y), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

    try:
        x = np.array([float(i) for i in input("Введите x через пробел: ").split()])
        y = np.array([float(i) for i in input("Введите y через пробел: ").split()])
        print(mnk(x, y))
    except ValueError:
        print("Ошибка ввода: введите числа через пробел")
