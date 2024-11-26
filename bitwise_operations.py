import sys

def validate_input(input_data):
    try:
        numbers = list(map(int, input_data.split(',')))
        return numbers
    except ValueError:
        print("Error: Please enter a comma-separated list of integers.")
        sys.exit(1)

def bitwise_operations(numbers):
    result_and = numbers[0]
    result_or = numbers[0]
    result_xor = numbers[0]

    for num in numbers[1:]:
        result_and &= num
        result_or |= num
        result_xor ^= num

    return result_and, result_or, result_xor

def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

if __name__ == "__main__":
    input_data = input("Enter integers separated by commas: ")
    threshold = int(input("Enter a threshold: "))

    numbers = validate_input(input_data)
    and_result, or_result, xor_result = bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold)

    print(f"Bitwise AND: {and_result}")
    print(f"Bitwise OR: {or_result}")
    print(f"Bitwise XOR: {xor_result}")
    print(f"Numbers greater than threshold: {filtered_numbers}")
