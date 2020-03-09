BASE_URL = 'https://www.avanza.se'

constants = {
  'paths': {},
  'public': {}
}


# Paths
constants['paths']['POSITIONS_PATH'] =             '/_mobile/account/positions'
constants['paths']['OVERVIEW_PATH'] =              '/_mobile/account/overview'
constants['paths']['ACCOUNT_OVERVIEW_PATH'] =      '/_mobile/account/{}/overview'
constants['paths']['DEALS_AND_ORDERS_PATH'] =      '/_mobile/account/dealsandorders'
constants['paths']['WATCHLISTS_PATH'] =            '/_mobile/usercontent/watchlist'
constants['paths']['WATCHLISTS_ADD_DELETE_PATH'] = '/_api/usercontent/watchlist/{}/orderbooks/{}'
constants['paths']['STOCK_PATH'] =                 '/_mobile/market/stock/{}'
constants['paths']['FUND_PATH'] =                  '/_mobile/market/fund/{}'
constants['paths']['CERTIFICATE_PATH'] =           '/_mobile/market/certificate/{}'
constants['paths']['INSTRUMENT_PATH'] =            '/_mobile/market/{}/{}'
constants['paths']['ORDERBOOK_PATH'] =             '/_mobile/order/{}'
constants['paths']['ORDERBOOK_LIST_PATH'] =        '/_mobile/market/orderbooklist/{}'
constants['paths']['CHARTDATA_PATH'] =             '/_mobile/chart/orderbook/{}'
constants['paths']['ORDER_PLACE_DELETE_PATH'] =    '/_api/order'
constants['paths']['ORDER_EDIT_PATH'] =            '/_api/order/{}/{}'
constants['paths']['ORDER_GET_PATH'] =             '/_mobile/order/{}'
constants['paths']['SEARCH_PATH'] =                '/_mobile/market/search/{}'
constants['paths']['INSPIRATION_LIST_PATH'] =      '/_mobile/marketing/inspirationlist/{}'
constants['paths']['TRANSACTIONS_PATH'] =          '/_mobile/account/transactions/{}'
constants['paths']['CATEGORIZED_ACCOUNTS'] =       '/_cqbe/ff/overview/categorizedAccounts'
constants['paths']['CHARTDATA_OVERVIEW'] =         '/_cqbe/ff/overview/chart/{}'
constants['paths']['CHARTDATA_DISTRIBUTION'] =     '/ab/component/accountsdistribution/chart/'
constants['paths']['SEARCH'] =                     '/_cqbe/search/global-search/global-search-template?query={}'
constants['paths']['NEWS'] =                       '/_cqbe/placera/feed-news-bill/{}'
constants['paths']['LOGIN'] =                      '/start(right-overlay:login/login-overlay)'
constants['paths']['HOME'] =                       '/hem/senaste.html'
constants['paths']['FEED'] =                       '/_cqbe/campaign/feed'
constants['paths']['ACCOUNTS'] =                   '/_cqbe/insights/customer/accounts'
constants['paths']['INSIGHT'] =                    '/_cqbe/insights/?timePeriod={}'


# Chartdata
constants['public']['chartdata'] =                  {}
constants['public']['chartdata']['TODAY'] =         'TODAY'
constants['public']['chartdata']['ONE_MONTH'] =     'ONE_MONTH'
constants['public']['chartdata']['THREE_MONTHS'] =  'THREE_MONTHS'
constants['public']['chartdata']['ONE_WEEK'] =      'ONE_WEEK'
constants['public']['chartdata']['THIS_YEAR'] =     'THIS_YEAR'
constants['public']['chartdata']['ONE_YEAR'] =      'ONE_YEAR'
constants['public']['chartdata']['THREE_YEARS'] =   'THREE_YEARS'
constants['public']['chartdata']['FIVE_YEARS'] =    'FIVE_YEARS'
