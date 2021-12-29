from app import db

association = db.Table('association',
                       db.Column('author_id', db.Integer, db.ForeignKey('author.author_id')),
                       db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'))
                       )

rent = db.Table('rent',
                db.Column('book_id', db.Integer, db.ForeignKey('book.book_id')),
                db.Column('rental_id', db.Integer, db.ForeignKey('rental.rental_id'))
                )


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    books = db.relationship('Book', secondary=association, backref=db.backref('books'), lazy='dynamic')

    def __str__(self):
        return f"<User {self.name}>"


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    rental = db.relationship('Rental', secondary=rent, backref=db.backref('rent'), lazy='dynamic')

    def __str__(self):
        return f"<User {self.title}>"


class Rental(db.Model):
    rental_id = db.Column(db.Integer, primary_key=True)
    rented = db.Column(db.String(20))

    def __str__(self):
        return f"<User {self.rented}>"