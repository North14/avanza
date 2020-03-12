BASE_URL = 'https://www.avanza.se'

constants = {
  'paths': {},
  'public': {}
}


# Paths
constants['paths']['POSITIONS_PATH'] =             '/_mobile/account/positions'
constants['paths']['OVERVIEW_PATH'] =              '/_mobile/account/overview'
constants['paths']['ACCOUNT_OVERVIEW_PATH'] =      '/_mobile/account/{0:d}/overview'
constants['paths']['DEALS_AND_ORDERS_PATH'] =      '/_mobile/account/dealsandorders'
constants['paths']['WATCHLISTS_PATH'] =            '/_mobile/usercontent/watchlist'
constants['paths']['INSTRUMENT_PATH'] =            '/_mobile/market/{0:s}/{1:d}'
constants['paths']['INSPIRATION_LIST_PATH'] =      '/_mobile/marketing/inspirationlist/'
constants['paths']['TRANSACTIONS_PATH'] =          '/_mobile/account/transactions/{0:d}'
constants['paths']['CATEGORIZED_ACCOUNTS'] =       '/_cqbe/ff/overview/categorizedAccounts'

constants['paths']['CHARTDATA_PATH'] =             '/_mobile/chart/orderbook/{0:d}?timePeriod={1:s}'
constants['paths']['CHARTDATA_OVERVIEW'] =         '/_cqbe/ff/overview/chart/{}'
constants['paths']['CHARTDATA_DISTRIBUTION'] =     '/ab/component/accountsdistribution/chart'

constants['paths']['SEARCH'] =                     '/_cqbe/search/global-search/global-search-template?query={0:s}'
constants['paths']['NEWS'] =                       '/_cqbe/placera/feed-news-bill/{}'
constants['paths']['LOGIN'] =                      '/start(right-overlay:login/login-overlay)'
constants['paths']['HOME'] =                       '/hem/senaste.html'
constants['paths']['FEED'] =                       '/_cqbe/campaign/feed'
constants['paths']['ACCOUNTS'] =                   '/_cqbe/insights/customer/accounts'
constants['paths']['INSIGHT'] =                    '/_cqbe/insights/?timePeriod={}'

constants['paths']['WATCHLISTS_ADD_DELETE_PATH'] = '/_api/usercontent/watchlist/{}/orderbooks/{}'
constants['paths']['ORDERBOOK_PATH'] =             '/_mobile/order/?orderbookId={}'
constants['paths']['ORDERBOOK_LIST_PATH'] =        '/_mobile/market/orderbooklist/{}'

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

# Instruments
constants['public']['instruments'] = {}
constants['public']['instruments']['STOCK'] =                'STOCK'
constants['public']['instruments']['CERTIFICATE'] =          'CERTIFICATE'
constants['public']['instruments']['FUND'] =                 'FUND'
constants['public']['instruments']['BOND'] =                 'BOND'
constants['public']['instruments']['OPTION'] =               'OPTION'
constants['public']['instruments']['FUTURE_FORWARD'] =       'FUTURE_FORWARD'
constants['public']['instruments']['WARRANT'] =              'WARRANT'
constants['public']['instruments']['ETF'] =                  'ETF'
constants['public']['instruments']['INDEX'] =                'INDEX'
constants['public']['instruments']['PREMIUM_BOND'] =         'PREMIUM_BOND'
constants['public']['instruments']['SUBSCRIPTION_OPTION'] =  'SUBSCRIPTION_OPTION'
constants['public']['instruments']['EQUITY_LINKED_BOND'] =   'EQUITY_LINKED_BOND'
constants['public']['instruments']['CONVERTIBLE'] =          'CONVERTIBLE'
