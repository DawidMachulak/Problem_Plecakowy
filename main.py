import random

KNAPSACK_CAPACITY = 1000
ALL_ITEMS_COUNT = 100
MAX_UNIMPROVED_ITERATIONS = 100
MIN_WEIGHT = 5
MAX_WEIGHT = 50


class Knapsack:
    def __init__(self):
        self.itemsWeights = [random.randint(MIN_WEIGHT, MAX_WEIGHT + 1) for i in range(ALL_ITEMS_COUNT)]
        self.genome = [random.random() % 2 == 0 for i in range(ALL_ITEMS_COUNT)]
        self.genomeScore = self.score(self.genome)

    def is_better(self, mutatedGenomeScore):
        if self.genomeScore > KNAPSACK_CAPACITY:
            return mutatedGenomeScore < self.genomeScore
        if mutatedGenomeScore <= KNAPSACK_CAPACITY:
            return mutatedGenomeScore > self.genomeScore
        return False

    def score(self, genomeToScore):
        return sum([self.itemsWeights[i] for i in range(ALL_ITEMS_COUNT) if genomeToScore[i]])

    def mutate(self):
        newGenome = list(self.genome)
        index = random.randint(0, ALL_ITEMS_COUNT - 1)
        newGenome[index] = not newGenome[index]
        return newGenome

    def pack(self):
        print("Weights:")
        print(self.itemsWeights)
        print("First genome:")
        print(['+' if i else '-' for i in self.genome])
        # print("Score:", self.genomeScore)
        print("--------------------------------------------------------------------------------")

        mutationsCount = 0
        unimprovedMutationsCount = 0

        while unimprovedMutationsCount < MAX_UNIMPROVED_ITERATIONS:
            mutationsCount += 1
            mutatedGenome = self.mutate()
            mutatedGenomeScore = self.score(mutatedGenome)

            if self.is_better(mutatedGenomeScore):
                self.genome = mutatedGenome
                self.genomeScore = mutatedGenomeScore
                unimprovedMutationsCount = 0
            else:
                unimprovedMutationsCount += 1

        print("Best genome:")
        print(['+' if i else '-' for i in self.genome])
        print("Score:", self.genomeScore)
        print("--------------------------------------------------------------------------------")
        print("Total Iterations:", mutationsCount)
        print("Best after:", mutationsCount - MAX_UNIMPROVED_ITERATIONS)
        print("--------------------------------------------------------------------------------")


knapsack = Knapsack()
knapsack.pack()
