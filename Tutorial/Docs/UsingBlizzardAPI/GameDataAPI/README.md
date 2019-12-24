## [Game Data APIs](https://develop.battle.net/documentation/guides/game-data-apis)

Data:
* game data API:
    * static data: data related to a game itself
    * dynamic data: changing, world-related data that is not connected to players
* profile API: data related to individuals, their characters or accounts

Structure: JSON that can be localized using an identifier  
Namespaces: allows multiple instances of the same type of document to coexist  
* Request Header: `Battlenet-Namespace`
* Query Parameter: `?namespace=`
Authorization: requires an access token  
Response format: you may need to follow up links to get the whole resource  
