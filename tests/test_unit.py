import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams, Players

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:1234@34.105.208.208/crud_app",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all() 
        test_team = Teams(team_name="team name", sponsor="Emirates")
        db.session.add(test_team)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_add_get(self):
        response = self.client.get(url_for('add', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)
        
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"team name", response.data)

class TestCreate(TestBase):
    def test_create_task(self):
        response = self.client.post(url_for("create"),
            data=dict(team_name="New team", sponsor="Emirates"),
            follow_redirects=True
        )
        self.assertIn(b"New team", response.data)

class TestUpdate(TestBase):
    def test_update_task(self):
        response = self.client.post(url_for("update", id=1),
            data=dict(team_name="Updated name", sponsor="updated sponsor"),
            follow_redirects=True
        )
        self.assertIn(b"Updated name", response.data)

class TestAdd(TestBase):
    def test_add_task(self):
        response = self.client.post(url_for("add", id=1),
            data=dict(name="add name", position='CM', club='club', height='1.77'),
            follow_redirects=True
        )
        self.assertIn(b"add name", response.data)

class TestDelete(TestBase):
    def test_update_task(self):
        response = self.client.get(url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"team name", response.data)
        self.assertNotIn(b"Emirates", response.data)