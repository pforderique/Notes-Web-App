from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

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