# number of trips for each route and user type
routes = trip.groupby(
    ["user_type","from_station_id","to_station_id"]
).size().rename("trips").reset_index()
# create a boolean column telling whether the user is a member or not 
routes["member"] = routes["user_type"]=="Member"
# sort by number of trips
routes = routes.sort_values(by="trips", ascending=0)

# most popular routes for members
routes.query("member").head(5)

# most popular routes for non-members
routes.query("~member").head(5)