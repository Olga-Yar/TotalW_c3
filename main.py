from utils.func import get_data, get_filtered, get_formatted, get_last_date


def main():
    OPERATIONS_URL = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677520657447&signature=_SXeoiqueQ2WvOCYn-JcGB_ueSslK2gYgg5PQ52Chx0&downloadName=operations.json'
    COUNT_LAST = 5
    FILTERED_EMPTY_FROM = True

    data = get_data(OPERATIONS_URL)
    if not data:
        exit('Error')

    data = get_filtered(data, FILTERED_EMPTY_FROM)
    data = get_last_date(data, COUNT_LAST)
    data = get_formatted(data)
    for i in data:
        print(i)


if __name__ == '__main__':
    main()

