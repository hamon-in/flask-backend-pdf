from api import db

class PdfForm(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	data = db.Column(db.LargeBinary)
	boxes = db.relationship('BoxManager', backref='box', lazy=True)

	def __init__(self,name,data):
		self.name = name
		self.data = data

	def __repr__(self):
		return f'PdfForm({self.id},{self.name})'

class BoxManager(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	top_lt_x = db.Column(db.Integer, nullable=False)
	top_lt_y = db.Column(db.Integer, nullable=False)
	btm_rt_x = db.Column(db.Integer, nullable=False)
	btm_rt_y = db.Column(db.Integer, nullable=False)
	pdf_id = db.Column(db.Integer, db.ForeignKey('pdf_form.id'), nullable=False)

	def __init__(self,name,tx,ty,bx,by):
		self.name = name
		self.top_lt_x = tx
		self.top_lt_y = ty
		self.btm_rt_x = bx
		self.btm_rt_y = by

	def __repr__(self):
		return f'BoxManager({self.name},{self.top_lt_x},{self.top_lt_y},{self.btm_rt_x},{self.btm_rt_y})'