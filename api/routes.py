from api.models import PdfForm, BoxManager
from flask import request, jsonify
from api import app, db
from api.schema import boxes_manager_schema, pdf_form_schema
import json

@app.route('/post_pdf', methods=['POST'])
def post_pdf():
	pfile = request.files['pfile']
	box_arr = json.loads(request.form['box_data'])
	#create a pdf instance by passing respective data
	pdf_instance = PdfForm(pfile.filename,pfile.read())
	#save to database
	db.session.add(pdf_instance)
	db.session.commit()

	return pdf_form_schema.jsonify(pdf_instance)

"""	for box in box_arr:
		#create a box instance by passing respective data
		box_instance = BoxManager(box[0],box[1],box[2],box[3],box[4])
		box_instance.pdf_id = pdf_instance.id
		#save it to the database
		db.session.add(box_instance)
		db.session.commit()

	return boxes_manager_schema.jsonify(pdf_instance.boxes)"""


@app.route('/put_boxes/<int:pid>', methods=['PUT'])
def put_boxes(pid):
	#get box data from request
	pid = request.form['pid']
