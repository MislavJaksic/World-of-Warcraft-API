## [Getting Started](https://develop.battle.net/documentation/guides/getting-started)

You will need:
* to have or create a `Battle.net` account
* to login to your `Battle.net` account
* to create a `Client` through the `API Access` menu option
* to generate a `Secret` for the `Client`
* to understand how Blizzard APIs work with `OAuth`
* to learn how to make API requests

### Log in or register an account

Create or login to your `Battle.net` account.  
Attach a `Blizzard Authenticator`.  
Carefully read and accept the `Blizzard Developer API Terms of Use`.  

### Creating a client

```
Login -> API Access -> Create New Client ->

Client Name: a name to identify your client
Redirect URIs: URI to redirect the user to after they finish authorizing through the Blizzard's login page; used with OAuth authentication
Service URL: URL of the service that will be using this client
Intended Use: how you intend to use this client
```

### Managing clients

It can be done.  

### Generating a new client secret

To generate a new `Client` `Secret`:
* generate a new `Secret`
* invalidate the old `Secret`

### Read the documentation

[Using OAuth](../UsingOAuth)  
[Game Data APIs](../GameDataAPI)  
[Community APIs](../CommunityAPI)  
[Regionality and APIs](../RegionalityAndAPI)

### Making API requests

Blizzard API requests require client credentials.  
Access tokens are granted by:  
* [OAuth client credentials flow](../UsingOAuth/ClientCredentialsFlow)
* [OAuth authorization code flow](../UsingOAuth/AuthorizationCodeFlow)

Blizzard URIs follow the syntax:
* `Region-Id.api.blizzard.com/API-Path`
* `gateway.battlenet.com.cn/API-Path` for China

Example request, get the current price of a WoW Token:
1) follow the [OAuth client credentials flow](../UsingOAuth/ClientCredentialsFlow) to get an access token
2) `$: curl --user Client-Id:Client-Secret --data grant_type=client_credentials https://us.battle.net/oauth/token`
3) `$: curl --header "Authorization: Bearer Access-Token" https://us.api.blizzard.com/data/wow/token/?namespace=dynamic-us`

### Throttling

API clients are limited to:
* 36,000 requests per hour
* 100 requests per second
