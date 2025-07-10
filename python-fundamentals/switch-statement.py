http_status = 550

if http_status == 200 or http_status == 201:
    print('Success! The request was successful.')
elif http_status == 400:
    print('Bad Request!')
elif http_status == 404:
    print('Not Found!')
elif http_status == 500 or http_status == 501:
    print('Server Error!')
else:
    print('Unknown Error!')

match http_status:
    case 200 | 201:
         print('Success!')
    case 400:
         print('Bad Request!')
    case 404:
         print('Not Found!')
    case 500 | 501:
        print('Server Error!')
    case _:
        print('Unknown Error!')