import numpy as np
import copy
import time
import random
import math


real_sol=[]
data_length=0
data_int=[]

#讀檔
def readfile(file):
	j=0;
	i=0;
	global data_length


	f=open(file,mode='r');
	data_str=f.readlines()  #逐行讀取txt並存成list。每行是list的一個元素，資料型別為str
	f.close();

	#算出有幾個城市
	data_length=len(data_str); 
	
	#把資料轉成int，存到data_int
	for i in range(data_length): 
		for j in range(len(list(data_str[0].split()))):
			data_int.append(int(data_str[i].split(' ')[j]));

	#把data_int轉成二維的
	city=np.zeros((data_length,3));
	for i in range(data_length):
		for j in range(3):
			city[i][j]=data_int[i*3+j];

	#算出個城市之間的距離
	cost=np.zeros((data_length,data_length));
	for i in range(data_length):
		for j in range(i+1,data_length):
			cost[i][j]=pow(pow((city[i][1]-city[j][1]),2)+pow((city[i][2]-city[j][2]),2),0.5);
			cost[j][i]=cost[i][j];


	return city,cost

#Simulated Annealing Algorithms
def SA(T,T_end,q,L,tmp_sol):
	minCost=99999.99
	minTour=[]
	while T >= T_end:
		for i in range(L):
			new_sol=create_new_sol(tmp_sol) #做一個新的路徑
			f1=path_len(tmp_sol) #舊的路徑長
			f2=path_len(new_sol) #新的路徑長
			df=f2-f1
			if(df<0): #新的路徑比舊的好就取代
				tmp_sol=copy.deepcopy(new_sol)
				if(f2<minCost):
					minTour=copy.deepcopy(tmp_sol)
					minCost=f2
			else:
				r=random.uniform(0.0,1.0) #如果比這個隨機數大就取代
				if(math.exp((f1-f2)/T)>=r):
					tmp_sol=copy.deepcopy(new_sol)
		T=T*q
		print("Temperature: ", T)
	return minTour


#做一個隨機新的路徑
def create_new_sol(tmp_sol):
	new_sol=[]
	new_sol=copy.deepcopy(tmp_sol)
	#隨機生成兩個城市進行交換
	index1=random.randint(1,data_length-2)
	index2=random.randint(1,data_length-2)
	tmp=new_sol[index1]
	new_sol[index1]=new_sol[index2]
	new_sol[index2]=tmp

	return new_sol

#算出路徑長
def path_len(path):
	total_len=0.0
	num_city=len(path)
	for i in range(num_city-1):
		total_len=total_len+cost[path[i]-1][path[i+1]-1]
		
	return total_len





#把答案存起來
def writefile(city,real_sol,time_period):
	f_draw = open('draw.txt', 'w')
	f_output = open('output.txt','w')
	for i in range(data_length+1):
		print(int(city[real_sol[i]-1][1]),'', end='',file=f_draw)
		print(int(city[real_sol[i]-1][2]),file=f_draw)
	print("Optimal Visit Order: ",end='',file=f_output)
	for i in range(data_length+1):
		print(data_int[(real_sol[i]-1)*3],' ',end='',file=f_output)
	print('\n',end='',file=f_output)
	print("Optimal Distance： ",path_len(real_sol),file=f_output)
	print("Execution Time: ",time_period," (s)",file=f_output)
	f_draw.close()
	f_output.close()

if __name__=='__main__':

	#Initial Temperature
	T=100.0
	#End Temperature
	T_end=(1e-4)
	#Annealing Factor
	q=0.99
	#Number of Iterative
	L=1000

	#記錄起始時間
	start_time=time.time()
	#讀readfile.txt，算出個城市間的距離存在cost
	file = 'readfile.txt'
	city,cost=readfile(file)
	#做一個初始的答案:[1,2,3,4,5.....,end]
	tmp_sol=[]
	for i in range(1,data_length+1):
		tmp_sol.append(i)
	#Simulated Annealing
	minTour=SA(T,T_end,q,L,tmp_sol)
	#回到城市原點
	minTour.append(1)
	#Execution Time
	Exe_time=time.time()-start_time

	print("Optimal Visit Order:",minTour)
	print("Optimal Distance:",path_len(minTour))
	print("Execution Time: ",Exe_time)

	#寫入檔案
	writefile(city,minTour,Exe_time)
