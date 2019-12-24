## [Developer portal](https://develop.battle.net/)

### Get Client Id and Secret

You will need:
* to have or create a `Battle.net` account
* to login to your `Battle.net` account
* to create a `Client` through the `API Access` menu option
* to generate a `Secret` for the `Client`

### Get an access token

```
$: curl --user Client-Id:Client-Secret --data grant_type=client_credentials https://us.battle.net/oauth/token
```

### Make API requests

```
$: curl --header "Authorization: Bearer Access-Token" https://Region-Id.api.blizzard.com/API-Path
```
