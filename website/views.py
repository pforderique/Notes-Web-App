from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, GlobalNote
from . import db, MAX_GLOBAL_NOTES
import json

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"]) # root page
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')
        
        if len(note) < 1: 
            flash('Note too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Noted Added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/global', methods=["GET", "POST"])
def globalNotes():
    # if something was posted to global, then user had to be signed in
    if request.method == "POST":
        globalnote = request.form.get('globalnote')

        if len(globalnote) < 1: 
            flash('Note too short!', category='error')
        else:
            new_gnote = GlobalNote(data=globalnote, user_id=current_user.id)
            db.session.add(new_gnote)
            db.session.commit()
            flash('Global Note Added!', category='success')

    # Nonetheless, get a list of global notes to show any user
    globalnotes = GlobalNote.query.order_by(GlobalNote.date.desc()).limit(MAX_GLOBAL_NOTES).all()

    return render_template("global.html", gnotes=globalnotes, user=current_user)

@views.route('/delete-note', methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    # basically, query the note and delete it
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})