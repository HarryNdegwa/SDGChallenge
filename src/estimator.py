
class Estimator(object):

  def __init__(self,data=None):
    if data:
      self.input_data = data
    else:
      self.input_data = {}


  def get_current_infected_estimation(self):
    reported_cases = self.input_data.get("reportedCases")
    if reported_cases != None:
      return reported_cases*10
    else:
      return 0

















def estimator(data):
  return data
