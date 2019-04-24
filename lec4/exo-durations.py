# trip duration in minutes
trip["trip_minutes"] = trip["trip_duration"].div(60).round(0)

# normalized histogram 
durations = trip.groupby("user_type")["trip_minutes"]\
.value_counts(normalize=True).rename("frequency").reset_index()
durations.head()

# plot the normalized histograms
alt.Chart(
    durations
).mark_line(interpolate='step').encode(
    x="trip_minutes", y="frequency", color="user_type"
).interactive(bind_y=False)