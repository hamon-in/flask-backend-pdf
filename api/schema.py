from api import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class BoxManagerSchema(ma.Schema):
	class Meta:
		fields = ('id','name','top_lt_x','top_lt_y','btm_rt_x','btm_rt_y')

class PdfFormSchema(ma.Schema):
	class Meta:
		fields = ('id','name')

boxes_manager_schema = BoxManagerSchema(many=True,strict=True)
pdf_form_schema = PdfFormSchema(strict=True)