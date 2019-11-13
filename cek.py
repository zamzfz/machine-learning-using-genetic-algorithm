import math
import random
import csv
import itertools
from itertools import permutations   
from itertools import combinations 
# from tqdm import tqdm
import collections

def readTrainingData():
    results = []
    with open("datatraining.txt") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)
    results.remove(results[0])
    return results

def setRangeKromosom():
	tmp = []
	arrKromosom = []
	for i in range(1,75):
		if i % 15 == 0:
			tmp.append(i)
	return tmp

def createChromosome(arr):
	ruleRange = random.choice(arr)
	arrKromosom = []
	for i in range(1,ruleRange+1):
		arrKromosom.append(random.randint(0,1))	
	return arrKromosom
	
def createPopulation(N):
	population = []
	for i in range(1,N+1):
		population.append(createChromosome(setRangeKromosom()))
	return population

def splitRule(arrKromosom):
    for i in range(0, len(arrKromosom),15):
        yield arrKromosom[i:i+15] 

def decodeChromosome(chromosome):
	tmp = []
	suhu = chromosome[0:3]
	waktu = chromosome[3:7]
	langit = chromosome[7:11]
	lembap = chromosome[11:14]
	status = chromosome[14]
	cekSL = (list(itertools.product([1, 0], repeat=3)))
	cekWL = (list(itertools.product([1, 0], repeat=4)))
	# print(chromosome)
	if ((suhu == [1,1,1] and waktu == [1,1,1,1] and langit == [1,1,1,1] and lembap == [1,1,1]) or ((suhu == [0,0,0] or waktu == [0,0,0,0] or langit ==[0,0,0,0] or lembap == [0,0,0]))):
		tmp.append("S")
		tmp.append("S")
		tmp.append("S")
		tmp.append("S")
		tmp.append("S")
	else:
		if suhu == list(cekSL[0]):
			tmp.append("Normal,Tinggi,Rendah")
		elif suhu == list(cekSL[1]):
			tmp.append("Normal,Tinggi")
		elif suhu == list(cekSL[2]):
			tmp.append("Tinggi,Rendah")
		elif suhu == list(cekSL[3]):
			tmp.append("Tinggi")
		elif suhu == list(cekSL[4]):
			tmp.append("Normal,Rendah")
		elif suhu == list(cekSL[5]):
			tmp.append("Normal")
		elif suhu == list(cekSL[6]):
			tmp.append("Rendah")
		elif suhu == list(cekSL[7]):
			tmp.append("Rendah")

		if waktu == list(cekWL[0]):
			tmp.append("Pagi,Siang,Sore,Malam")
		elif waktu == list(cekWL[1]):
			tmp.append("Pagi,Siang,Sore")
		elif waktu == list(cekWL[2]):
			tmp.append("Pagi,Siang,Malam")
		elif waktu == list(cekWL[3]):
			tmp.append("Pagi,Siang")
		elif waktu == list(cekWL[4]):
			tmp.append("Pagi,Sore,Malam")
		elif waktu == list(cekWL[5]):
			tmp.append("Pagi,Sore")
		elif waktu == list(cekWL[6]):
			tmp.append("Pagi,Malam")	
		elif waktu == list(cekWL[7]):
			tmp.append("Pagi")
		elif waktu == list(cekWL[8]):
			tmp.append("Siang,Sore,Malam")
		elif waktu == list(cekWL[9]):
			tmp.append("Siang,Sore")
		elif waktu == list(cekWL[10]):
			tmp.append("Siang,Malam")
		elif waktu == list(cekWL[11]):
			tmp.append("Siang")
		elif waktu == list(cekWL[12]):
			tmp.append("Sore,Malam")
		elif waktu == list(cekWL[13]):
			tmp.append("Sore")
		elif waktu == list(cekWL[14]):
			tmp.append("Malam")
		elif waktu == list(cekWL[15]):
			tmp.append("Pagi")		

		if langit == list(cekWL[0]):
			tmp.append("Berawan,Cerah,Hujan,Rintik")
		elif langit == list(cekWL[1]):
			tmp.append("Berawan,Cerah,Hujan")
		elif langit == list(cekWL[2]):
			tmp.append("Berawan,Cerah,Rintik")
		elif langit == list(cekWL[3]):
			tmp.append("Berawan,Cerah")
		elif langit == list(cekWL[4]):
			tmp.append("Berawan,Hujan,Rintik")
		elif langit == list(cekWL[5]):
			tmp.append("Berawan,Hujan")
		elif langit == list(cekWL[6]):
			tmp.append("Berawan,Rintik")	
		elif langit == list(cekWL[7]):
			tmp.append("Berawan")
		elif langit == list(cekWL[8]):
			tmp.append("Cerah,Hujan,Rintik")
		elif langit == list(cekWL[9]):
			tmp.append("Cerah,Hujan")
		elif langit == list(cekWL[10]):
			tmp.append("Cerah,Rintik")
		elif langit == list(cekWL[11]):
			tmp.append("Cerah")
		elif langit == list(cekWL[12]):
			tmp.append("Hujan,Rintik")
		elif langit == list(cekWL[13]):
			tmp.append("Hujan")
		elif langit == list(cekWL[14]):
			tmp.append("Rintik")
		elif langit == list(cekWL[15]):
			tmp.append("Berawan")

		if lembap == list(cekSL[0]):
			tmp.append("Normal,Tinggi,Rendah")
		elif lembap == list(cekSL[1]):
			tmp.append("Normal,Tinggi")
		elif lembap == list(cekSL[2]):
			tmp.append("Tinggi,Rendah")
		elif lembap == list(cekSL[3]):
			tmp.append("Tinggi")
		elif lembap == list(cekSL[4]):
			tmp.append("Normal,Rendah")
		elif lembap == list(cekSL[5]):
			tmp.append("Normal")
		elif lembap == list(cekSL[6]):
			tmp.append("Rendah")
		elif lembap == list(cekSL[7]):
			tmp.append("Rendah")

		# print(chromosome[14])
		# print(status)
		if (status == 1):
			tmp.append("Ya")
		else:
			tmp.append("Tidak")

	# print(tmp,chromosome)
	return tmp

