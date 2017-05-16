import requests


def test_request():
    def request(url):
        try:
            response = requests.get(url)

            return response.status_code
        except Exception:
            return -1

    result = request("http://www.avgthreatlabs.com/ww-en/website-safety-reports/domain/google.com")

    assert result == 200
