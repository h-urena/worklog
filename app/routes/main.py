from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.worklog import WorkLog
from app.models.achievement import Achievement

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Display all work log entries and achievements."""
    entries = WorkLog.query.order_by(WorkLog.id.desc()).all()
    achievements = Achievement.query.order_by(Achievement.created_at.desc()).all()
    return render_template('index.html', entries=entries, achievements=achievements)

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

@main.route('/achievements/add', methods=['GET', 'POST'])
def add_achievement():
    """Add a new achievement entry."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form.get('category', '')
        sprint = request.form.get('sprint', '')
        column = request.form.get('column', '')
        worklog_id = request.form.get('worklog_id')
        
        achievement = Achievement(
            title=title,
            description=description,
            category=category,
            sprint=sprint,
            column=column,
            worklog_id=int(worklog_id) if worklog_id and worklog_id.strip() else None
        )
        db.session.add(achievement)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    # Get all worklogs for linking
    worklogs = WorkLog.query.order_by(WorkLog.id.desc()).all()
    return render_template('add_achievement.html', worklogs=worklogs)

@main.route('/achievements/delete/<int:id>')
def delete_achievement(id):
    """Delete an achievement by ID."""
    achievement = Achievement.query.get_or_404(id)
    db.session.delete(achievement)
    db.session.commit()
    return redirect(url_for('main.index'))
