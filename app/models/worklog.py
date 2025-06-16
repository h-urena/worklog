from app import db

class WorkLog(db.Model):
    """Model for a work log entry."""
    id = db.Column(db.Integer, primary_key=True)
    pbi_number = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sprint = db.Column(db.String(50), nullable=False)
    effort = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)

    def __repr__(self):
        """String representation for debugging."""
        return f'<WorkLog {self.pbi_number} - {self.description[:20]}>'
