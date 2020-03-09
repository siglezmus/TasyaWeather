from pathlib import Path

from selenium import webdriver
import datetime
from references import *
from pathlib import Path

driver_loc = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#driver_loc = str(Path.absolute(__file__).parent) + "chrome.exe"

class Weather:

    def __init__(self):
        self.driver = webdriver.Chrome(driver_loc)
        self.driver.get(driver_search_query)
        self.time = self.get_time(self.driver)
        self.humidity = self.get_humidity(self.driver)  #Влажность
        self.precipitation = self.get_precipitation(self.driver)    #Осадки
        self.location = self.get_location(self.driver)
        self.description = self.get_description(self.driver)
        self.current_temperature = self.get_current_temperature(self.driver)
        self.upper_temperature = self.get_upper_temperature(self.driver)
        self.lower_temperature = self.get_lower_temperature(self.driver)
        self.last_weather_request = datetime.datetime.now()
        self.driver.close()
        #self.print_all()
        self.sticker_reference = self.get_sticker(self.description)

    def get_sticker(self, description):

        if (description in list1):
            return ref1
        elif(description in list2):
            return ref2
        elif (description in list3):
            return ref3
        elif (description in list4):
            return ref4
        elif (description in list5):
            return ref5
        elif (description in list6):
            return ref6
        elif (description in list7):
            return ref7
        elif (description in list8):
            return ref8
        elif (description in list9):
            return ref9
        elif (description in list10):
            return ref10
        elif (description in list11):
            return ref11
        elif (description in list12):
            return ref12
        elif (description in list13):
            return ref13
        elif (description in list14):
            return ref14
        else:
            return err_ref

    def get_current_temperature(self, driver):
        return driver.find_elements_by_xpath(current_temperature_xpath)[0].text
    def get_location(self, driver):
        return driver.find_element_by_id(location_id1).find_element_by_id(location_id2).text
    def get_description(self, driver):
        return driver.find_elements_by_xpath(description_xpath)[0].text
    def get_time(self, driver):
        return driver.find_element_by_id(time_id1).find_element_by_id(time_id2).find_element_by_id(time_id3).text
    def get_precipitation(self, driver):
        return driver.find_elements_by_xpath(precipitation_xpath)[0].text
    def get_humidity(self, driver):
        return driver.find_elements_by_xpath(humidity_xpath)[0].text
    def get_upper_temperature(self, driver):
        return driver.find_element_by_id(upper_lower_id1).find_element_by_id(upper_lower_id2).find_element_by_class_name(upper_class).find_element_by_class_name(upper_lower_final_class).text
    def get_lower_temperature(self, driver):
        return driver.find_element_by_id(upper_lower_id1).find_element_by_id(upper_lower_id2).find_elements_by_class_name(lower_class)[1].find_element_by_class_name(upper_lower_final_class).text




    def print_all(self):
        print(self.current_temperature + "\n")
        print(self.humidity + "\n")
        print(self.time + "\n")
        print(self.location + "\n")
        print(self.upper_temperature)
        print(self.lower_temperature)
        print(self.precipitation + "\n")
        print(self.description + "\n")

    def update(self):
        self.driver = webdriver.Chrome(driver_loc)
        self.driver.get(driver_search_query)
        self.time = self.get_time(self.driver)
        self.humidity = self.get_humidity(self.driver)  # Влажность
        self.precipitation = self.get_precipitation(self.driver)  # Осадки
        self.location = self.get_location(self.driver)
        self.description = self.get_description(self.driver)
        self.current_temperature = self.get_current_temperature(self.driver)
        self.upper_temperature = self.get_upper_temperature(self.driver)
        self.lower_temperature = self.get_lower_temperature(self.driver)
        self.last_weather_request = datetime.datetime.now()
        self.driver.close()
        # sticker reference
