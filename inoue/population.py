import sys

def population_ranking(rank):
    # 世界人口ランキング（2021年時点）
    countries = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

    # 指定された順位の国名を出力
    if 0 < rank <= 10:
        return countries[rank - 1]
    else:
        return "Error: Rank must be between 1 and 10."

rank = int(sys.argv[1])
print(population_ranking(rank))
