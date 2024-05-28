import uuid
import os
import threading

def worker():
	while True:
		uuidGen = uuid.uuid4().hex

		if not os.path.exists(uuidGen):
			with open(f"{uuidGen}", "w") as f:
				f.write(f"{uuidGen}")
				print(uuidGen)
		else:
			print("File already existing exist.")

# "100" is the number of worker, can be change
for i in range(100):
	t = threading.Thread(target=worker)
	t.start()
