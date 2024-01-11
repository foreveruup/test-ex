import unittest
import random
from serialization import serialize, deserialize

class TestSerializationMethods(unittest.TestCase):

    def test_random_data(self):
        data = [random.randint(1, 300) for _ in range(100)]
        serialized = serialize(data)
        deserialized = deserialize(serialized)
        self.assertEqual(sorted(data), sorted(deserialized))

    def test_single_digit_data(self):
        data = [random.randint(1, 9) for _ in range(100)]
        serialized = serialize(data)
        deserialized = deserialize(serialized)
        self.assertEqual(sorted(data), sorted(deserialized))

    def test_double_digit_data(self):
        data = [random.randint(10, 99) for _ in range(100)]
        serialized = serialize(data)
        deserialized = deserialize(serialized)
        self.assertEqual(sorted(data), sorted(deserialized))

    def test_triple_digit_data(self):
        data = [random.randint(100, 300) for _ in range(100)]
        serialized = serialize(data)
        deserialized = deserialize(serialized)
        self.assertEqual(sorted(data), sorted(deserialized))

    def test_repeated_data(self):
        data = [42] * 100
        serialized = serialize(data)
        deserialized = deserialize(serialized)
        self.assertEqual(data, deserialized)

    def test_empty_data(self):
        data = []
        serialized = serialize(data)
        deserialized = deserialize(serialized)
        self.assertEqual(data, deserialized)

if __name__ == '__main__':
    unittest.main()
