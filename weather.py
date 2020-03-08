from selenium import webdriver
import datetime
from references import *




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
        #sticker reference

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
