n = int(input())

for i in range(n):
    dragons = input().split(' ')
    type, name, damage, health, armor = dragons[::]
    damage = int(damage)
    health = int(health)
    armor = int(armor)
    print(dragons)
