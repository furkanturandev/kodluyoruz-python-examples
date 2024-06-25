import math

points = [(2, 3), (5, 7), (1, 1), (8, 2), (4, 6)]
distances = []
min_distance = float("inf") # this value means positive infinity

# euclidean formula
def euclideanDistance(point1, point2):
    x1, y1 = point1 # example >> x1, x2 = (2,3) => x1 = 2 & x2 = 3
    x2, y2 = point2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return int(distance)

# loop that calculates the distances of items in a list of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# find minimum distance in distances list (optional)
for distance in distances:
    if distance < min_distance:
        min_distance = distance
        
print(f"Uzaklıklar: {distances}")

print(f"Listedeki en küçük uzaklık: {min_distance}")
        


        



