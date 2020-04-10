import math,decimal


class Estimator(object):

  def __init__(self,data=None):
    if data:
      self.input_data = data
    else:
      self.input_data = {}

    self.reported_cases = self.input_data.get("reportedCases")
    # to set the factor instance variable
    self.period_factor_calculator()


  def get_current_infected_estimation(self):
    if self.reported_cases != None:
      return self.reported_cases*10
    return 0


  def get_severe_current_infected_estimation(self):
    if self.reported_cases != None:
      return self.reported_cases*50
    return 0


  def period_normaliser_to_days(self):
    days = "days"
    weeks = "weeks"
    months = "months"
    days_in_a_week = 7
    days_in_a_month = 30

    period_type = self.input_data.get("periodType")
    elapse_time = self.input_data.get("timeToElapse")

    if str(period_type).casefold() == days.casefold():
      return elapse_time
    elif str(period_type).casefold() == weeks.casefold():
      return elapse_time*days_in_a_week
    elif str(period_type).casefold() == months.casefold():
      return elapse_time*days_in_a_month


  def period_factor_calculator(self):
    infections_to_double_period_in_days = 3
    days = self.period_normaliser_to_days()
    self.factor = math.floor(days/infections_to_double_period_in_days)
    return self.factor


  def get_projected_number_of_infections(self):
    current_infections_estimation = self.get_current_infected_estimation()
    return current_infections_estimation*(2**self.factor) 


  def get_projected_number_of_severe_infections(self):
    current_severe_infections_estimation = self.get_severe_current_infected_estimation()
    return current_severe_infections_estimation*(2**self.factor)





def estimator(data):
  return data
