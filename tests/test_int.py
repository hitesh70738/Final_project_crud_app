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
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        app.config['SECRET_KEY'] = "asd"
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

class TestAddPlayer1(TestCreateTeam):
    def add_player(self):
        self.driver.find_element_by_xpath('/html/body/form[3]/input').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Thomas')
        self.driver.find_element_by_xpath('//*[@id="position"]').send_keys('CM')
        self.driver.find_element_by_xpath('//*[@id="club"]').send_keys('Watford FC')
        self.driver.find_element_by_xpath('//*[@id="height"]').send_keys('1.2')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('add') in self.driver.current_url
        assert Players.query.filter_by(id=1).first().name == 'Thomas'
        assert Players.query.filter_by(id=1).first().position == 'CM'
        assert Players.query.filter_by(id=1).first().position == 'Watford FC'
        assert Players.query.filter_by(id=1).first().position == '1.2'

class TestAddPlayer2(TestCreateTeam):
    def add_player(self):
        self.driver.find_element_by_xpath('/html/body/form[3]/input').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Partey')
        self.driver.find_element_by_xpath('//*[@id="position"]').send_keys('CB')
        self.driver.find_element_by_xpath('//*[@id="club"]').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="height"]').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('add') in self.driver.current_url
        assert Players.query.filter_by(id=1).first().name == 'Partey'
        assert Players.query.filter_by(id=1).first().position == 'CB'
        assert Players.query.filter_by(id=1).first().position == ''
        assert Players.query.filter_by(id=1).first().position == ''

class TestAddPlayer3(TestCreateTeam):
    def add_player(self):
        self.driver.find_element_by_xpath('/html/body/form[3]/input').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Bale')
        self.driver.find_element_by_xpath('//*[@id="position"]').send_keys('LW')
        self.driver.find_element_by_xpath('//*[@id="club"]').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="height"]').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('add') in self.driver.current_url
        assert Players.query.filter_by(id=1).first().name == 'Bale'
        assert Players.query.filter_by(id=1).first().position == 'LW'
        assert Players.query.filter_by(id=1).first().position == ''
        assert Players.query.filter_by(id=1).first().position == ''

class TestAddPlayer4(TestCreateTeam):
    def add_player(self):
        self.driver.find_element_by_xpath('/html/body/form[3]/input').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Messi')
        self.driver.find_element_by_xpath('//*[@id="position"]').send_keys('RW')
        self.driver.find_element_by_xpath('//*[@id="club"]').send_keys('Barca')
        self.driver.find_element_by_xpath('//*[@id="height"]').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('add') in self.driver.current_url
        assert Players.query.filter_by(id=1).first().name == 'Messi'
        assert Players.query.filter_by(id=1).first().position == 'RW'
        assert Players.query.filter_by(id=1).first().position == 'Barca'
        assert Players.query.filter_by(id=1).first().position == ''

class TestUpdateTeam(TestCreateTeam):

    def create_team(self):
        self.driver.find_element_by_xpath("/html/body/a[1]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="team_name"]').send_keys('New team')
        self.driver.find_element_by_xpath('//*[@id="sponsor"]').send_keys('New sponsor')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        
        assert url_for('home') in self.driver.current_url

class TestDeleteTeam(TestCreateTeam):

    def create_team(self):
        self.driver.find_element_by_xpath("/html/body/form[2]/input").click()
        time.sleep(1)
        
        assert url_for('delete') in self.driver.current_url




if __name__ == '__main__':
    unittesting.main(port=5000)