from datetime import datetime
from pytz import timezone

data_ = '2025-03-20 10:05:44'
formato = '%Y-%m-%d %H:%M:%S'

data_agora = datetime.now()
data_agora_timezone = datetime.now(timezone('America/Sao_Paulo'))

# data = datetime(2025,3,24,10,5,44)

data = datetime.strptime(data_, formato)

# print(data_agora.timestamp())
# print(data_agora_timezone)

nova_data_timestamp = datetime.fromtimestamp(1742877464.220397)

print(nova_data_timestamp)
