from webapp import db

class Anggota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    jenkel = db.Column(db.String(100), nullable=False)
    jabatan = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    no_hp = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"'{self.nama}','{self.jenkel}','{self.jabatan}','{self.alamat}','{self.no_hp}'"
    

db.create_all()