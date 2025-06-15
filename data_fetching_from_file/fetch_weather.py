import os
import gzip
import pandas as pd
import csv
from datetime import datetime




def process_inverter_data(data):
    """Extract inverter data."""
    inverter_data = []
    for i in range(len(data)):
        row = str(data.iloc[i:i+1]).split(";")
        if "Inverter" in row:
            inv_data = str(data.iloc[i + 2:i + 3]).split(";")[5:]
            inv_index = row[6]
            inverter_entry = {"invt_id": row[7], 'invt_no': inv_index,'device_type':'INV','plant_srno':str(data.iloc[i:i+1]).split(";")[3]}
            inverter_entry.update({
                str(j + 1): (inv_data[j]) if inv_data[j] != 'NA' else -1
                for j in range(len(inv_data))
            })
            inverter_data.append(inverter_entry)
    return inverter_data

def process_meter_data(data):
    """Extract meter data."""
    meter = []
    for i in range(len(data)):
        row = str(data.iloc[i:i+1]).split(";")
        if "Meter" in row:
            met_data = str(data.iloc[i + 2:i + 3]).split(";")[5:]
            met_index = row[6]
            meter_entry = {"meter_id": row[7], 'meter_no': met_index,'plant_srno':str(data.iloc[i:i+1]).split(";")[3],'device_type':'METER'}
            meter_entry.update({
                str(j + 1): float(met_data[j]) if met_data[j] != 'NA' else -1
                for j in range(len(met_data))
            })
            meter.append(meter_entry)
    return meter

def process_weather_data(data):
    """Extract weather data."""
    weather = {}
    for i in range(len(data)):
        row = str(data.iloc[i:i+1]).split(";")
        if "Weather" in row:
            weather_data = str(data.iloc[i + 2:i + 3]).split(";")[5:]
            weather = {
                "plant_srno": str(data.iloc[i:i+1]).split(";")[3],"ws_id":row[-3],"ws_no":row[-3],"device_type":"WMS",
                **{str(j + 1): float(weather_data[j]) for j in range(len(weather_data))}
            }
    return weather


csv_file = "C:\\Users\\Bikash Chandra Sahoo\\OneDrive\\Desktop\\GenSOM ERP\\newfile.csv"
folder_path='C:\\Users\\Bikash Chandra Sahoo\\OneDrive\\Desktop\\New folder'
all_files=os.listdir(folder_path)

for file_path in all_files:
    with gzip.open(f"{folder_path}/{file_path}", "rt", encoding="ISO-8859-1") as file:
        data = pd.read_csv(file)
        # weather = {}
        inverter_data = process_inverter_data(data)
        print(inverter_data)
        
        
#         for i in range(len(data)):
#             row = str(data.iloc[i:i+1]).split(";")
#             weather_data1 = str(data.iloc[1:2]).split(";")
#             data_date = datetime.strptime(weather_data1[-2].split(" ")[-1], "%d/%m/%y-%H:%M:%S")
            
#             if "Weather" in row:
#                 weather_data = str(data.iloc[i + 2:i + 3]).split(";")[5:]
#                 weather = {
#                     "plant_srno": str(data.iloc[i:i+1]).split(";")[3],
#                     "ws_id": row[-3],
#                     "ws_no": row[-3],
#                     "device_type": "WMS",
#                     **{str(j + 1): float(weather_data[j]) for j in range(len(weather_data))}
#                 }

#         df = pd.DataFrame([weather])
#         data_val = df['2']  # Adjust column name if needed

#         json_data = {
#             'data_timestamp': data_date.strftime('%Y-%m-%d %H:%M:%S'),
#             'data_value': list(data_val.to_dict().values())[0]
#         }

#         # Write to CSV file
#         file_exists = os.path.exists(csv_file)
        
#         with open(csv_file, 'a', newline='') as f:
#             writer = csv.DictWriter(f, fieldnames=json_data.keys())
#             if not file_exists:
#                 writer.writeheader()  # Write header if file doesn't exist
#             writer.writerow(json_data)

# df = pd.read_csv(csv_file, names=['data_timestamp', 'data_value'], header=None)

# df_sorted_desc = df.sort_values(by='data_timestamp', ascending=True)
# print(df_sorted_desc)

