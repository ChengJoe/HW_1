# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108060010.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
#創建目標 station ID 的列表
station_id = ['C0F9A0', 'C0A880', 'C0G640', 'C0R190', 'C0X260']
goal_data = []

#sort 目標 station ID 列表
station_id = sorted(station_id)

#將目標 station 的資料擷取出來
ID_and_TEMP = []

for station in station_id:
   temp_list = list(filter(lambda item: item['station_id'] == station, data))
   temp_list_filtered = []
   for row in temp_list:
      temp_list_filtered.append(list([row['station_id'], float(row['H_FX'])]))    
   ID_and_TEMP.append(temp_list_filtered)

#去除異常值、求出最大值
ID_and_TEMP_cleaned = []
max_data_in_each_station = []

for id_and_temp in ID_and_TEMP:
   id = id_and_temp[0][0]
   id_and_temp = [each_id_temp for each_id_temp in id_and_temp if each_id_temp[1] != -99.0 and each_id_temp[1] != -999.0]
   ID_and_TEMP_cleaned.append(id_and_temp)
   if id_and_temp == []:
      max_data_in_each_station.append([id, 'None'])
   else:
      max_data_in_each_station.append(max(id_and_temp))
#=======================================

# Part. 4
#=======================================
#列印

print(max_data_in_each_station)
#=======================================
