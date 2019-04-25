import pandas as pd

trips = pd.DataFrame({
    "date":['2018-10-01','2018-10-02','2018-10-03'],
    "trips":[421,212,183]
})
trips.to_csv("fake_trips.csv",index=False)

weather = pd.DataFrame({
    "date":['2018-10-01','2018-10-03'],
    "event":["sun","rain"],
    "temperature":[15,7]
})
weather.to_csv("fake_weather.csv",index=False)

medical_test = pd.DataFrame({
    "treatment": ["A", "A", "B", "B", "B"],
    "age": [20, 32, 12, 45, 80],
    "sick": [True, False, False, False, True]
})
medical_test.to_csv("fake_medical_test.csv", index=False)

sensor_data = pd.DataFrame({
  "date":["2018-01-01"]*2+["2018-01-02"]*3,
  "sensor":["pressure","temperature","pressure","temperature","humidity"],
  "values":[101, 19, 100, 21, 30]
})
sensor_data.to_csv("fake_sensor_data.csv", index=False)

glucose_levels = pd.DataFrame({
    "patient": [1, 2, 3, 4],
    "age": [30, 60, 20, 21],
    "treatment": ["A", "A", "B", "B"],
    "2018-01-01":[80, 125, 143, 90],
    "2018-01-02":[85, 128, 142, 93],
    "2018-01-03":[82, 122, 147, 92],
    "2018-01-04":[81, 123, 141, 92]
})
glucose_levels.to_csv("fake_glucose_levels.csv", index=False)
