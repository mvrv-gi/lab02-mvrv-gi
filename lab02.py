def seconds_to_hms(seconds):
    """Convert seconds to hours, minutes, and seconds."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours}: {minutes} :{remaining_seconds}"

print(seconds_to_hms(3661)) 
print(seconds_to_hms(59))
print(seconds_to_hms(7325))

def admission_price(age):
    """Determine the admission price based on age."""
    if age < 5:
        return 0 
    elif age >=5 and age <=12:
        return 8.00 
    elif age >= 13 and age <= 64:
        return 15.00 
    else:
        return 10.00 

print(admission_price(3)) 
print(admission_price(10))
print(admission_price(30))
print(admission_price(70))

def sum_multiples_of_3_and_5(limit):
    """Calculate the sum of all multiples of 3 or 5 below a given limit."""
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(sum_multiples_of_3_and_5(10))
print(sum_multiples_of_3_and_5(20))
print(sum_multiples_of_3_and_5(1)) 

def total_positives(numbers):
    """Calculate the total of all positive numbers in a list."""
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

print(total_positives([1, -2, 3, -4, 5]))
print(total_positives([-1, -2]))
print(total_positives([10,20]))
                    













































































