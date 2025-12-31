import pandas as pd


df = pd.read_csv("taxi_hotspot_dataset.csv")

df.columns = df.columns.str.strip()
lat_col = 'latitude' if 'latitude' in df.columns else 'lat'
lon_col = 'longitude' if 'longitude' in df.columns else 'lon'


df = df.dropna(subset=[lat_col, lon_col, 'car_id', 'fare', 'timestamp'])
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['fare'] = pd.to_numeric(df['fare'], errors='coerce')

df = df.sort_values('timestamp').reset_index(drop=True)

valid_clusters = []
grouped = df.groupby([lat_col, lon_col])

for (lat, lon), group in grouped:
    group = group.sort_values('timestamp')
    trips = group.to_dict('records')
    for i in range(len(trips) - 2):
        trip1, trip2, trip3 = trips[i], trips[i+1], trips[i+2]
        if len({trip1['car_id'], trip2['car_id'], trip3['car_id']}) != 3:
            continue
        A, B, C = float(trip1['fare']), float(trip2['fare']), float(trip3['fare'])
        if round(B, 2) == round(abs(A - C) + (A % C), 2):
            valid_clusters.append({
                'trips': [trip1, trip2, trip3],
                'score': A + B + C,
                'earliest_time': trip1['timestamp']
            })

if not valid_clusters:
    print("No valid clusters found!")
    exit()

valid_clusters.sort(key=lambda x: x['earliest_time'])
earliest_cluster = valid_clusters[0]

A, B, C = [float(t['fare']) for t in earliest_cluster['trips']]


lat_min, lat_max = 35.55, 35.57
lon_min, lon_max = 6.17, 6.20


total_fare = A + B + C
frac_A = (A % total_fare) / total_fare
frac_B = (B % total_fare) / total_fare


lat = lat_min + frac_A * (lat_max - lat_min)
lon = lon_min + frac_B * (lon_max - lon_min)

lat = round(lat, 5)
lon = round(lon, 5)


print(" Refined Real Hotspot in Batna:")
print("Latitude:", lat)
print("Longitude:", lon)
print("Google Maps link:", f"https://www.google.com/maps?q={lat},{lon}")


print("\nEarliest cluster fares:", A, B, C)
