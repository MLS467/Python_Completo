from datetime import datetime

data_ = '2025-03-20 10:05:44'
formato = '%Y-%m-%d %H:%M:%S'



# data = datetime(2025,3,24,10,5,44)
data = datetime.strptime(data_,formato)

print(data)