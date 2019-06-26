from api import db

class PdfForm(db.Model):
	pid = db.Column(db.Integer, primary_key=True)
	pname = db.Column(db.String(255), nullable=False)
	pfile = db.Column(db.LargeBinary)
	boxes = db.relationship('BoxManager', backref='box', lazy=True)

	def __init__(self,name,data):
		self.pname = name
		self.pfile = data

	def __repr__(self):
		return f'PdfForm({self.pid},{self.pname})'

class BoxManager(db.Model):
	bid = db.Column(db.Integer, primary_key=True)
	bname = db.Column(db.String(50), nullable=False)
	lx = db.Column(db.Integer, nullable=False)
	ly = db.Column(db.Integer, nullable=False)
	rx = db.Column(db.Integer, nullable=False)
	ry = db.Column(db.Integer, nullable=False)
	pid = db.Column(db.Integer, db.ForeignKey('pdf_form.pid'), nullable=False)

	def __init__(self,name,lx,ly,rx,ry):
		self.bname = name
		self.lx = lx
		self.ly = ly
		self.rx = rx
		self.ry = ry

	def __repr__(self):
		return f'BoxManager({self.bname},{self.lx},{self.ly},{self.rx},{self.ry})'