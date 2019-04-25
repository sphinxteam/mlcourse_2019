# checking trip_id and bike_id
print(f"trip: {trip.shape[0]} rows {trip.shape[1]} columns\n")
n_trip_id = trip["trip_id"].nunique()
print(f"There are {n_trip_id} distinct trip_id\n")
n_bike_id = trip["bike_id"].nunique()
print(f"There are {n_bike_id} distinct bike_id\n")
print(trip.dtypes)

# gender and usertype values are okay
trip[["gender","user_type"]].describe().T

# birthyear values are okay
trip[["birth_year"]].describe().T

# checking weather dataset
print(f"weather: {weather.shape[0]} rows {weather.shape[1]} columns\n")
print(weather.dtypes)

# Date values are okay
weather[["date"]].describe().T

# Events values are okay
weather[["events"]].describe().T

# numeric columns values are okay
weather.describe().T