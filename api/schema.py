from api import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class BoxManagerSchema(ma.Schema):
	class Meta:
		fields = ('bid','bname','lx','ly','rx','ry')

class PdfFormSchema(ma.Schema):
	class Meta:
		fields = ('pid','pname')

box_manager_schema = BoxManagerSchema(many=True,strict=True)
pdf_form_schema = PdfFormSchema(strict=True)