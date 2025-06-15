

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
                str(j + 1): float(inv_data[j]) if inv_data[j] != 'NA' else -1 
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