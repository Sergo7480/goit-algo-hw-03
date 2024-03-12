import random
def get_numbers_ticket(min, max, quantity):
   
    if quantity < 1 or quantity > max - min + 1:
        return []
    numbers_ticket = set()
    while len(numbers_ticket) < quantity:
        numbers_ticket.add(random.randint(min, max))   
    sorted_numbers = sorted(list(numbers_ticket))
    return sorted_numbers
    
min = 10
max = 15
quantity = 6
result = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", result)

