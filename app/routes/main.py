from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.worklog import WorkLog

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Display all work log entries."""
    entries = WorkLog.query.order_by(WorkLog.id.desc()).all()
    return render_template('index.html', entries=entries)

@main.route('/add', methods=['GET', 'POST'])
def add_entry():
    """Add a new work log entry."""
    if request.method == 'POST':
        pbi_number = request.form['pbi_number']
        description = request.form['description']
        sprint = request.form['sprint']
        effort = request.form['effort']
        comments = request.form['comments']
        entry = WorkLog(
            pbi_number=pbi_number,
            description=description,
            sprint=sprint,
            effort=effort,
            comments=comments
        )
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_entry.html')

@main.route('/delete/<int:id>')
def delete_entry(id):
    """Delete a work log entry by ID."""
    entry = WorkLog.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('main.index'))
