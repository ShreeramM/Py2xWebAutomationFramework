from selenium.webdriver.common.by import By


class katalonPage:
    def __init__(self, driver):
        self.driver = driver

    makeAppointment = (By.ID, "btn-make-appointment")
    username = (By.ID, "txt-username")
    password = (By.ID, "txt-password")
    login = (By.ID, "btn-login")
    appointmentmsg = (By.XPATH, "//div/h2[text()='Make Appointment']")
    toggle = (By.ID, "menu-toggle")
    logout = (By.LINK_TEXT, "Logout")

    def make_Appointment(self):
        return self.driver.find_element(*katalonPage.makeAppointment)

    def Username(self):
        return self.driver.find_element(*katalonPage.username)

    def Password(self):
        return self.driver.find_element(*katalonPage.password)

    def Login(self):
        return self.driver.find_element(*katalonPage.login)

    def Appointmentmsg(self):
        return self.driver.find_element(*katalonPage.appointmentmsg)

    def ToggleBtn(self):
        return self.driver.find_element(*katalonPage.toggle)

    def Logoutlink(self):
        return self.driver.find_element(*katalonPage.logout)

    def katalon_login(self, usr, pwd):
        self.make_Appointment().click()
        self.Username().send_keys(usr)
        self.Password().send_keys(pwd)
        self.Login().click()

    def make_appointment_msg(self):
        return self.Appointmentmsg().text

    def katalon_logout(self):
        self.ToggleBtn().click()
        self.Logoutlink().click()