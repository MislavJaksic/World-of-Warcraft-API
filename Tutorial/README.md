## [Developer portal](https://develop.battle.net/)

### Get Client Id and Secret

### Get an access token

```
$: curl --user Client-Id:Client-Secret --data grant_type=client_credentials https://us.battle.net/oauth/token
```

### Get "game data"

```
$: curl --header "Authorization: Bearer Access-Token" https://Region-Id.api.blizzard.com/API-Path
```
