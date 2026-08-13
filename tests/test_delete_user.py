import requests


def test_delete_user(user_api_client):

    response = user_api_client.delete("/users/1")

    assert response.status_code == 200


    # DELETE 通常不應該有內容
    print(response.text)