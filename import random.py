import random
def get_numbers_ticket(min, max, quantity):
    
    if min < 1 or max > 1000 or quantity < 0:
        return []
    numbers_ticket = set()
    while len(numbers_ticket) < quantity:
        numbers_ticket.add(random.randint(min, max))
    
    sorted_numbers = sorted(list(numbers_ticket))
    return sorted_numbers
min = 1
max = 1000
quantity = 8
result = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", result)

