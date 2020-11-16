# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import allure


def handle_black(func):
    def wrapper(*args, **kwargs):
        from UI.fram2.bass_page import BassPage
        instance: BassPage = args[0]
        try:
            result = func(*args, **kwargs)
            instance._error_num = 0
            return result
        except Exception as e:
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num += 1
            for black_ele in instance.black_list:
                print(black_ele)
                print("查找黑名单元素")
                print(*black_ele)
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    print("点击操作")
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
