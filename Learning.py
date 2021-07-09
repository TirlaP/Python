from bs4 import BeautifulSoup


# Scraping simple website built by us

with open('home.html', 'r') as html_file:
    # read the content from the site as text
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'logo')
    for course in course_cards:
        course_name = course.h4.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')




















