import qrcode
from .models import QrCodeData
from rest_framework.views import APIView
from utils.service import create_response


class GenerateQR(APIView):
    def post(self, request):
        try:
            qr_name = request.data.get("qr_name")
            if not qr_name:
                return create_response(message="qr_name required")
            qr_data = request.data.get("qr_data")
            if not qr_data:
                return create_response(message="qr_data required")
            qr = qrcode.make(qr_data)
            if qr:
                qr_obj = QrCodeData(qr_name=qr_name, qr_cust_data=qr_data, qr_final_dat=qr)
