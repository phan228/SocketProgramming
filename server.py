import socket
import os
import threading
import datetime
import time

SEPARATOR = "<SEPARATOR>"
pathClient = '/Users/thttien/documents/1_Susu/spring2020/cs371/Client/'
pathServer = '/Users/thttien/documents/1_Susu/spring2020/cs371/Server/'
pathInfo = '/Users/thttien/documents/1_Susu/spring2020/cs371/Info/'
path371 = '/Users/thttien/documents/1_Susu/spring2020/cs371/'

def download(file, socket):
	filename = socket.recv(1024)

	# if the file we want to download exists
	os.chdir(pathServer)
	if os.path.isfile(filename):
		socket.send("FOUND" + str(os.path.getsize(filename)))
		clientRes = socket.recv(1024)
		if clientRes[:1] == 'y':
			with open(filename, 'rb') as f:
				data = f.read(1024)
				socket.send(data)
				# In case the file is more than 1024 bytes
				while data != "":
					data = f.read(1024)
					socket.send(data)
		else:
			print("Download cancelled")

	# if the file is not there
	else:
		socket.send("ERROR")

def Main():
	# Create the socket
	# AF_INET == ipv4
	# SOCK_STREAM == TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Binding
	host = socket.gethostname()
	port = 5000
	s.bind((host, port))

	# Listen
	s.listen(5)

	while True:
		# Accept
		connection, address = s.accept()
		print("Connection from : " + str(address))

		action = connection.recv(1024)

		# Send/ receive
		if action ==  "download":
			t = threading.Thread(target=download, args=("retrThread", connection))
			t.start()

		if action == "upload":
			filename = connection.recv(1024)
			size = connection.recv(1024)
			filesize = int(size)
			start_time = time.time()
			print("Uploading...")
			with open(pathServer + 'uploaded_' + filename, "wb") as uploaded:
				bytes_read = connection.recv(1024)
			
				# write to the file the bytes we just received
				uploaded.write(bytes_read)
				received = len(bytes_read)
				elasped_time = time.time() - start_time
				if elasped_time > 0:
					upload_speed = received/(1000000 * elasped_time)
					upload_speed = str(round(upload_speed, 2))
				else:
					upload_speed = 'TOO FAST'
					print(upload_speed)
				# Make sure to get all data
				count = 0
				while received < filesize:
					go  = time.time()
					data = connection.recv(1024)
					uploaded.write(data)
					received += len(data)
					elasped_time = time.time() - start_time
					count += 1
					if elasped_time > 0:
						upload_speed = received/(1000000 * elasped_time)
						upload_speed = str(round(upload_speed, 2))
						if (count % 10000) == 0:
							print(upload_speed)
					else:
						upload_speed = 'TOO FAST'
						print(upload_speed)			    
			# Done downloading
			uploaded.close()
			elasped_time = time.time() - start_time
			if elasped_time > 0:
				avg_upload_speed = filesize/(1000000 * elasped_time)
				avg_upload_speed = str(round(avg_upload_speed, 2))
			else:
				avg_upload_speed = 'FAST'

			print("Average upload speed = " + avg_upload_speed + " mbps")
			
			now = datetime.datetime.now()
			info = open(pathInfo + "info.txt", 'a')
			info.write(filename + " " + str(filesize) + " bytes " + str(now) + '\n')
			info.close()

			print("Upload completed!")

		if action  == "delete":
			filename = connection.recv(1024)
			os.chdir(pathServer)
			if os.path.isfile(filename):
				os.remove(filename)
				print(filename + " removed!")
			else:
				os.chdir(pathClient)
				if os.path.isfile(filename):
					os.remove(filename)
					print(filename + " removed!")
				else:
					print(filename + " does not exists!")
			os.chdir(pathServer)

		if action == "dir":
			os.chdir(path371)
			foldername = connection.recv(1024)
			if os.path.isdir(foldername):
				files = os.listdir(foldername)
				for file in files:
					here = False
					info = open(pathInfo + "info.txt", 'r')  
					dload = open(pathInfo + "downloadRecord.txt", 'r')
					for x in info:
						read = x.split()
						if read[0] == file:
							here = True
							print(x.strip())
					
					for i in dload:
						read = i.split()
						if (read[0] == file):
							here = True
							print(i.strip())
					if here == False:
						print(file)
					info.close()
					dload.close()
			else:
				print("Folder does not exsist!")		


	# Close the connection
	connection.close()
	s.close()

if __name__ == '__main__':
	Main()
	