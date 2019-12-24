## [Client Credentials Flow](https://develop.battle.net/documentation/guides/using-oauth/client-credentials-flow)

Exchange client credentials for an access token.  

```
$: curl --user Client-Id:Client-Secret --data grant_type=client_credentials https://us.battle.net/oauth/token

$: curl --header "Authorization: Bearer Access-Token" https://Region-Id.api.blizzard.com/API-Path
```
