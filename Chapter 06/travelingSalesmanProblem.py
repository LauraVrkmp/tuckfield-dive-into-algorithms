import numpy as np
import math
import matplotlib.collections as mc
import matplotlib.pylab as pl

random_seed = 1729
np.random.seed(random_seed)
N = 40
x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x, y)
cities = list(points)
itinerary = list(range(0, N))


def genLines(cities, itinerary):
    lines = []
    for j in range(0, len(itinerary) - 1):
        lines.append([cities[itinerary[j]], cities[itinerary[j + 1]]])
    return lines


def howFar(lines):
    distance = 0
    for j in range(0, len(lines)):
        distance += math.sqrt(abs(lines[j][1][0] - lines[j][0][0])**2 + 
                              abs(lines[j][1][1] - lines[j][0][1])**2)
    return distance


def plotItinerary(cities, itin, plottitle, thename):
    lc = mc.LineCollection(genLines(cities, itin), linewidths = 2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.scatter(x, y)
    pl.title(plottitle)
    pl.xlabel('X Coordinate')
    pl.ylabel('Y Coordinate')
    pl.savefig(str(thename) + '.png')
    pl.close()


def findNearest(cities, idx, nnItinerary):
    point = cities[idx]
    minDistance = float('inf')
    minIdx = -1
    for j in range(0, len(cities)):
        distance = math.sqrt((point[0] - cities[j][0])**2 + 
                             (point[1] - cities[j][1])**2)
        if distance < minDistance and distance > 0 and j not in nnItinerary:
            minDistance = distance
            minIdx = j
    return minIdx


def donn(cities, N):
    nnItinerary = [0]
    for j in range(0, N - 1):
        next = findNearest(cities, nnItinerary[len(nnItinerary) - 1], nnItinerary)
        nnItinerary.append(next)
    return nnItinerary


def perturb(cities,itinerary):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))
    
    itinerary2 = itinerary.copy()
    
    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]
    
    distance1 = howFar(genLines(cities,itinerary))
    distance2 = howFar(genLines(cities,itinerary2))
    
    itinerarytoreturn = itinerary.copy()
    
    if(distance1 > distance2):
        itinerarytoreturn = itinerary2.copy()
    
    return(itinerarytoreturn.copy())


def perturb_sa1(cities,itinerary,time):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))
    
    itinerary2 = itinerary.copy()
    
    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]
    
    distance1 = howFar(genLines(cities,itinerary))
    distance2 = howFar(genLines(cities,itinerary2))
    
    itinerarytoreturn = itinerary.copy()
    
    randomdraw = np.random.rand()
    temperature = 1/((time/1000) + 1)
    
    if((distance2 > distance1 and (randomdraw) < (temperature)) or (distance1 > distance2)):
        itinerarytoreturn=itinerary2.copy()
    
    return(itinerarytoreturn.copy())


def perturb_sa2(cities, itinerary, time):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.foor(np.random.rand() * (len(itinerary)))

    itinerary2 = itinerary.copy()

    randomdraw2 = np.random.rand()
    small = min(neighborids1, neighborids2)
    big = max(neighborids1, neighborids2)
    if (randomdraw2 >= 0.55):
        itinerary2[small:big] = itinerary2[small:big][:: - 1]
    elif (randomdraw2 < 0.45):
        tempitin = itinerary[small:big]
        del(itinerary2[small:big])
        neighborids3 = math.floor(np.random.rand() * (len(itinerary)))
        for j in range(0, len(tempitin)):
            itinerary2.insert(neighborids3 + j, tempitin[j])
    else:
        itinerary2[neighborids1] = itinerary[neighborids2]
        itinerary2[neighborids2] = itinerary[neighborids1]
    
    distance1 = howFar(genLines(cities, itinerary))
    distance2 = howFar(genLines(cities, itinerary2))

    itineraryToReturn = itinerary.copy()

    randomdraw = np.random.rand()
    temperature = 1 / ((time / 1000) + 1)

    if ((distance2 > distance1 and (randomdraw) < (temperature)) or (distance1 > distance2)):
        itineraryToReturn = itinerary2.copy()

    return itineraryToReturn.copy()


