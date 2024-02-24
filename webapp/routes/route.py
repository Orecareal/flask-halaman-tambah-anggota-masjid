from flask import render_template, jsonify, request
from webapp import app, db
from webapp.models.model import Anggota

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/anggota', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        data = request.form.to_dict()
        new_data = Anggota(
            nama=data['nama'], 
            jenkel=data['jenkel'],
            jabatan=data['jabatan'],
            alamat=data['alamat'],
            no_hp=data['no_hp']
            )
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'User created successfully', 'new_data':data})
    anggota = Anggota.query.all()
    user_data = [{
        'id': user.id, 
        'nama': user.nama, 
        'jenkel': user.jenkel,
        'jabatan': user.jabatan,
        'alamat': user.alamat,
        'no_hp': user.no_hp,
        } for user in anggota
    ]
    return jsonify({'data': user_data})
    

@app.route('/anggota/<int:user_id>', methods=['PUT', 'DELETE'])
def manage_user(user_id):
    anggota = Anggota.query.get_or_404(user_id)
    if request.method == 'PUT':
        data = request.form.to_dict()
        anggota.nama=data['nama'], 
        anggota.jenkel=data['jenkel'],
        anggota.jabatan=data['jabatan'],
        anggota.alamat=data['alamat'],
        anggota.no_hp=data['no_hp']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})

    if request.method == 'DELETE':
        db.session.delete(anggota)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})