#### Turnauksen järjestäjänä...
* haluan luoda uusia turnauksia.
```
INSERT INTO Cup (name, start_time, end_time, points, account_id) VALUES ('Espoo-Cup', '2019-06-02' 09:00:00, '2019-06-02 18:00:00', 100, 1)
```
* haluan muokata luomiani turnauksia.
```
UPDATE Cup SET date_modified=CURRENT_TIMESTAMP, points=150 WHERE cup.id = 1
```
* haluan poistaa luomani turnauksen.
* haluan lisätä luomaani turnaukseen joukkueita.
* haluan päivittää turnauksen tuloksia.

#### Lajin seuraajana...
* haluan selata turnauksia, joukkueita ja turnausten tuloksia.
* haluan tietää miten joukkueeni pärjää suhteessa muihin joukkueisiin seuraamalla joukkueiden rankkauspistetilannetta.
```
SELECT Team.name, Team.home, SUM(Result.points) AS points, Team.id FROM Team LEFT JOIN Result ON Team.id = Result.team_id GROUP BY Team.name, Team.home, Team.id ORDER BY points DESC
```
* haluan tietää, milloin seuraava turnaus järjestetään.
```
SELECT Cup.name, Cup.start_time, Cup.end_time, Cup.points, COUNT(Result.team_id) AS teams FROM Cup LEFT JOIN Result ON Cup.id = Result.cup_id WHERE Cup.start_time >= CURRENT_TIMESTAMP GROUP BY Cup.name, Cup.start_time, Cup.end_time, Cup.points ORDER BY Cup.start_time
```
#### Ylläpitäjänä...
* haluan luoda, muokata ja poistaa joukkueita.
* haluan luoda, muokata ja poistaa turnauksia.
* haluan luoda, muokata ja poistaa tuloksia.