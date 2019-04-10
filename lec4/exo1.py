# checking trip_id and bike_id
print(f"trip: {trip.shape[0]} rows {trip.shape[1]} columns\n")
n_trip_id = trip["trip_id"].nunique()
print(f"There are {n_trip_id} distinct trip_id\n")
n_bike_id = trip["bike_id"].nunique()
print(f"There are {n_bike_id} distinct bike_id\n")
print(trip.dtypes)

# gender and usertype values are okay
trip[["gender","usertype"]].describe().T

# birthyear values are okay
trip[["birthyear"]].describe().T

# checking weather dataset
print(f"weather: {weather.shape[0]} rows {weather.shape[1]} columns\n")
print(trip.dtypes)

# Date values are okay
weather[["Date"]].describe().T

# Events values are okay
weather[["Events"]].describe().T

# numeric columns values are okay
weather.describe().T