def perturb_sa3(cities, itinerary, time, maxItin):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))
    global minDistance
    global minItinerary
    global minIdx
    itinerary2 = itinerary.copy()
    randomdraw = np.random.rand()

    randomdraw2 = np.random.rand()
    small = min(neighborids1, neighborids2)
    big = max(neighborids1, neighborids2)
    if (randomdraw2 >= 0.55):
        itinerary2[small:big] = itinerary2[small:big][:: - 1]
    elif (randomdraw2 < 0.45):
        tempitin = itinerary[small:big]
        del(itinerary2[small:big])
        neighborids3 = math.floor(np.random.rand() * (len(itinerary)))
        for j in range(0, len(tempitin)):
            itinerary2.insert(neighborids3 + j, tempitin[j])
    else:
        itinerary2[neighborids1] = itinerary[neighborids2]
        itinerary2[neighborids2] = itinerary[neighborids1]
    
    temperature = 1 / (time / (maxItin / 10) + 1)

    distance1 = howFar(genLines(cities, itinerary))
    distance2 = howFar(genLines(cities, itinerary2))

    itineraryToReturn = itinerary.copy()

    scale = 3.5
    if ((distance2 > distance1 and (randomdraw) < (math.exp(scale * 
                (distance1 - distance2)) * temperature)) or 
                (distance1 > distance2)):
        itineraryToReturn = itinerary2.copy()

    reset = True
    resetthresh = 0.04
    if (reset and (time - minIdx) > (maxItin * resetthresh)):
        itineraryToReturn = minItinerary
        minIdx = time

    if (howFar(genLines(cities, itineraryToReturn)) < minDistance):
        minDistance = howFar(genLines(cities, itinerary2))
        minItinerary = itineraryToReturn
        minIdx = time

    if (abs(time - maxItin) <= 1):
        itineraryToReturn = minItinerary.copy()

    return itineraryToReturn.copy()


def siman(itinerary, cities):
    newItinerary = itinerary.copy()
    global minDistance
    global minItinerary
    global minIdx
    minDistance = howFar(genLines(cities, itinerary))
    minItinerary = itinerary
    minIdx = 0

    maxItin = len(itinerary) * 50000
    for t in range(0, maxItin):
        newItinerary = perturb_sa3(cities, newItinerary, t, maxItin)

    return newItinerary.copy()


# np.random.seed(random_seed)
# itinerary = list(range(N))
# nnItin = donn(cities, N)
# nnResult = howFar(genLines(cities, nnItin))
# simanItinerary = siman(itinerary, cities)

# plotItinerary(cities, simanItinerary, 
#               'Traveling Salesman Itinerary - Simulated Annealing', 'figure5')
# simanResult = howFar(genLines(cities, simanItinerary))
# print(nnResult)
# print(simanResult)
# print(simanResult / nnResult)


# itinerary = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
#              25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
# np.random.seed(random_seed)

# itinerary_ps = itinerary.copy()
# for n in range(0,len(itinerary) * 50000):
#     itinerary_ps = perturb(cities,itinerary_ps)

# itinerary = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
#              25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
# np.random.seed(random_seed)

# itinerary_sa = itinerary.copy()
# for n in range(0,len(itinerary) * 50000):
#     itinerary_sa = perturb_sa1(cities,itinerary_sa,n)

# print(howFar(genLines(cities, itinerary))) # random itinerary
# print(howFar(genLines(cities, itinerary_ps))) # perturb search
# print(howFar(genLines(cities, itinerary_sa))) # simulated annealing
# print(howFar(genLines(cities, donn(cities, N)))) # nearest neighbor

# totalDistance = howFar(genlines(cities, itinerary))
# plotItinerary(cities, itinerary, 'TSP - Random Itinerary', 'figure2')
# plotItinerary(cities, donn(cities, N), 'TSP - Nearest Neighbor', 'figure3')
# print(howFar(genlines(cities, donn(cities, N))))