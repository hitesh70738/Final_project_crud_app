import unittest
import time
from flask import url_for
from urllib.request import urlopen

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Teams, Players

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@34.105.208.208/crud_app"
        app.config['SECRET_KEY'] = "asdasda"
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/hites/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestCreateTeam(TestBase):

    def create_team(self):
        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="team_name"]').send_keys('Arsenal')
        self.driver.find_element_by_xpath('//*[@id="sponsor"]').send_keys('Emirates')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('home') in self.driver.current_url
        assert Teams.query.filter_by(id=1).first().team_name == 'Arsenal'
        assert Teams.query.filter_by(id=1).first().sponsor == 'Emirates'

class TestAddPlayer(TestCreateTeam):
    def add_player(self):
        self.driver.find_element_by_xpath('/html/body/form[3]/input').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Thomas Partey')
        self.driver.find_element_by_xpath('//*[@id="position"]').send_keys('CDM')
        self.driver.find_element_by_xpath('//*[@id="club"]').send_keys('Arsenal FC')
        self.driver.find_element_by_xpath('//*[@id="height"]').send_keys('1.8')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('add') in self.driver.current_url
        assert Players.query.filter_by(id=1).first().name == 'Thomas Partey'
        assert Players.query.filter_by(id=1).first().position == 'CDM'
        assert Players.query.filter_by(id=1).first().position == 'Arsenal FC'
        assert Players.query.filter_by(id=1).first().position == '1.8'

class TestDeleteTeam(TestCreateTeam):

    def create_team(self):
        self.driver.find_element_by_xpath("/html/body/form[2]/input").click()
        time.sleep(1)
        
        assert url_for('delete') in self.driver.current_url




if __name__ == '__main__':
    unittesting.main(port=5000)