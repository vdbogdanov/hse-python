import base64, requests


def virustotal_sendfile(api_key, file_path, file_password):
    """
    Отправка файла на сканирование в virustotal
    """
    url = "https://www.virustotal.com/api/v3/files"
    files = {
        "file": (file_path.split("/")[-1], open(file_path, "rb"), "application/zip")
    }
    headers = {"accept": "application/json", "x-apikey": api_key}

    if file_password:
        payload = {"password": file_password}
        response = requests.post(url, data=payload, files=files, headers=headers)
    else:
        response = requests.post(url, files=files, headers=headers)

    if response.status_code == 200:
        print("\nФайл успешно отправлен на сканирование!")
        file_id = response.json()["data"]["id"]
        file_id_decoded = base64.b64decode(file_id).decode("utf-8").split(":")[0]
        return file_id_decoded
    else:
        print("\nОшибка при отправке файла:", response.status_code)
        print("\nТекст ошибки:", response.text)
        return 0


def virustotal_analyzer(api_key, file_id):
    """
    Получение отчетка о сканировании файла из virustotal
    """
    url = f"https://www.virustotal.com/api/v3/files/{file_id}"
    headers = {"accept": "application/json", "x-apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("\nФайл успешно сканирован!")
        return response.json()
    else:
        print("\nОшибка при сканировании файла:", response.status_code)
        return 0
