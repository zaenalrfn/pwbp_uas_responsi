from app.model.mahasiswa import Mahasiswa
from app import response
from flask import request, jsonify, redirect
from app import db


def index():
    try:
        mahasiswa_list = Mahasiswa.query.all()
        data = transform(mahasiswa_list)
        return response.ok(data, "Data mahasiswa berhasil diambil.")
    except Exception as e:
        print(e)
        return response.bad_request(
            message="Gagal mengambil data mahasiswa. Terjadi kesalahan pada server."
        )


def store():
    try:
        npm = request.json["npm"]
        nama = request.json["nama"]
        tgl_lahir = request.json["tgl_lahir"]
        alamat = request.json["alamat"]

        mahasiswa = Mahasiswa(npm=npm, nama=nama, tgl_lahir=tgl_lahir, alamat=alamat)

        db.session.add(mahasiswa)
        db.session.commit()

        return response.ok("", "Mahasiswa Berhasil ditambahkan!")

    except Exception as e:
        print(e)
        return jsonify({"message": "Terjadi kesalahan saat membuat mahaiswa!"}), 500


def transform(mahasiswa_list):
    array = []
    for m in mahasiswa_list:
        array.append(
            {
                "npm": m.npm,
                "nama": m.nama,
                "tgl_lahir": m.tgl_lahir,
                "alamat": m.alamat,
                "created_at": m.created_at,
                "updated_at": m.updated_at,
            }
        )
    return array


def update(npm):
    try:
        nama = request.json["nama"]
        tgl_lahir = request.json["tgl_lahir"]
        alamat = request.json["alamat"]

        mahasiswa = Mahasiswa.query.filter_by(npm=npm).first()

        if mahasiswa:
            mahasiswa.nama = nama
            mahasiswa.tgl_lahir = tgl_lahir
            mahasiswa.alamat = alamat

            db.session.commit()

            return response.ok("", "Berhasil update mahasiswa!")
        else:
            return response.error("Mahasiswa tidak ada", 404)

    except Exception as e:
        print(e)
        return response.error("Terjadi kesalahan saat update mahasiswa", 500)


def singleTransform(mahasiswa):
    data = {
        "npm": mahasiswa.npm,
        "nama": mahasiswa.nama,
        "tgl_lahir": mahasiswa.tgl_lahir,
        "alamat": mahasiswa.alamat,
        "created_at": mahasiswa.created_at,
        "updated_at": mahasiswa.updated_at,
    }
    return data


def show(npm):
    try:
        mahasiswa = Mahasiswa.query.filter_by(npm=npm).first()

        if not mahasiswa:
            return response.badRequest([], "Mahasiswa tidak ada")

        data = singleTransform(mahasiswa)
        return response.ok(data, "Mahasiswa berhasil diambil.")

    except Exception as e:
        print(f"An error occurred: {e}")
        return response.badRequest(
            [], "Terjadi kesalahan saat mengambil data mahasiswa."
        )


def destroy(npm):
    try:
        mahasiswa = Mahasiswa.query.filter_by(npm=npm).first()

        if not mahasiswa:
            return response.badRequest([], "Mahasiswa tidak ada.")

        db.session.delete(mahasiswa)
        db.session.commit()

        return response.ok("", "Mahasiswa berhasil dihapus.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return response.badRequest(
            [], "Terjadi kesalahan saat menghapus data mahasiswa."
        )


# bagian website
def web_store(npm, nama, tgl_lahir, alamat):
    try:
        # Membuat objek Mahasiswa
        mahasiswa = Mahasiswa(npm=npm, nama=nama, tgl_lahir=tgl_lahir, alamat=alamat)

        # Menambahkan mahasiswa ke dalam database
        db.session.add(mahasiswa)
        db.session.commit()
        response.ok("", "Berhasil menambahkan mahasiswa.")
        return redirect("/")
    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred while creating mahasiswa!"}), 500
