import random

def randomize_numbers(times, count, start, end):
    all_random_numbers = []
    for _ in range(times):
        random_numbers = random.sample(range(start, end + 1), count)
        all_random_numbers.append(random_numbers)
    return all_random_numbers

# Configurações
times = 5  # Número de vezes que queremos randomizar
count = 7  # Número de números aleatórios por vez
start = 1  # Início do intervalo
end = 9    # Fim do intervalo

# Gerar os números aleatórios
randomized_lists = randomize_numbers(times, count, start, end)

# Separar os últimos dois números dos outros cinco
print(f"Números da MegaSenha")
for i, numbers in enumerate(randomized_lists):
    first_five = numbers[:-2]
    last_two = numbers[-2:]
    print(f"Números: {first_five} |Estrelas: {last_two}")
