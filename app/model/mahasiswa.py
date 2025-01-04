from app import db


class Mahasiswa(db.Model):
    __tablename__ = 'tb_mahasiswa'
    npm = db.Column(db.String(20), primary_key=True)
    nama = db.Column(db.String(230), nullable=False)
    tgl_lahir = db.Column(db.Date, nullable=False)
    alamat = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Mahasiswa %r>' % self.nama