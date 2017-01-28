#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import peyconfig as cfg
from sys import argv, exit
from utils import usage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os.path import abspath 
import work

def scroll_to(driver, element):
    scroll = """
        function move_up(element) {
            element.scrollTop = element.scrollTop - 1000;
        }

        function move_down(element) {
            element.scrollTop = element.scrollTop + 1000;
        }

        move_down(arguments[0]);
        move_down(arguments[0]);
        """
    driver.execute_script(scroll, element)
    sleep(2)


def create_package(driver, company):
    driver.find_element_by_id('name').send_keys(company)
    cover = driver.find_element_by_css_selector(
            "input[type='radio'][name='11']")
    resume = driver.find_element_by_css_selector(
            "input[type='radio'][name='12']")
    transcript = driver.find_element_by_css_selector(
            "input[type='radio'][name='13']")

    cover.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    resume.click()
    transcript.click()
    # wait for new div to show up
    sleep(1)
    driver.find_element_by_css_selector(
            "input[type='submit'][value='Create Package']").click()


def upload_cover_letter(driver, path, job_id, company):
    driver.execute_script("orbisApp.buildForm({action:'displayDocUpload',postingId:%s}).submit();" % job_id)
    driver.execute_script(
            "document.getElementsByName('docType')[0].value = '11';")
    driver.find_element_by_name('docName').send_keys(company + ' cover')
    driver.find_element_by_name('docUploaded').send_keys(abspath(path))
    driver.execute_script("$('#fileUploadForm').submit();")


def make_cover_letter(company_name, job_title, team):
    return work.main([company_name, job_title, team])


def application_page(driver):
    driver.find_element_by_id('applyButton').click()


def find_posting(driver, job_id):
    job_id_input = driver.find_element_by_name('postingId')
    job_id_input.send_keys(job_id)
    job_id_input.send_keys(Keys.RETURN)


def login(driver):
    driver.get('https://www.uoftengcareerportal.ca/students/login.htm')

    # get the username and password input elements
    username_input = driver.find_element_by_id('j_username')
    password_input = driver.find_element_by_id('j_password')

    # make sure everything is clear
    username_input.clear()
    password_input.clear()

    # send the username and password
    username_input.send_keys(cfg.username)
    password_input.send_keys(cfg.password)
    password_input.send_keys(Keys.RETURN)


def open_internships(driver):
    # driver should be logged in.
    driver.find_element_by_css_selector("a[href*='#searchPostings']").click()
    driver.find_element_by_css_selector(
            "a[href*='/myAccount/internship/postings.htm']").click()


def main(args):
    if len(args) < 3:
        usage()
        exit(1)

    job_id = args[0]
    company = args[1]
    title = args[2]
    team = "Engineering"
    if len(args) == 4:
        team = args[3]

    driver = webdriver.Chrome()
    driver.maximize_window()
    login(driver)
    open_internships(driver)
    find_posting(driver, job_id)
    application_page(driver)
    cover_letter_path = make_cover_letter(company, title, team)
    upload_cover_letter(driver, cover_letter_path, job_id, company)
    create_package(driver, company)
    # u have to post urself
    sleep(10)
    driver.quit()


if __name__ == "__main__":
    main(argv[1:])
