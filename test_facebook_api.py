for i in range(0, len(others_content_visible)):
    others_content.append(others_content_visible[i].a.get_text())
    print(others_content)

print(others_title + " " + others_content)

t = 1
for i in range(0, 10):
    for x in range(0, len(soup2)):
        arq.write("%d- %s \n" %
                  (t, soup2[x].a.get_text().encode(encoding='UTF-8', errors='strict')))
        names.append("%s" % (soup2[x].a.get_text().encode(
            encoding='UTF-8', errors='strict')))
        t = t+1
    URL = ("https://www.imdb.com/search/title?title_type=movie&genres=action&start={}&explore=title_type,genres&ref_=adv_nxt".format(t))
    response = get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup2 = soup.find_all("div", {"class": "lister-item-content"})

arq.close

test_df = pd.DataFrame({'movie': names})
print(test_df.info())
test_df


def main():
    token = "EAAkZCSBZApuk4BAKbK6QD59NZBA1bOUHQ6ZC3WjRAslivLtaZCgXhp4Jv8l5wg6lGWczazj8BFJC2b3fB5L68ZACT8DEYMl4RcSZANQ8ZCEyQ5c5AcRZAqfWDiA1AratfuMZCbRjIGQNORGAHnDMSV8vo6ocUCS2DfisWOzcxS78M2K4mEeMfjGHNACvQnanbqz00ZD"
    graph = facebook.GraphAPI(token)
    # fields = ['first_name', 'location{location}','email','link']
    id = 'cicero.henrique.92754'
    profile = graph.get_object(
        'me', fields='birthday,gender,hometown,location,name,favorite_athletes')

    all_fields = ['user_birthday', 'hometown', 'location', 'likes', 'photos',
                  'videos', 'friends', 'status', 'tagged_places', 'posts', 'gender', 'link',
                  'age_range', 'email', 'instagram_basic', 'public_profile']

    # post = graph.get_object(id='414573129108005', fields='message')
    # print(post['message'])

    # friends = graph.get_connections(id='me', connection_name='friends')
    # print(friends)
    # print(friends['data'])
    # return desired fields
    print(json.dumps(profile, indent=4))


if __name__ == '__main__':
    main()
