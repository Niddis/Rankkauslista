#### Turnauksen järjestäjänä...
* haluan luoda uusia turnauksia.
* haluan lisätä luomaani turnaukseen joukkueita.
* haluan päivittää turnauksen tuloksia.

#### Lajin seuraajana...
* haluan selata turnauksia, joukkueita ja turnausten tuloksia.
* haluan tietää miten joukkueeni pärjää suhteessa muihin joukkueisiin seuraamalla joukkueiden pistetilannetta.

SQL-kysely: "SELECT Team.name, Team.home, SUM(Result.points) AS points, Team.id FROM Team LEFT JOIN Result ON Team.id = Result.team_id GROUP BY Team.name, Team.home, Team.id ORDER BY points DESC"

* haluan tietää, milloin seuraava turnaus järjestetään.

SQL-kysely: "SELECT Cup.name, Cup.start_time, Cup.end_time, Cup.points, COUNT(Result.team_id) AS teams FROM Cup LEFT JOIN Result ON Cup.id = Result.cup_id WHERE Cup.start_time >= CURRENT_TIMESTAMP GROUP BY Cup.name, Cup.start_time, Cup.end_time, Cup.points ORDER BY Cup.start_time"

#### Ylläpitäjänä...
* haluan hallinoida joukkueita, turnauksia ja tuloksia.