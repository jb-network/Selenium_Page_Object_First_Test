from selenium import webdriver

class TrainingGroundPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inpt = self.driver.find_element('id', 'ipt1')
        inpt.clear()
        inpt.send_keys(text)
        return None

    def get_input_text(self):
        inpt = self.driver.find_element('id', 'ipt1')
        elem_text = inpt.get_attribute('value')
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element('id', 'b1')
        button.click()
        return None

# My Test
browser = webdriver.Chrome()

# Test Setup
test_value = "it worked"

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input(test_value)
# Course did not address alert box that occurs from the button click below.
# if the line is uncommented then the next two lines must be commented out.
# I wanted to leave this, to address it in the future
# trng_page.click_button_1()
txt_from_input = trng_page.get_input_text()
assert txt_from_input == test_value, f"Test Failed: Input did not match: {test_value}"
print("Test passed")
