
class Estimator(object):

  def __init__(self,data=None):
    if data:
      self.input_data = data
    else:
      self.input_data = {}

    self.reported_cases = self.input_data.get("reportedCases")


  def get_current_infected_estimation(self):
    if self.reported_cases != None:
      return self.reported_cases*10
    return 0


  def get_severe_current_infected_estimation(self):
    if self.reported_cases != None:
      return self.reported_cases*50
    return 0



payload = {
    "region":{
        "name":"Africa",
        "avgAge":19.7,
        "avgDailyIncomeInUSD":5,
        "avgDailyIncomePopulation":0.71
    },
    "periodType":"Days",
    "timeToElapse":58,
    "reportedCases":674,
    "population":66622705,
    "totalHospitalBeds":1380614
}


e = Estimator(payload)

print(e.get_current_infected_estimation())
print(e.get_severe_current_infected_estimation())










def estimator(data):
  return data
