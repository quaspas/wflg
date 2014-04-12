from django.db import models
from whatsforlunch.search.connect import api_request


class Place(models.Model):

    api_id = models.CharField()

    @property
    def info(self):
        params = {'id':self.api_id}
        return api_request(params,path='/v2/business')

