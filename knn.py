from general import loadCSV, dictListToInt
import math

dataset = dictListToInt(loadCSV('trainset.csv'))
data_dicari = dictListToInt(loadCSV('testset.csv'))

# Split dataset
test_data = []
training_data = []
for i in range(0, len(dataset)):
    if i % 5 == 0:
        test_data.append(dataset[i])
    else:
        training_data.append(dataset[i])
print(len(training_data), len(test_data))
# print(training_data)
# print(test_data)
def euclideanDistance(instance1, instance2, length):
    distance = 0
    
    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    
    return math.sqrt(distance)

def calculateEuclidianDistances(training_data, test_data):
    distances = []
    
    for training_instance in training_data:
        distance = euclideanDistance([test_data["x1"], test_data["x2"], test_data["x3"]], [training_instance["x1"], training_instance["x2"], training_instance["x3"], ], 3)
        distances.append((training_instance, distance))
    
    return distances

def sortDistances(distances):
    return sorted(distances, key=lambda x: x[1])

def getNNeighbours(distances, n):
    return distances[:n]

def getResponse(neighbours):
    sums = {0:0,1:0}
    for i in neighbours:
        sums[int(i[0]["y"])] += 1
    return max(sums, key=sums.get)

def knn(training_data, test_data, k):
    distances = calculateEuclidianDistances(training_data, test_data)
    sorted_distances = sortDistances(distances)
    neighbours = getNNeighbours(sorted_distances, k)
    return getResponse(neighbours)

def accuracyOfK(k):
    correct = 0
    for evalInstance in test_data:
        if knn(training_data, evalInstance, k) == int(evalInstance["y"]):
            correct += 1
    return correct/len(test_data)

def getBestK():
    bestK = 0
    bestAccuracy = 0
    for k in range(1, 100):
        accuracy = accuracyOfK(k)
        if accuracy > bestAccuracy:
            bestK = k
            bestAccuracy = accuracy
    return bestK, bestAccuracy

def main():
    best = getBestK()
    print(best)
    k = best[0]
    correct = 0
    for evalInstance in test_data:
        print(evalInstance, knn(training_data, evalInstance, k))
        if knn(training_data, evalInstance, k) == int(evalInstance["y"]):
            correct += 1
    print("Akurasi: " + str(correct/len(test_data)))

    for evalInstance in data_dicari:
        print(evalInstance, knn(training_data, evalInstance, k))
if __name__ == "__main__":
    main()
    