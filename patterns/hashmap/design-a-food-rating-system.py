from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c2rf = defaultdict(SortedList)
        self.f2cr = {} # self.f2cr[food][0] c self.f2cr[food][1] r
        for f, c, r in zip(foods, cuisines, ratings):
            self.f2cr[f] = [c, r]
            self.c2rf[c].add((-r, f)) # point: cannot sort food, so sort something with number

    def changeRating(self, food: str, newRating: int) -> None:
        [cuisine, oldRating] = self.f2cr[food]
        
        self.c2rf[cuisine].discard((-oldRating, food))
        self.c2rf[cuisine].add((-newRating, food))
        self.f2cr[food][1] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.c2rf[cuisine][0][1]
