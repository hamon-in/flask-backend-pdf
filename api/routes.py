from api.models import PdfForm, BoxManager
from flask import request, jsonify
from api import app, db
from api.schema import boxes_manager_schema, pdf_form_schema
import json

@app.route('/read_pdf', methods=['POST'])
def read_pdf():
	#import pdb;pdb.set_trace()
	print(request.form['box_data'])
	print(json.loads(request.form['box_data']))

	pdf_file = request.files['pdf_file']
	box_arr = json.loads(request.form['box_data'])
	#create a pdf instance by passing respective data
	pdf_instance = PdfForm(pdf_file.filename,pdf_file.read())
	#save to database
	db.session.add(pdf_instance)
	db.session.commit()

	for box in box_arr:
		#create a box instance by passing respective data
		box_instance = BoxManager(box[0],box[1],box[2],box[3],box[4])
		box_instance.pdf_id = pdf_instance.id
		#save it to the database
		db.session.add(box_instance)
		db.session.commit()

	return boxes_manager_schema.jsonify(pdf_instance.boxes)