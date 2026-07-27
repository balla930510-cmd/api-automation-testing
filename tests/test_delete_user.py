import requests


def test_delete_user():

    url = "https://jsonplaceholder.typicode.com/users/1"


    response = requests.delete(url)


    # 驗證 HTTP Status Code
    assert response.status_code == 200


    # DELETE 通常不應該有內容
    print(response.text)