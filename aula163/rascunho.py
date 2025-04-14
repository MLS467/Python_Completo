from datetime import datetime  # timedelta,
from dateutil.relativedelta import relativedelta

# data_nascimento = datetime.strptime('1992-05-08 11:50:00', "%Y-%m-%d %H:%M:\
# %S")

# # data_nova = datetime.strptime('1995-05-24 02:07:01', "%Y-%m-%d %H:%M:%S")
# # diferenca = - (data_nascimento - data_nova)
# # print(diferenca.days / 365)

# mais_dez = timedelta(days=10)

# print(data_nascimento + mais_dez)


# print('relative', data_nascimento + relativedelta(days=12000))
# print('relative', data_nascimento + relativedelta(seconds=60))

formato = "%Y-%m-%d %H:%M:%S"
data_nasc_m = datetime.strptime("1995-05-24 11:30:00", formato)
data_nasc_l = datetime.strptime("1992-05-8 9:00:00", formato)

diferenca = relativedelta(data_nasc_m, data_nasc_l)

print(diferenca.days)
print(diferenca.years)
