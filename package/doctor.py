from flask_restful import Resource, Api, request
from package.model import conn
class Doctors(Resource):
    """API untuk mengambil keseluruhan data dokter"""

    def get(self):
        """API List Dokter"""

        doctors = conn.execute("SELECT * FROM doctor ORDER BY doc_date DESC").fetchall()
        return doctors

    def post(self):
        """API Tambah dokter"""

        doctorInput = request.get_json(force=True)
        doc_first_name=doctorInput['doc_first_name']
        doc_last_name = doctorInput['doc_last_name']
        doc_ph_no = doctorInput['doc_ph_no']
        doc_address = doctorInput['doc_address']
        doctorInput['doc_id']=conn.execute('''INSERT INTO doctor(doc_first_name,doc_last_name,doc_ph_no,doc_address)
            VALUES(?,?,?,?)''', (doc_first_name, doc_last_name,doc_ph_no,doc_address)).lastrowid
        conn.commit()
        return doctorInput

class Doctor(Resource):
    """API yang mengatur data tunggal dokter"""

    def get(self,id):
        """API untuk mengambil data tunggal dokter lewat ID"""

        doctor = conn.execute("SELECT * FROM doctor WHERE doc_id=?",(id,)).fetchall()
        return doctor

    def delete(self, id):
        """API untuk menghapus data tunggal dokter lewat ID"""

        conn.execute("DELETE FROM doctor WHERE doc_id=?", (id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """API untuk update data tunggal dokter lewat ID"""

        doctorInput = request.get_json(force=True)
        doc_first_name=doctorInput['doc_first_name']
        doc_last_name = doctorInput['doc_last_name']
        doc_ph_no = doctorInput['doc_ph_no']
        doc_address = doctorInput['doc_address']
        conn.execute(
            "UPDATE doctor SET doc_first_name=?,doc_last_name=?,doc_ph_no=?,doc_address=? WHERE doc_id=?",
            (doc_first_name, doc_last_name, doc_ph_no, doc_address, id))
        conn.commit()
        return doctorInput