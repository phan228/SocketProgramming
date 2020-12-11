import socket
import os
import time

SEPARATOR = "<SEPARATOR>"
pathClient = '/Users/thttien/documents/1_Susu/spring2020/cs371/Client/'
pathServer = '/Users/thttien/documents/1_Susu/spring2020/cs371/Server/'
pathInfo = '/Users/thttien/documents/1_Susu/spring2020/cs371/Info/'

def Main():
	# Create the socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect
	host = socket.gethostname()

	# Send/ receive
	print("Enter \"connect\", \"download\", \"upload\", \"delete\", \"dir\" (or \"q\" to quit)")
	action = raw_input("-> ")
	
	if action == "connect":
			portNum = raw_input("Port: ")
			port = int(portNum)
			s.connect((host, port))
			action = raw_input("-> ")

	if action != 'q':
		port = 5000
		s.connect((host, port))	

		s.send(action)
		if action == 'download':
			filename = raw_input("Filename: ")
			s.send(filename)
			data = s.recv(1024)
			if data[:5] == 'FOUND':
				filesize = long(data[5:])
				response = raw_input("File exists, download? (y/n): ")
				s.send(response)
				# Save the file after download
				if response == 'y':
					start_time = time.time()
					# new file
					downloaded = open(pathClient + 'downloaded_' + filename, 'wb')	
					# Receive downloaded data and write it in the new file
					data = s.recv(1024)
					downloaded.write(data)
					received = len(data)
					elasped_time = time.time() - start_time
					if elasped_time > 0:
						download_speed = received/(1000000 * elasped_time)
						download_speed = str(round(download_speed, 2))
					else:
						download_speed = 'TOO FAST'
						print(download_speed)
					# Make sure to get all data
					count = 0
					while received < filesize:
						data = s.recv(1024)
						received += len(data)
						downloaded.write(data)
						elasped_time = time.time() - start_time
						count += 1
						if elasped_time > 0:
							download_speed = received/(1000000 * elasped_time)
							download_speed = str(round(download_speed, 2))
							if (count % 12000) == 0:
								print(download_speed)
						else:
							download_speed = 'TOO FAST'
							print(download_speed)
					# Done downloading
					downloaded.close()
					elasped_time = time.time() - start_time
					if elasped_time > 0:
						avg_download_speed = filesize/(1000000 * elasped_time)
						avg_download_speed = str(round(avg_download_speed, 2))
					else:
						avg_download_speed = 'FAST'

					print("Average download speed = " + avg_download_speed + " mbps")

					info = open(pathInfo + 'downloadRecord.txt', 'a+')
					if os.stat(pathInfo + "downloadRecord.txt").st_size == 0:
						info.write(filename + " " + "1 \n")
					else:
						exist = False
						for line in info:
							print(line)
							read = line.split()
							if read[0] == filename:
								exist = True
								newNum = int(read[1]) 
								newNum += 1
								line.replace(read[1], str(newNum))
								print(read[1])
								break
						
						if exist == False:
							numDownload = 1
							info.write(filename + " " + str(numDownload) + "\n")
					
					info.close()
					print("Download completed!")
			else:
				print("Error!")

		if action == 'upload':
			filename = raw_input("Filename: ")
			os.chdir(pathClient)
			if os.path.isfile(filename):
				filesize = os.path.getsize(filename)
				s.send(filename)
				s.send(str(filesize))			
				with open(filename, 'rb') as f:
					data = f.read(1024)
					s.send(data)
					# In case the file is more than 1024 bytes
					while data != "":
						data = f.read(1024)
						s.send(data)
					f.close()
			else:
				print("Error!")

		if action == 'delete':
			filename = raw_input("Filename: ")
			s.send(filename)

		if action == 'dir':
			foldername = raw_input("Folder name: ")
			s.send(foldername)

	# Close the connection
	s.close()

if __name__ == '__main__':
	Main()
	