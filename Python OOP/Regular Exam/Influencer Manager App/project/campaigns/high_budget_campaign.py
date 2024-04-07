from campaigns.base_campaign import BaseCampaign



class HighBudgetCampaign(BaseCampaign):
    
    def __init__(self, name, age):
      self.name = name
      self.age = age