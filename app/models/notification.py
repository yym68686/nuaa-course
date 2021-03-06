#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKeyConstraint
from datetime import datetime
from app import db, login_manager as lm
from random import randint
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, \
     check_password_hash
from flask_babel import gettext as _

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    to_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    from_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow().date())
    time = db.Column(db.DateTime, default=datetime.utcnow())
    operation = db.Column(db.String(50), nullable=False)
    ref_class = db.Column(db.String(50))
    ref_obj_id = db.Column(db.Integer)
    ref_display_class = db.Column(db.String(50))
    display_text = db.Column(db.Text)

    to_user = db.relationship('User', foreign_keys=to_user_id, backref=db.backref('notifications', order_by='desc(Notification.id)'))
    from_user = db.relationship('User', foreign_keys=from_user_id)

    def __init__(self, to_user, from_user, operation, ref_obj, ref_display_class=None):
        self.to_user = to_user
        self.from_user = from_user
        self.date = datetime.utcnow().date()
        self.time = datetime.utcnow()
        self.operation = operation
        self.ref_class = ref_obj.__class__.__name__
        self.ref_display_class = ref_display_class or self.ref_class
        self.ref_obj_id = ref_obj.id

    def save(self):
        self.display_text = self.__display_text
        db.session.add(self)
        db.session.commit()

    @property
    def ref_obj(self):
        from .review import Review, ReviewComment
        from .course import Course
        from .user import User, Teacher
        if self.ref_class == 'Review':
            return Review.query.get(self.ref_obj_id)
        elif self.ref_class == 'ReviewComment':
            return ReviewComment.query.get(self.ref_obj_id)
        elif self.ref_class == 'Course':
            return Course.query.get(self.ref_obj_id)
        elif self.ref_class == 'User':
            return User.query.get(self.ref_obj_id)
        elif self.ref_class == 'Teacher':
            return Teacher.query.get(self.ref_obj_id)
        else:
            return None

    @property
    def class_name(self):
        class_names = {
            'Review': '??????',
            'ReviewComment': '??????',
            'Course': '??????',
            'User': '??????',
            'Teacher': '??????',
        }
        if self.ref_class in class_names:
            return class_names[self.ref_class]
        else:
            return 'doge'

    @property
    def ref_obj_name(self):
        if self.ref_display_class == 'Review':
            return '?????????' + self.ref_obj.link + '?????? ' + self.ref_obj.author.link + ' ?????????'
        elif self.ref_display_class == 'ReviewComment':
            return '?????????' + self.ref_obj.review.link + '?????? ' + self.ref_obj.review.author.link + ' ???????????? ' + self.ref_obj.author.link + ' ?????????'
        elif self.ref_display_class == 'Course':
            return '?????????' + self.ref_obj.link + '???'
        elif self.ref_display_class == 'User':
            if self.ref_obj == current_user:
                return '???'
            else:
                return '?????????' + self.ref_obj.link + '???'
        elif self.ref_display_class == 'Teacher':
            return '?????????' + self.ref_obj.link + '???'
        else:
            return 'doge'

    @property
    def operation_text(self):
        if self.operation == 'mention':
            return '???' + self.ref_obj_name + '???????????????'
        elif self.operation == 'upvote':
            return '???' + self.ref_obj_name + '????????????'
        elif self.operation == 'downvote':
            return '???' + self.ref_obj_name + '???????????????'
        elif self.operation == 'comment':
            return '?????????' + self.ref_obj_name
        elif self.operation == 'review':
            return '?????????' + self.ref_obj_name
        elif self.operation == 'follow':
            return '?????????' + self.ref_obj_name
        else:
            return 'doge'

    @property
    def __display_text(self):
        try:
            return self.from_user.link + ' ' + self.operation_text
        except:
            return ""

    @property
    def url(self):
        return self.ref_obj.url

    @property
    def link(self):
        return self.ref_obj.link
