from flask import render_template, redirect, url_for
from flask import request, jsonify
from app import app
from app.controller import MahasiswaController


@app.route("/mahasiswa", methods=["GET"])
def index():
    # Ambil data mahasiswa dari controller
    mahasiswa_list = MahasiswaController.index()
    # Kirim data mahasiswa ke template
    return MahasiswaController.index()


@app.route("/mahasiswa", methods=["POST"])
def store():
    # Logika untuk menyimpan data mahasiswa
    return MahasiswaController.store()


@app.route("/mahasiswa/<npm>", methods=["GET"])
def show(npm):
    # Ambil data mahasiswa berdasarkan npm
    mahasiswa = MahasiswaController.show(npm)
    return MahasiswaController.show(npm)


@app.route("/mahasiswa/<npm>", methods=["PUT"])
def update(npm):
    # Proses update data mahasiswa
    return MahasiswaController.update(npm)


@app.route("/mahasiswa/<npm>", methods=["DELETE"])
def destroy(npm):
    # Proses hapus data mahasiswa
    return MahasiswaController.destroy(npm)


# bagian tampil website
@app.route("/", methods=["GET"])
def home():

    return render_template("index.html")


@app.route("/mahasiswa/tambah", methods=["GET"])
def tambah():
    return render_template("tambah_mahasiswa.html")