def cekFitness(population,dataUji):
	tmp = 0
	count = 0
	listFitness = []
	for kromosom in population:
		fit = 0
		dataRule =  list(splitRule(kromosom))
		print(dataRule)
		for data in dataUji:
			for drule in dataRule:
				cekStatus = decodeChromosome(drule)
				print(cekStatus)
				print(data)
				s = cekStatus[0].split(",")
				w = cekStatus[1].split(",")
				l = cekStatus[2].split(",")
				k = cekStatus[3].split(",")		
				status = cekStatus[4]
				if data[0] in s:
					count += 1
				if data[1] in w:
					count += 1
				if data[2] in l:
					count += 1
				if data[3] in k:
					count += 1
				if data[4] in status:
					count+=1

				print("jumlah bener ",count)
				if count == 5:
					fit += 1
					count = 0				
					print("fitness ",fit)
					print()
					break
				else:
					count = 0			

		fitness = fit/80
		listFitness.append(fitness)
	return listFitness

def rouletteWheels(Fitness):
	sumFitness = sum(Fitness)
	countFitness = 0
	randomNumber = random.random()
	idx = 0
	for i in population:
		countFitness += Fitness[idx]
		if countFitness/sumFitness > randomNumber:
			return i
			break
		idx+=1

def crossOverNew(parent1,parent2):
	arr = []
	while len(arr)==0:
		tipot1a  = random.randint(1,len(parent1)-2)
		tipot1b = random.randint(tipot1a+1,len(parent1)-1)
		tp1 = [tipot1a,tipot1b]
		pc1 = tipot1a % 15	
		pc2 = tipot1b % 15
		jumlahAturan = len(parent2) // 15
		for i in range(jumlahAturan):
			for j in range(i,jumlahAturan):
				x = i *15 + pc1		
				y = j *15 + pc2
				if (x > y):
					continue
				arr.append([x,y])
	print(tp1)
	print(arr)
	tp2 = random.choice(arr)
	anak1 = (parent1[:tp1[0]]+parent2[tp2[0]:tp2[1]]+parent1[tp1[1]:])
	anak2 = (parent2[:tp2[0]]+parent1[tp1[0]:tp1[1]]+parent2[tp2[1]:])
	anak = [anak1,anak2]
	return anak

def mutate(child):
	for i in range(0,len(child)):
		prob = random.random()
		if prob<0.8:
			child[i] = random.randint(0,1)
	return child

def fitnessTerbaik(listFitness):
	x = max(listFitness)
	for i in range(len(listFitness)):
		if (listFitness[i]==x):
			return i

def elitism(listFitness):
	bestLokal = fitnessTerbaik(listFitness)
	return bestLokal

if __name__ == '__main__':
	dataUji = readTrainingData() 
	listFitness = []
	population = [[1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]]
	arr1 = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
	arr2 = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
	print(decodeChromosome(population[0]))

	x = crossOverNew(arr1,arr2)
	# listFitness = cekFitness(population,dataUji)
	# generasi = 0
	# idx = 0
	# print(listFitness)
	# print(len(population[0]))

