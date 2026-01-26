"""Achievement model for tracking accomplishments."""
from app import db

class Achievement(db.Model):
    """Model for an achievement/accomplishment entry."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))  # e.g., Technical, Leadership, Impact
    sprint = db.Column(db.String(50))
    column = db.Column(db.Text)  # Comments column
    worklog_id = db.Column(db.Integer, db.ForeignKey('work_log.id'), nullable=True)
    worklog = db.relationship('WorkLog', backref='achievements')
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        """String representation for debugging."""
        return f'<Achievement {self.title[:30]}>'
