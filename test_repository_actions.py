from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.main_user_page import MainUserPage
from .pages.new_repository_page import NewRepositoryPage
from .pages.repository_page import RepositoryPage
from .pages.repository_setting_page import RepositorySettingPage
from .pages.readme_page import ReadmePage
import pytest
import time



class TestUserCanCreateRepository:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://github.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        username = "VladislavTest"
        password = "SecondTestAcc123"
        login_page.authentication_user(username, password)
        self.link = browser.current_url

    def test_user_can_create_new_repository(self, browser):
        page = MainUserPage(browser, self.link)
        page.go_to_page_for_create_new_repository()
        create_new_repository_page = NewRepositoryPage(browser, browser.current_url)
        name_new_repository = "test_rep"
        create_new_repository_page.create_new_repository(name_new_repository)
        create_new_repository_page.new_repository_was_created(name_new_repository)


    def test_user_can_rename_repository(self, browser):
        page = MainUserPage(browser, self.link)
        page.go_to_repository_page()
        time.sleep(10)
        page_repository = RepositoryPage(browser, browser.current_url)
        page_repository.go_to_repository_setting()
        page_repository_setting = RepositorySettingPage(browser, browser.current_url)
        new_name_repository = "new_rep"
        page_repository_setting.rename_repository(new_name_repository)
        page_repository_setting.should_be_rename_repository(new_name_repository)

    @pytest.mark.prob_test
    def test_user_can_add_readme(self, browser):
        page = MainUserPage(browser, self.link)
        page.go_to_repository_page()
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_new_readme_page()
        readme_page = ReadmePage(browser, browser.current_url)
        readme_page.add_information_in_readme()
        readme_page.add_commit_title_for_readme_page()
        readme_page.add_commit_description_for_readme_page()
        readme_page.go_commit_new_file()
        readme_page.should_be_readme_in_list_files_in_repository()
        time.sleep(10)




    # def test_user_can_delete_repository(self, browser):
    #     pass
