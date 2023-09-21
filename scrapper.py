review_element = driver.find_elements_by_xpath(
    "/html/body/div[1]/div/main/div/section[4]//child::*")

def review():
    review_element = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/main/div/section[4]//child::*")
    count = 0
    reviews = []
    ratings = []
    for c in review_element:
        if c.tag_name == 'p' and c.get_attribute('class') != 'sc-1hez2tp-0 iHWhFg':
            if count > 10 and count % 6 == 0:
                print("count: ", count, " name: ", c.text)
            elif count > 10 and count % 2 == 0 and count % 6 != 0:
                reviews.append(c.text)
                print("count: ", count, " review: ", c.text)
            count += 1

        if(c.tag_name == 'div') and c.get_attribute('class') == 'sc-1q7bklc-5 kHxpSk':
            if count > 10 and count % 2 == 0:
                print("count: ", count, "  rating", c.text)
                ratings.append(c.text)

            count += 1
    for i in range(len(reviews)):
        if (reviews[i] != '' and ratings[i] != ''):
            k = [reviews[i], ratings[i]]
            data.append(k)

for c in review_element:
    try:
        if c.tag_name == 'a':

            if c.text.isnumeric():
                element = driver.find_element_by_link_text(c.text)
                element.click()
                time.sleep(3)
                review()
            else:
                print("no anchor tag")
    except:
        pass
print("endd")
