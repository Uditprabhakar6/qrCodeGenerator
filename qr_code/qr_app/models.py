from django.db import models
from base.models import BaseModel

class QrCodeData(BaseModel):
    qr_name = models.CharField(max_length=200)
    qr_cust_data = models.CharField(max_length=500)
    qr_final_data = models.CharField(max_length=1000)

    def __str__(self):
        return self.qr_name