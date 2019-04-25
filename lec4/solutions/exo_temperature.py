# create the weekend column
daily_trips_joined["day_name"] = daily_trips_joined["date"].dt.day_name()
daily_trips_joined["weekend"] = daily_trips_joined["day_name"].isin(["Sunday", "Saturday"])

# scatterplot of trips versus temperature, one point = one day
alt.Chart(daily_trips_joined).mark_point().encode(
    x="mean_temperature", y="trips", color="user_type", column="weekend"
)

# trips versus weather events, one tick = one day 
alt.Chart(daily_trips_joined).mark_tick().encode(
    y="events", x="trips", column="user_type"
)

# median of trips versus weather events 
alt.Chart(daily_trips_joined).mark_bar().encode(
    y="events", x="median(trips)", column="user_type"
)