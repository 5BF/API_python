import  re









pwdOne = 'GIsPp%2Btfp8WoMX40pkIRceEXnACxi34IU3x9RkZZjnOdBHHr0hRREdZvQXMgpXrQ%2F' \
         'CQf8nOTEgC98sgeMRAFK%2Fvq9fCy1cMboC1%2FpLbmISYAtV6%2FG%2FPsviJ3oW5mQ9' \
         '73eUqHZ%2B%2ByTIQZT%2FiFzWR7w0DBBHz%2BAicglyL2e5NcGYwfB3mHsTWtq3%2F8Z' \
         'PcVmWRHDXFULN6lczFjGsRzt%2BwcrwGU2E6ZO6fs%2F3LhagUKRNWs7Tt0HS0KQRJ9M77' \
         '4dHJ7xEhnp0N9D7PZyRtbuJN1SYpbuzcngmGYWygkIhxGfzn61TMZkC5bk5o9GM32oV4v' \
         '2WZLNNCegC1Yz7yxEiDJPQ%3D%3D'



pwdTwo='fgRbnc6hfnutOtT6soub3aSNGLOJCMHbiYsPR7mZZXoH0UkMFzzJ0P6EXH1ssxw9w%2Fee' \
         'J%2Bvmriv%2FKpK2Hm%2BGJphqnU5zNdytePgRoDhnbxc31brPDqT0Tm3JC67Jk7aA%2Bl' \
         '0s288nEEfDt5OCtbjEeEz2ebbCodv9x%2BOjYmBdWPZBAEt75AFHbLIQYoWKQIt5K%2BpO' \
         'reVlLj%2F7qW0lgMQsjfmDOws%2F9N5va%2Bpd2%2B83c4nxv4TxXbkDyEKveeHMTnPihH' \
         '2uPKejGk6jKuoXHT2S9YEudd6dHs%2BFZuCFeEoBryuPxRkuj4sz4OcUWDfYQoizM3c9nGh' \
         '2dM14z1Ude5FKhg%3D%3D'


'''def search_str(response,regex_list):
    try:
        for i in regex_list:
            re_com = re.comile(i)
            search_str = re_com.search(response)
            if search_str is None:'''


def contrast(response,succuss):
    if succuss not in response:
        print("没有匹配到预期结果")