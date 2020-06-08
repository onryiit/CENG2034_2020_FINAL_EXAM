import os 
import urllib.request
import hashlib
import sys
import multiprocessing 
from itertools import product

#This all urls and you can enter as many urls as you want.
url_list=[
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"
,"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg"
]


check = os.fork() #This separates as parent and child to 2 and parent has real pid.


# n greater than 0  means parent process 
if (check > 0): 
	#I used the os.wait() command so that the parent and child process did not interfere.		
	os.wait()
	print("Parent process and id is : ", os.getpid()) 

    
#If n equals 0, it means child process.
elif check==0: 
	
	print("Child process and id is : ", os.getpid()) 
	
	print("Starting file download...")
	
	
	

	urllib.request.urlretrieve(url_list[0], "/home/onur/Masaüstü/picture/picture1")
	urllib.request.urlretrieve(url_list[1], "/home/onur/Masaüstü/picture/picture2")
	urllib.request.urlretrieve(url_list[2], "/home/onur/Masaüstü/picture/picture3")
	urllib.request.urlretrieve(url_list[3], "/home/onur/Masaüstü/picture/picture4")
	urllib.request.urlretrieve(url_list[4], "/home/onur/Masaüstü/picture/picture5")
	

	print("All files downloaded!")
	



	#List of downloaded pictures.
	pictures = os.listdir("/home/onur/Masaüstü/picture")

	#Function to return hash code of images.
	def hash_code (file):
		MD_hash = hashlib.md5()
		pic = open(file, "rb")
		MD_hash.update(pic.read())
		return(MD_hash.hexdigest())
        #I use this algorithm to check photos or pictures that are dublicate.
	def duplicates(h,h1):
		if h[0]!=h1[0]:
			if h[1] == h1[1]:
				print("This file:" ,h1[0], "and" , h1[0] , " same." )

	#Hash code of downloaded photos with multiprocessing.
	hashes=[]
	for i in pictures:
		hashes.append((i, hash_code("/home/onur/Masaüstü/picture/" + i)))
	if __name__ == '__main__': 
		multiproc = multiprocessing.Pool()
		multiproc.starmap(duplicates, product(hashes, repeat =2))

#In these codes, the codes used when getting and comparing the hash code without using multiple operations
#At first, I couldn't do it with multiprocessing, but I didn't want to delete it.
'''
#I have written a program for it that may have copies files in the hash list
x=set(hashes)
copies=[]
for c in x:
    if(hashes.count(c)>1):
        copies.append(c)

#To delete duplicated images I use such an algorithm.
for i in copies:
	index = hashes.index(i)
	os.remove('/home/onur/Masaüstü/picture/' + pictures.pop(index))
	
'''
