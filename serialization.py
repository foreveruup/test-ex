def serialize(numbers): #Преобразование массива чисел в компактную строку.

    if not numbers:
        return ""

    # Сортируем числа для максимизации эффективности
    numbers.sort()

    # Initialize variables
    prev_number = numbers[0]
    count = 1
    serialized_string = ""

    for number in numbers[1:]:
        if number == prev_number:
            count += 1
        else:
            serialized_string += f"{prev_number}:{count},"
            prev_number = number
            count = 1

    # Add the last number
    serialized_string += f"{prev_number}:{count}"

    return serialized_string

def deserialize(serialized_string): # преобразование строки обратно в массив чисел.

    if not serialized_string:
        return []

    numbers = []
    elements = serialized_string.split(',')

    for element in elements:
        number, count = map(int, element.split(':'))
        numbers.extend([number] * count)

    return numbers

