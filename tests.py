from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='user')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_follow(self):
        u1 = User(username='john', email='john@mail.ru')
        u2 = User(username='john2', email='john2@mail.ru')

        db.session.add(u1)
        db.session.add(u2)

        db.session.commit()

        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()

        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'john2')

    def test_follow_posts(self):
        u1 = User(username='test1', email='test1@mail.ru')
        u2 = User(username='test2', email='test2@mail.ru')
        u3 = User(username='test3', email='test3@mail.ru')
        u4 = User(username='test4', email='test4@mail.ru')
        db.session.add_all([u1, u2, u3, u4])

        now = datetime.utcnow()
        p1 = Post(body='post from test1', author=u1,
                        timestamp=now + timedelta(seconds=1))
        p2 = Post(body='post from test2', author=u2,
                        timestamp=now + timedelta(seconds=2))
        p3 = Post(body='post from test3', author=u3,
                        timestamp=now + timedelta(seconds=4))
        p4 = Post(body='post from test4', author=u4,
                        timestamp=now + timedelta(seconds=6))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        followed_posts_u1 = u1.followed_posts().all()
        followed_posts_u2 = u2.followed_posts().all()
        followed_posts_u3 = u3.followed_posts().all()
        followed_posts_u4 = u4.followed_posts().all()

        self.assertEqual(followed_posts_u1, [p4, p2, p1])
        self.assertEqual(followed_posts_u2, [p3, p2])
        self.assertEqual(followed_posts_u3, [p4, p3])
        self.assertEqual(followed_posts_u4, [p4])
        
if __name__ == '__main__':
    unittest.main(verbosity=2)