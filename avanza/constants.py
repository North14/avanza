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


# Search
constants['public']['STOCK'] =               'stock'
constants['public']['FUND'] =                'fund'
constants['public']['BOND'] =                'bond'
constants['public']['OPTION'] =              'option'
constants['public']['FUTURE_FORWARD'] =      'future_forward'
constants['public']['CERTIFICATE'] =         'certificate'
constants['public']['WARRANT'] =             'warrant'
constants['public']['ETF'] =                 'exchange_traded_fund'
constants['public']['INDEX'] =               'index'
constants['public']['PREMIUM_BOND'] =        'premium_bond'
constants['public']['SUBSCRIPTION_OPTION'] = 'subscription_option'
constants['public']['EQUITY_LINKED_BOND'] =  'equity_linked_bond'
constants['public']['CONVERTIBLE'] =         'convertible'


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


# Marketing
constants['public']['HIGHEST_RATED_FUNDS'] = 'HIGHEST_RATED_FUNDS'
constants['public']['LOWEST_FEE_INDEX_FUNDS'] = 'LOWEST_FEE_INDEX_FUNDS'
constants['public']['BEST_DEVELOPMENT_FUNDS_LAST_THREE_MONTHS'] = 'BEST_DEVELOPMENT_FUNDS_LAST_THREE_MONTHS'
constants['public']['MOST_OWNED_FUNDS'] = 'MOST_OWNED_FUNDS'


# Transactions
constants['public']['OPTIONS'] =          'options'
constants['public']['FOREX'] =            'forex'
constants['public']['DEPOSIT_WITHDRAW'] = 'deposit-withdraw'
constants['public']['BUY_SELL'] =         'buy-sell'
constants['public']['DIVIDEND'] =         'dividend'
constants['public']['INTEREST'] =         'interest'
constants['public']['FOREIGN_TAX'] =      'foreign-tax'


# Channels
constants['public']['ACCOUNTS'] =           'accounts'
constants['public']['QUOTES'] =             'quotes'
constants['public']['ORDERDEPTHS'] =        'orderdepths'
constants['public']['TRADES'] =             'trades'
constants['public']['BROKERTRADESUMMARY'] = 'brokertradesummary'
constants['public']['POSITIONS'] =          'positions'
constants['public']['ORDERS'] =             'orders'
constants['public']['DEALS'] =              'deals'


# Order types
constants['public']['BUY'] =  'BUY'
constants['public']['SELL'] = 'SELL'
