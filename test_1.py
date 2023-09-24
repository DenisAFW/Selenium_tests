import yaml
import time
from module import Site

with open('testdata.yaml') as f:
    data = yaml.safe_load(f)

site = Site(data["address"])


def test_step1(x_selector1, x_selector2, btn_selector, err_selector, correct_res):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(data["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(data["passwd"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", err_selector).text
    assert err_label == correct_res, "Test 1 FAIL"


def test_step2(x_selector1, x_selector2, btn_selector, x_selector3, result):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(data["user"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(data["user_pass"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    profile = site.find_element("xpath", x_selector3).text
    assert profile == result, "Test 2 FAIL"


def test_step3(create_post, title, description, content, save_button, title_post, check_2):
    plus = site.find_element("xpath", create_post)
    plus.click()
    time.sleep(1)
    input1 = site.find_element("xpath", title)
    input1.send_keys("For Emperor!")
    input2 = site.find_element("xpath", description)
    input2.send_keys("Glory to the Emperor!")
    input3 = site.find_element("xpath", content)
    input3.send_keys("My God is the Emperor!")
    save = site.find_element("xpath", save_button)
    save.click()
    time.sleep(1)
    result = site.find_element("xpath", title_post).text
    assert result == check_2, "Test 2 FAIL"


def test_step4(del_post, check_posts, check_2):
    """
    Тест 4 удаляет созданный пост после всех проверок для повторного запуска данных тестов.
    """
    delete_btn = site.find_element("xpath", del_post)
    delete_btn.click()
    posts = site.find_element("xpath", check_posts).text
    assert posts != check_2, "test 4 FAIL"

# css_selector = data["login_size_css"]
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath = data['button_xpath']
# print(site.get_element_property("xpath", xpath, "color"))
