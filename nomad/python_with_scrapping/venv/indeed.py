from selenium import webdriver
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'class': 'pagination'})
    links = pagination.find_all('a')

    pages = []
    for link in links:
        pages.append(link.find('span').string)

    pages = list(map(int, pages[:-1]))
    max_page = pages[-1]
    return max_page


def extract_job(html):   # extract_indeed_jobs 함수의 result가 인자로 들어감
    title = html.find('h2', {'class': 'title'}).find('a')['title']   # a태그에서 title 속성값 가져오기
    company = html.find('span', {'class': 'company'})
    company_anchor = company.find('a')
    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string
    company = company.strip()
    # location = html.find('span', {'class':'location'}).string
    location = html.find('div', {'class':'recJobLoc'})['data-rc-loc']
    job_id = html['data-jk']
    return {'title': title, 'company': company, 'location':location, 'link':f'https://www.indeed.com/viewjob?jk={job_id}'}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping page {page}')
        result = requests.get(f'{URL}&start={page*LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})
        for result in results:
            job = extract_job(result)   # 위에서 정의한 extract_job 함수 호출
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
