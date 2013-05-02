Account and SubAccount
---------------------------------

This corresponds to the accounts API as described at:

https://www.plivo.com/docs/api/account/

Account
============

Provides these two methods::

    account = client.Account.get(...) #Returns a client object
    client.Account.modify(...) #Modify the account
    #TODO: Check if this works
    account.modify(...)



SubAccount
============

Provides these methods::


    sub_account = client.SubAccount.create(...)
    sub_account = client.SubAccount.get(...)
    sub_accounts = client.SubAccount.get_all()#List of all sub accounts
    sub_account.modify(..)
    sub_account.delete(..)




