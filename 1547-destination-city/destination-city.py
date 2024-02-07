from collections import deque

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting_cities = set()
        for path in paths:
            starting_cities.add(path[0])
        for path in paths:
            if not path[1] in starting_cities:
                return path[1]
        return ""

        