# compute trips and days in service for each bike
bike_data = trip.groupby("bike_id").agg({"start_time":"min", "stop_time":"max", "from_station_id":"nunique", "to_station_id":"nunique"})
bike_data = bike_data.join(trip.groupby("bike_id").size().rename("trips"))
bike_data["days_in_service"] = (bike_data["stop_time"] - bike_data["start_time"]).dt.days
bike_data.head()

# scatterplot of trips vs days_in_service, one point = one bike
alt.Chart(bike_data).mark_circle().encode(x="days_in_service",y="trips")