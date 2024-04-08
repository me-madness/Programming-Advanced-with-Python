from campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    
    def __init__(self, name, age):
      self.name = name
      self.age = age