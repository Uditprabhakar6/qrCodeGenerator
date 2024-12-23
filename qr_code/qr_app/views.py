import qrcode
import traceback
from .models import QrCodeData
from rest_framework.views import APIView
from utils.service import create_response
from django.http import HttpResponse
from io import BytesIO


class GenerateQR(APIView):
    def post(self, request):
        try:
            import ipdb;ipdb.set_trace()
            qr_name = request.data.get("qr_name")
            if not qr_name:
                return create_response(message="qr_name required")
            qr_data = request.data.get("qr_data")
            if not qr_data:
                return create_response(message="qr_data required")
            qr = qrcode.make(qr_data)
            if qr:
                qr_obj = QrCodeData(qr_name=qr_name, qr_cust_data=qr_data, qr_final_data=qr)
                qr_obj.save()
                # Save the QR code to a BytesIO stream
                img_byte_arr = BytesIO()
                qr.save(img_byte_arr, format='PNG')
                img_byte_arr.seek(0)

                # Return the image in the response
                response = HttpResponse(img_byte_arr, content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename="{qr_name}.png"'
                return response
            else:
                return create_response(message=str(traceback.format_exc()))
        except:
            return create_response(message=str(traceback.format_exc()))
            

