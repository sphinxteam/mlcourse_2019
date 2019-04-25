# extract hour and day name from start_time
trip["hour"] = trip["start_time"].dt.hour
trip["day_name"] = trip["start_time"].dt.day_name()

# trips per hour, day of week, for each user type
user_type_trips = trip.groupby(["hour","day_name","user_type"]).size().rename("trips").reset_index()
user_type_trips.head()

# visualization
alt.Chart(user_type_trips).mark_line().encode(
    x='hour',y="sum(trips)",color="day_name",column="user_type"
)