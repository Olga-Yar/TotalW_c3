from utils.func import get_data, get_filtered, get_last_date, get_formatted


def test_get_data():
    url = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677520657447&signature=_SXeoiqueQ2WvOCYn-JcGB_ueSslK2gYgg5PQ52Chx0&downloadName=operations.json'
    assert get_data(url) is not None


def test_get_filtered(test_data):
    assert len(get_filtered(test_data)) == 4
    assert len(get_filtered(test_data, filtered_empty_from=True)) == 2


def test_get_last_date(test_data):
    data = get_last_date(test_data, count_lasts=2)
    assert data[0]['date'] == '2021-04-04T23:20:05.206878'
    assert len(data) == 2


def test_get_formatted(test_data):
    data = get_formatted(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nДанные скрыты  -> **Счет\n31957.58 руб.\n']
    data = get_formatted(test_data[1:2])
    assert data == ['03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> **Счет\n8221.37 USD\n']



