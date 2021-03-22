class Solution:
	def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

		seconds = 0

		for i in range(len(points)-1):
			deltax = abs(points[i][0] - points[i+1][0])
			deltay = abs(points[i][1] - points[i+1][1])
			seconds += max(deltax, deltay)

		return seconds