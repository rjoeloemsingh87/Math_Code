#Standard Deviation
import math

def standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    deviations = [(x - mean) ** 2 for x in numbers]
    variance = sum(deviations) / (n - 1)
    std_dev = math.sqrt(variance)
    return std_dev
