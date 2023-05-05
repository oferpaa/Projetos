import numpy as np

print('='*100)
name = input('Olá, qual seu nome? ')
print('='*100)

nums = input(f'{name}, insira uma lista de números e os separe por vírgula: ')
nums = [int(num) for num in nums.split(',')]
print('='*100)

# Média
media = np.mean(nums)
# Mediana
mediana = np.median(nums)
# Moda
moda = max(set(nums), key=nums.count)

print('Média: {:.2f}'.format(media))
print('Mediana: {:.0f}'.format(mediana))
print('Moda: ', moda)
print('='*100)
