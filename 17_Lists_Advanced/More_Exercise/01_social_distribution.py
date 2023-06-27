"""60/100"""

from sys import maxsize


def distribute_wealth(population: list, minimum_wealth: int) -> list:
    DISTRIBUTABLE = True
    for index, distribute in enumerate(population):
        if distribute < minimum_wealth:
            wealthiest, index_wealthiest = find_wealthiest(population)
            while distribute < minimum_wealth and DISTRIBUTABLE:
                distribute += 1
                wealthiest -= 1
                population[index] = distribute
                population[index_wealthiest] = wealthiest
                if wealthiest == minimum_wealth:
                    wealthiest, index_wealthiest = find_wealthiest(population)
                    if wealthiest == minimum_wealth and distribute < minimum_wealth:
                        DISTRIBUTABLE = False
    return DISTRIBUTABLE, population


def find_wealthiest(population: list):
    wealthiest = -maxsize
    index_wealthiest = 0
    for index, wealth in enumerate(population):
        if wealth > wealthiest:
            wealthiest = wealth
            index_wealthiest = index
    return wealthiest, index_wealthiest


entry_population, entry_wealth = [int(x) for x in input().split(', ')], int(input())
DSTRBTBL, pop_list = distribute_wealth(entry_population, entry_wealth)
print(pop_list) if DSTRBTBL else print("No equal distribution possible")

"""100/100"""
# population = list(map(int, input().split(", ")))
# minimum_wealth = int(input())
# countries_count = len(population)
# if sum(population) < countries_count * minimum_wealth:
#     print("No equal distribution possible")
# else:
#     while min(population) < minimum_wealth:
#         for index, country in enumerate(population):
#             if country < minimum_wealth:
#                 difference = minimum_wealth - country
#                 population[index] += difference
#                 max_population_index = population.index(max(population))
#                 population[max_population_index] -= difference
#     print(population)
