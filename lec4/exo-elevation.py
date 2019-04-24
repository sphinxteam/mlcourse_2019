# elevation for from_station_id
routes_joined = pd.merge(
    routes.rename(columns={"from_station_id":"station_id"}),
    elevations[["station_id", "elevation"]],
    how="left",
    on="station_id"
).rename(columns={
    "station_id":"from_station_id",
    "elevation":"from_elevation"
})
# elevation for to_station_id
routes_joined = pd.merge(
    routes_joined.rename(columns={"to_station_id":"station_id"}),
    elevations[["station_id", "elevation"]],
    how="left",
    on="station_id"
).rename(columns={
    "station_id":"to_station_id",
    "elevation":"to_elevation"
})
# is the route uphill, downhill or flat ?
routes_joined["delta_elevation"] = routes_joined["to_elevation"] - routes_joined["from_elevation"] 
routes_joined["elevation_type"] = np.where(
    routes_joined["delta_elevation"] < -10,
    "downhill", 
    np.where(routes_joined["delta_elevation"] > 10,
        "uphill",
        "flat"
))
routes_joined.head()

# plot number of downhill/uphill/flat trips 
alt.Chart(routes_joined).mark_bar().encode(
    x="sum(trips)", y="elevation_type", column="user_type"
)