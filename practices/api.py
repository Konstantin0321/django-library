import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class ApiError(Exception):
    pass


def get_json(url):
    request = Request(url, headers={"User-Agent": "django-library-practices/1.0"})
    try:
        with urlopen(request, timeout=8) as response:
            return json.load(response)
    except HTTPError as error:
        if error.code == 404:
            raise ApiError("Запись не найдена.") from error
        raise ApiError(f"Сервис вернул HTTP {error.code}.") from error
    except (URLError, TimeoutError, ValueError) as error:
        raise ApiError("Не удалось получить данные от сервиса.") from error
