from flask_restful import Resource, Api, request
from package.model import conn

class Patients(Resource):
    """API untuk menampilkan seluruh data pasien"""

    def get(self):
        """API untuk mengambil data pasien dari database"""
        
        patients = conn.execute("SELECT * FROM patient  ORDER BY pat_date DESC").fetchall()
        return patients


    def post(self):
        """API untuk menambahkan data pasien"""

        patientInput = request.get_json(force=True)
        pat_first_name=patientInput['pat_first_name']
        pat_last_name = patientInput['pat_last_name']
        pat_insurance_no = patientInput['pat_insurance_no']
        pat_ph_no = patientInput['pat_ph_no']
        pat_address = patientInput['pat_address']
        patientInput['pat_id']=conn.execute('''INSERT INTO patient(pat_first_name,pat_last_name,pat_insurance_no,pat_ph_no,pat_address)
            VALUES(?,?,?,?,?)''', (pat_first_name, pat_last_name, pat_insurance_no,pat_ph_no,pat_address)).lastrowid
        conn.commit()
        return patientInput

class Patient(Resource):
    """API yang mengatur data tunggal entitas pasien"""

    def get(self,id):
        """API untuk mengambil data pasien lewat ID"""

        patient = conn.execute("SELECT * FROM patient WHERE pat_id=?",(id,)).fetchall()
        return patient

    def delete(self,id):
        """API untuk menghapus data pasien lewat ID"""

        conn.execute("DELETE FROM patient WHERE pat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """API untuk update data pasien lewat ID"""

        patientInput = request.get_json(force=True)
        pat_first_name = patientInput['pat_first_name']
        pat_last_name = patientInput['pat_last_name']
        pat_insurance_no = patientInput['pat_insurance_no']
        pat_ph_no = patientInput['pat_ph_no']
        pat_address = patientInput['pat_address']
        conn.execute("UPDATE patient SET pat_first_name=?,pat_last_name=?,pat_insurance_no=?,pat_ph_no=?,pat_address=? WHERE pat_id=?",
                     (pat_first_name, pat_last_name, pat_insurance_no,pat_ph_no,pat_address,id))
        conn.commit()
        return patientInput