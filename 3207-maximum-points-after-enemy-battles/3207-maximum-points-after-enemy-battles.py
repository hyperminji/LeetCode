class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        ene = 0
        len_ene = len(enemyEnergies)
        min_ene = enemyEnergies[0]
        for i in range(0, len_ene):
            ene = ene + enemyEnergies[i]
            if min_ene > enemyEnergies[i]:
                min_ene = enemyEnergies[i]
        if min_ene > currentEnergy:
            return 0
        ene = ene + currentEnergy - min_ene
        result =  ene // min_ene
        return result

        