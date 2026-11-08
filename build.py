#!/usr/bin/env python3
"""Generates the static site: index.html and sports/<slug>.html.

All sport content lives in SPORTS below. Edit it, then run:  python3 build.py
"""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "Sports for Non-Sports People"

SPORTS = [
    {
        "slug": "american-football",
        "name": "American Football",
        "emoji": "🏈",
        "color": "#8a4b2a",
        "tagline": "Chess with collisions, played a few yards at a time.",
        "description": [
            "American football is a game of territory. Two teams of 11 take turns trying to move an oval ball down a 100-yard field and into the other team's end zone. The game stops after almost every play, which leaves time for strategy (and for snacks).",
            "It is the most-watched sport in the United States. The NFL's championship game, the Super Bowl, is held every February and is as much a cultural event as a game, famous for its halftime show and its ads.",
        ],
        "facts": [("Players on the field", "11 per team"), ("Game length", "4 quarters × 15 min (about 3 hours in real time)"), ("Season", "September to February"), ("Big final", "The Super Bowl")],
        "rules": [
            "The team with the ball (the <b>offense</b>) gets four tries, called <b>downs</b>, to move the ball 10 yards. If they make it, they get a fresh set of four downs.",
            "If they fail, the other team gets the ball. That's why teams usually kick it away (a <b>punt</b>) on 4th down.",
            "You move the ball by running with it or by throwing a forward pass. The <b>quarterback</b> is the player who usually throws.",
            "<b>Touchdown</b> (carry or catch the ball in the end zone): 6 points, then a 1-point kick or a 2-point play.",
            "<b>Field goal</b> (kick the ball through the tall goalposts): 3 points. <b>Safety</b> (tackling the offense in its own end zone): 2 points.",
            "Yellow flags thrown by referees mean a penalty, usually costing the guilty team some yards.",
        ],
        "leagues": [("NFL", "National Football League. 32 teams, the top professional league."), ("College football (NCAA)", "Hugely popular, especially in the American South and Midwest."), ("CFL", "Canadian Football League. Slightly different rules and a bigger field.")],
        "teams_title": "Famous teams",
        "teams": [("Dallas Cowboys", "Nicknamed “America's Team” and among the most valuable sports franchises in the world."), ("New England Patriots", "Won six Super Bowls in the Tom Brady era."), ("Pittsburgh Steelers", "Six Super Bowl wins and a famously loyal fan base."), ("Green Bay Packers", "Owned by their fans and based in a small Wisconsin city."), ("Kansas City Chiefs", "The dominant team of the 2020s."), ("San Francisco 49ers", "A dynasty in the 1980s.")],
        "players": [("Tom Brady", "Quarterback with 7 Super Bowl wins, widely seen as the greatest ever."), ("Patrick Mahomes", "Chiefs quarterback known for no-look and sidearm throws."), ("Travis Kelce", "Chiefs tight end, also famous outside sports for his relationship with Taylor Swift."), ("Jerry Rice", "Holds nearly every career receiving record."), ("Peyton Manning", "Quarterback, two Super Bowl wins, now a TV personality.")],
        "lingo": [("Snap", "The hike of the ball that starts each play."), ("Interception", "A pass caught by the defense. Bad news for the quarterback."), ("Sack", "Tackling the quarterback before he can throw."), ("Hail Mary", "A long, desperate pass at the end of a half.")],
        "smart": "“They should go for it on fourth down.” Fans argue about this constantly, and analytics usually back you up.",
    },
    {
        "slug": "soccer",
        "name": "Soccer (Football)",
        "emoji": "⚽",
        "color": "#2e7d32",
        "tagline": "The world's game: one ball, two goals, no hands.",
        "description": [
            "Soccer, called “football” almost everywhere outside the US, is the most popular sport on Earth. Two teams of 11 try to kick or head the ball into the other team's net. Only the goalkeepers may use their hands.",
            "Goals are rare (a 1–0 game is normal), so each one is a huge moment. The FIFA World Cup, held every four years, is the most-watched sporting event in the world. The 2026 edition is hosted by the USA, Canada and Mexico.",
        ],
        "facts": [("Players on the field", "11 per team, including a goalkeeper"), ("Game length", "2 halves × 45 min, plus “stoppage time”"), ("Season", "August to May in Europe, February to December in MLS"), ("Big final", "The World Cup (every 4 years) and the Champions League final (every year)")],
        "rules": [
            "Score by getting the whole ball over the goal line between the posts.",
            "No hands or arms, except for the goalkeeper inside their own penalty area.",
            "<b>Offside</b>: an attacker can't be closer to the goal than the second-to-last defender at the moment a teammate passes to them. Basically, no lurking by the goal.",
            "Fouls give the other team a free kick. A foul inside the penalty area gives a <b>penalty kick</b>: one shooter against the goalie from 12 yards.",
            "A <b>yellow card</b> is a warning. A second yellow or a straight <b>red card</b> sends the player off, and the team plays a player short.",
            "League games can end in a tie (a “draw”). Knockout games go to extra time and then a penalty shootout.",
        ],
        "leagues": [("English Premier League", "The richest and most-watched league in the world."), ("La Liga (Spain)", "Home of Real Madrid and Barcelona."), ("Serie A (Italy), Bundesliga (Germany), Ligue 1 (France)", "The rest of Europe's “Big Five” leagues."), ("UEFA Champions League", "A yearly tournament between the best club teams in Europe."), ("MLS", "Major League Soccer, the top league in the US and Canada."), ("FIFA World Cup", "National teams, every four years.")],
        "teams_title": "Famous teams",
        "teams": [("Real Madrid", "The record winner of the European Cup / Champions League."), ("FC Barcelona", "Known for its passing style and for being Messi's longtime club."), ("Manchester United", "England's most famous club around the world."), ("Liverpool", "Famous for its anthem, “You'll Never Walk Alone.”"), ("Bayern Munich", "Germany's powerhouse, winning the league almost every year."), ("Brazil (national team)", "Five World Cup titles, more than any other country.")],
        "players": [("Lionel Messi", "Argentine magician who won the 2022 World Cup. Often called the GOAT."), ("Cristiano Ronaldo", "Portuguese superstar, all-time leading international goal scorer."), ("Pelé", "Brazilian legend who won three World Cups."), ("Diego Maradona", "Argentine icon, famous for the “Hand of God” goal in 1986."), ("Kylian Mbappé", "French forward, a World Cup winner at 19."), ("Erling Haaland", "Norwegian goal-scoring machine.")],
        "lingo": [("Pitch", "The field."), ("Clean sheet", "When a team doesn't concede a goal."), ("Nil", "Zero, as in “two-nil.”"), ("Hat trick", "One player scoring three goals in a game.")],
        "smart": "“VAR is ruining the game.” The video review system is the most reliable complaint in soccer.",
    },
    {
        "slug": "basketball",
        "name": "Basketball",
        "emoji": "🏀",
        "color": "#e65100",
        "tagline": "Fast, high-scoring, and played above the rim.",
        "description": [
            "Basketball is played by two teams of five on an indoor court. Each team tries to shoot the ball through a hoop 10 feet off the ground. Scoring is constant, often more than 100 points per team in the NBA, so the action rarely stops.",
            "Invented in 1891 by James Naismith in Massachusetts, it is now one of the most global sports, and its stars are some of the most famous athletes on the planet.",
        ],
        "facts": [("Players on the court", "5 per team"), ("Game length", "NBA: 4 quarters × 12 min (about 2.5 hours real time)"), ("Season", "October to June"), ("Big final", "The NBA Finals, and “March Madness” in college")],
        "rules": [
            "A basket counts <b>2 points</b>, or <b>3 points</b> if shot from behind the curved three-point line.",
            "<b>Free throws</b>, unguarded shots after certain fouls, are worth 1 point each.",
            "You must <b>dribble</b> (bounce) the ball while moving. Walking with it is <b>traveling</b>.",
            "The <b>shot clock</b> gives a team 24 seconds (NBA) to shoot, so nobody can stall.",
            "Too much physical contact is a <b>foul</b>. In the NBA, a player with 6 fouls must leave the game.",
            "Ties go to 5-minute overtime periods until someone wins.",
        ],
        "leagues": [("NBA", "National Basketball Association. 30 teams in the US and Canada."), ("WNBA", "The top women's professional league, growing fast."), ("NCAA", "College basketball. Its March Madness tournament is famous for upsets and office bracket pools."), ("EuroLeague", "The top club competition in Europe.")],
        "teams_title": "Famous teams",
        "teams": [("Los Angeles Lakers", "Hollywood's team: Magic, Kareem, Kobe, Shaq, LeBron."), ("Boston Celtics", "Tied with the Lakers for the most NBA titles."), ("Chicago Bulls", "Michael Jordan's six-title dynasty of the 1990s."), ("Golden State Warriors", "Revolutionized the game with three-point shooting in the 2010s."), ("Harlem Globetrotters", "An exhibition team famous for comedy and trick shots.")],
        "players": [("Michael Jordan", "Six titles with the Bulls, the most common pick for greatest ever."), ("LeBron James", "Four titles and the NBA's all-time leading scorer."), ("Stephen Curry", "The greatest shooter ever, who made the three-pointer king."), ("Kobe Bryant", "Five titles with the Lakers. Known for his “Mamba mentality.”"), ("Caitlin Clark", "Record-breaking college scorer turned WNBA star."), ("Shaquille O'Neal", "Giant center, now a beloved TV personality.")],
        "lingo": [("Dunk", "Slamming the ball down through the hoop."), ("Triple-double", "Reaching 10+ in three stats (like points, rebounds, assists) in one game."), ("Rebound", "Grabbing a missed shot."), ("Buzzer-beater", "A shot that goes in as time expires.")],
        "smart": "“Jordan or LeBron?” This debate never ends, and both answers are defensible.",
    },
    {
        "slug": "baseball",
        "name": "Baseball",
        "emoji": "⚾",
        "color": "#1565c0",
        "tagline": "America's pastime: a summer game of pitcher versus batter.",
        "description": [
            "Baseball is a duel at its core: a pitcher throws, a batter tries to hit, and the rest of the game flows from there. Teams take turns batting and fielding. A run scores when a batter makes it all the way around four bases.",
            "There is no game clock, though a pitch clock added in 2023 sped things up. With 162 games a season, baseball is part of everyday summer life: a radio broadcast, a hot dog at the ballpark, a box score in the paper.",
        ],
        "facts": [("Players on the field", "9 fielders for the defense"), ("Game length", "9 innings (about 2.5–3 hours)"), ("Season", "Late March to October (162 games)"), ("Big final", "The World Series")],
        "rules": [
            "An <b>inning</b> has two halves: each team bats once. A half ends when the batting team gets <b>3 outs</b>.",
            "The pitcher throws toward the batter. A swing-and-miss, or a good pitch that isn't swung at, is a <b>strike</b>. 3 strikes is a <b>strikeout</b>.",
            "A pitch outside the strike zone that isn't swung at is a <b>ball</b>. 4 balls is a <b>walk</b>, and the batter goes to first base free.",
            "Hit the ball and run. You're out if a fielder catches it in the air, or throws it to the base before you get there.",
            "Touching first, second, third and home base scores a <b>run</b>. Hitting it over the outfield wall is a <b>home run</b>.",
            "After 9 innings, the team with more runs wins. Ties go to extra innings.",
        ],
        "leagues": [("MLB", "Major League Baseball. 30 teams split into the American and National Leagues."), ("Nippon Professional Baseball", "Japan's top league, with famously passionate fans."), ("KBO League", "South Korea's top league, known for bat flips and cheer squads."), ("World Baseball Classic", "An international tournament between national teams.")],
        "teams_title": "Famous teams",
        "teams": [("New York Yankees", "27 World Series titles, by far the most."), ("Boston Red Sox", "The Yankees' archrivals. Ended an 86-year title drought in 2004."), ("Los Angeles Dodgers", "Big-spending powerhouse, and the team of Jackie Robinson (when in Brooklyn)."), ("Chicago Cubs", "Ended a 108-year championship drought in 2016."), ("St. Louis Cardinals", "The most successful National League franchise.")],
        "players": [("Babe Ruth", "The original sports superstar. Home-run-hitting legend of the 1920s."), ("Jackie Robinson", "Broke MLB's color barrier in 1947. Every player wears his #42 on April 15."), ("Shohei Ohtani", "Japanese phenom who both pitches and hits at an elite level."), ("Aaron Judge", "Yankees slugger who holds the American League home run record."), ("Derek Jeter", "Beloved Yankees shortstop and five-time champion.")],
        "lingo": [("Grand slam", "A home run with the bases loaded: 4 runs at once."), ("Bullpen", "The relief pitchers, and the area where they warm up."), ("No-hitter", "A game where a pitcher allows zero hits. Rare and celebrated."), ("Seventh-inning stretch", "When everyone stands and sings “Take Me Out to the Ball Game.”")],
        "smart": "“Pitching wins championships.” It's a cliché, but nobody will argue with you.",
    },
    {
        "slug": "ice-hockey",
        "name": "Ice Hockey",
        "emoji": "🏒",
        "color": "#0277bd",
        "tagline": "The fastest team sport, played on knives on ice.",
        "description": [
            "Ice hockey is played on skates. Players use sticks to shoot a hard rubber disc, the <b>puck</b>, into the other team's net. It is extremely fast, and players change on the fly every 45 seconds or so because skating at that speed is exhausting.",
            "Hockey is Canada's national obsession and hugely popular in the northern US, Scandinavia, Russia and Central Europe. Its trophy, the Stanley Cup, is one of the oldest in pro sports, and each winning player gets to spend a day with it.",
        ],
        "facts": [("Players on the ice", "6 per team (5 skaters + a goalie)"), ("Game length", "3 periods × 20 min (about 2.5 hours real time)"), ("Season", "October to June"), ("Big final", "The Stanley Cup Final")],
        "rules": [
            "Get the puck into the net for <b>1 goal</b>. Most goals wins.",
            "<b>Offside</b>: attackers can't enter the opponent's zone (past the blue line) before the puck does.",
            "<b>Icing</b>: you can't just fire the puck the length of the ice to clear it. Play stops and restarts near your own goal.",
            "Penalties (tripping, high-sticking and so on) send a player to the <b>penalty box</b>, usually for 2 minutes. The other team gets a <b>power play</b> with an extra skater.",
            "Body checking (hitting with the shoulder or hip) is legal in men's pro hockey. Fighting earns a 5-minute penalty but is still tolerated.",
            "Regular-season ties go to overtime and then a shootout. Playoff games use sudden-death overtime until someone scores.",
        ],
        "leagues": [("NHL", "National Hockey League. 32 teams across the US and Canada."), ("PWHL", "Professional Women's Hockey League, launched in 2024."), ("KHL", "Russia-based league, the second strongest in the world."), ("Winter Olympics", "Where countries like Canada, the US, Sweden and Finland battle for gold.")],
        "teams_title": "Famous teams",
        "teams": [("Montreal Canadiens", "24 Stanley Cups, the most of any team."), ("Toronto Maple Leafs", "Hugely popular, and famous for a Cup drought dating to 1967."), ("Detroit Red Wings", "“Hockeytown,” where fans throw octopuses on the ice."), ("Boston Bruins", "One of the “Original Six” founding teams, known for toughness."), ("Edmonton Oilers", "Wayne Gretzky's dynasty of the 1980s.")],
        "players": [("Wayne Gretzky", "“The Great One.” Holds dozens of records and is the clear GOAT."), ("Alex Ovechkin", "Russian sniper who broke Gretzky's career goals record in 2025."), ("Sidney Crosby", "Canadian captain and three-time Cup winner with Pittsburgh."), ("Connor McDavid", "Considered the fastest and most skilled player of today."), ("Mario Lemieux", "Pittsburgh legend who also later owned the team.")],
        "lingo": [("Hat trick", "Three goals by one player. Fans throw hats onto the ice."), ("Power play", "Having more players because the other team took a penalty."), ("Five-hole", "The gap between a goalie's legs."), ("Playoff beard", "Players don't shave during the playoffs.")],
        "smart": "“The goalie stood on his head.” It means the goalie played amazingly. Say it after any close win.",
    },
    {
        "slug": "tennis",
        "name": "Tennis",
        "emoji": "🎾",
        "color": "#827717",
        "tagline": "One-on-one combat with rackets and strange scoring.",
        "description": [
            "In tennis, two players (or two pairs, in doubles) hit a ball back and forth over a net with rackets. You win a point when your opponent can't return the ball into the court. There's no clock: a match lasts until someone wins, which can take an hour or five.",
            "The sport revolves around four huge tournaments, the <b>Grand Slams</b>. They are played on different surfaces (hard courts, clay and grass), and each one rewards a different style of play.",
        ],
        "facts": [("Players", "1 vs 1 (singles) or 2 vs 2 (doubles)"), ("Match length", "Best of 3 sets (best of 5 for men at Grand Slams)"), ("Season", "January to November, all around the world"), ("Biggest events", "The four Grand Slams")],
        "rules": [
            "Points within a game go <b>0 (“love”), 15, 30, 40, game</b>. Yes, really.",
            "At 40–40 (<b>deuce</b>), a player must win two points in a row. The first one gives them the <b>advantage</b>.",
            "Win <b>6 games</b> (by at least 2) to win a <b>set</b>. At 6–6, a <b>tiebreak</b> usually decides it.",
            "The server gets two tries to land the serve in the diagonal box. Missing both is a <b>double fault</b>.",
            "The ball may bounce only once on your side. A ball landing on the line counts as in.",
            "Players switch serving every game and switch ends of the court every two games.",
        ],
        "leagues": [("ATP Tour", "The men's professional tour."), ("WTA Tour", "The women's professional tour."), ("Davis Cup / Billie Jean King Cup", "Team competitions between countries.")],
        "teams_title": "The big four tournaments",
        "teams": [("Australian Open", "Melbourne, January. Hard courts and serious heat."), ("French Open (Roland-Garros)", "Paris, late May to June. Slow red clay."), ("Wimbledon", "London, July. Grass, an all-white dress code, strawberries and cream."), ("US Open", "New York, late August to September. Loud night sessions under the lights.")],
        "players": [("Serena Williams", "23 Grand Slam singles titles and a cultural icon."), ("Roger Federer", "Swiss maestro, admired for his graceful style."), ("Rafael Nadal", "Spanish “King of Clay” with a record 14 French Open titles."), ("Novak Djokovic", "Serbian with the most men's Grand Slam titles ever."), ("Carlos Alcaraz", "Spanish young star with a flashy, exciting style."), ("Jannik Sinner", "Italian star and Alcaraz's great modern rival.")],
        "lingo": [("Ace", "A serve the opponent can't even touch."), ("Break", "Winning a game while your opponent serves."), ("Love", "Zero."), ("Grand Slam", "One of the four majors, or winning all four in one year.")],
        "smart": "“Serve is so important on grass.” It's true at Wimbledon, and it sounds very knowledgeable.",
    },
    {
        "slug": "golf",
        "name": "Golf",
        "emoji": "⛳",
        "color": "#33691e",
        "tagline": "A long walk where the lowest score wins.",
        "description": [
            "In golf, players hit a small ball into a series of holes, usually 18, spread across a large outdoor course. The goal is to use as few strokes (swings) as possible. Players mostly compete against the course rather than against each other directly.",
            "Pro tournaments run four days. TV coverage hops between players around the course, and the tension builds on Sunday afternoon as the leaders reach the final holes.",
        ],
        "facts": [("Players", "Individual, usually grouped in twos or threes"), ("Tournament length", "4 rounds of 18 holes, Thursday to Sunday"), ("Season", "Year-round, with the biggest events April to July"), ("Biggest events", "The four majors and the Ryder Cup")],
        "rules": [
            "Each hole has a <b>par</b>, the number of strokes a skilled golfer should need (3, 4 or 5).",
            "One under par is a <b>birdie</b>, two under is an <b>eagle</b>, and one over is a <b>bogey</b>.",
            "Scores are shown relative to par, so “−10” means 10 strokes under par for the tournament. Lower is better.",
            "Players may carry at most 14 clubs. Drivers hit far, irons are for precision, and putters roll the ball on the green.",
            "You play the ball where it lies. Hitting it into water or out of bounds costs penalty strokes.",
            "Golf runs on etiquette: stay quiet during a swing, and players often call penalties on themselves.",
        ],
        "leagues": [("PGA Tour", "The main men's professional tour, based in the US."), ("LPGA Tour", "The top women's tour."), ("DP World Tour", "The European-based men's tour."), ("LIV Golf", "Saudi-funded rival league with team events, launched in 2022.")],
        "teams_title": "The big events",
        "teams": [("The Masters", "April, at Augusta National. The winner gets a green jacket."), ("PGA Championship", "May, at a different US course each year."), ("U.S. Open", "June. Known for brutally hard courses."), ("The Open Championship", "July, on windy seaside links courses in the UK."), ("Ryder Cup", "USA vs Europe team event every two years. Fans get rowdy.")],
        "players": [("Tiger Woods", "15 majors and the reason golf became cool for a generation."), ("Jack Nicklaus", "“The Golden Bear,” with a record 18 majors."), ("Arnold Palmer", "1960s icon, also the name of the iced tea and lemonade drink."), ("Rory McIlroy", "Northern Irish star who completed the career Grand Slam in 2025."), ("Scottie Scheffler", "The dominant world No. 1 of the mid-2020s."), ("Annika Sörenstam", "Swedish legend of women's golf.")],
        "lingo": [("Hole in one", "Getting the ball in with a single shot."), ("Fore!", "Shouted to warn people that a ball is flying their way."), ("Fairway", "The short, neat grass leading to the green."), ("Caddie", "The person who carries the bag and gives advice.")],
        "smart": "“Drive for show, putt for dough.” It means the short shots on the green decide who wins.",
    },
    {
        "slug": "cricket",
        "name": "Cricket",
        "emoji": "🏏",
        "color": "#6d4c41",
        "tagline": "Bat and ball, beloved by billions, and sometimes 5 days long.",
        "description": [
            "Cricket is a bat-and-ball game played by two teams of 11. One team bats and tries to score runs, while the other bowls and fields and tries to get batters out. Then they swap. It's huge in India, Pakistan, Australia, England, South Africa, the Caribbean and beyond, with perhaps more than a billion fans.",
            "It comes in different lengths. Traditional <b>Test</b> matches last up to five days and can still end in a draw. The modern <b>T20</b> format finishes in about three hours and is full of big hitting.",
        ],
        "facts": [("Players", "11 per team"), ("Game length", "T20: ~3 hours · One-Day: ~8 hours · Test: up to 5 days"), ("Season", "Year-round, moving around the globe"), ("Biggest events", "The Cricket World Cup, the Ashes and the IPL")],
        "rules": [
            "A <b>bowler</b> delivers the ball, usually with one bounce, toward a <b>wicket</b> (three wooden stumps). The batter defends it.",
            "Batters score <b>runs</b> by running between the two wickets after hitting the ball.",
            "Hitting the ball over the boundary rope along the ground scores <b>4</b>. Clearing it in the air scores <b>6</b>.",
            "Main ways to get out: <b>bowled</b> (the ball hits the stumps), <b>caught</b> (a fielder catches the hit in the air), <b>LBW</b> (the ball would have hit the stumps but hit the batter's leg) and <b>run out</b>.",
            "An <b>over</b> is 6 balls from one bowler. T20 gives each team 20 overs, and One-Day matches give 50.",
            "An innings ends when 10 batters are out or the overs run out. The team with more runs wins.",
        ],
        "leagues": [("Indian Premier League (IPL)", "A glitzy T20 league and one of the richest competitions in all of sports."), ("ICC Cricket World Cup", "The 50-over world championship, every four years."), ("ICC T20 World Cup", "The short-format world championship."), ("The Ashes", "The historic Test rivalry between England and Australia."), ("Big Bash League / The Hundred", "Popular short-format leagues in Australia and England.")],
        "teams_title": "Famous teams",
        "teams": [("India", "A cricket-mad nation, and the sport's financial powerhouse."), ("Australia", "The most successful World Cup team in history."), ("England", "Where the game was invented."), ("Mumbai Indians", "One of the most successful IPL teams."), ("Chennai Super Kings", "A hugely popular IPL team, long led by MS Dhoni.")],
        "players": [("Sachin Tendulkar", "Indian “Little Master,” scorer of 100 international centuries."), ("Virat Kohli", "Modern Indian superstar with an enormous social media following."), ("Don Bradman", "Australian whose batting average of 99.94 is considered the greatest stat in any sport."), ("MS Dhoni", "Calm Indian captain who won the 2011 World Cup."), ("Shane Warne", "Australian spin-bowling genius."), ("Brian Lara", "West Indies legend with a record 400 runs in one Test innings.")],
        "lingo": [("Century", "100 runs by one batter."), ("Duck", "Getting out for zero."), ("Howzat?", "“How's that?” Fielders shout it to appeal for an out."), ("Pitch", "The strip in the middle where the action happens.")],
        "smart": "“Test cricket is the real test.” Traditionalists will love you for saying it.",
    },
    {
        "slug": "formula-1",
        "name": "Formula 1",
        "emoji": "🏎️",
        "color": "#c62828",
        "tagline": "Motorsport's top tier: 200 mph, global glamour and team drama.",
        "description": [
            "Formula 1 is the highest level of single-seat auto racing. About 20 drivers race purpose-built cars, among the most advanced machines on Earth, around tracks and city streets worldwide, from Monaco to Las Vegas.",
            "It's a team sport as much as a driving one. Each team builds its own car, and engineering, strategy and pit stops matter as much as the driver. Netflix's <i>Drive to Survive</i> introduced millions of new fans to the sport.",
        ],
        "facts": [("Competitors", "10–11 teams with 2 drivers each"), ("Race length", "About 305 km, roughly 1.5–2 hours"), ("Season", "March to December, about 24 races"), ("Prize", "The Drivers' and Constructors' (team) championships")],
        "rules": [
            "Each race weekend has practice, then <b>qualifying</b>: a fastest-lap shootout that sets the starting order (the <b>grid</b>). First place is <b>pole position</b>.",
            "The top 10 finishers earn points, with <b>25</b> for a win. Points add up over the season.",
            "Two titles are decided: the <b>Drivers' Championship</b> for the best driver and the <b>Constructors' Championship</b> for the best team.",
            "Cars must make at least one <b>pit stop</b> to change tires. Tire choice and timing is a key strategy.",
            "Flags: yellow means danger, slow down. Red means the race is stopped. Checkered means the finish. A <b>safety car</b> slows the field after crashes.",
            "Teammates drive identical cars, so your teammate is also your biggest rival.",
        ],
        "leagues": [("Formula 1", "The top international series."), ("Formula 2 / Formula 3", "Junior series where future F1 drivers come from."), ("IndyCar", "America's open-wheel series, home of the Indianapolis 500."), ("NASCAR", "American stock-car racing, hugely popular in the US South."), ("F1 Academy", "A series for female drivers.")],
        "teams_title": "Famous teams",
        "teams": [("Ferrari", "The oldest and most iconic team. Its passionate fans are called the <i>tifosi</i>."), ("Mercedes", "Won eight straight Constructors' titles from 2014 to 2021."), ("Red Bull Racing", "Energy drink company turned title-winning powerhouse."), ("McLaren", "A historic British team, back at the front in the mid-2020s."), ("Williams", "A legendary independent team with nine Constructors' titles.")],
        "players": [("Lewis Hamilton", "British driver with 7 world titles, a record he shares. Joined Ferrari in 2025."), ("Michael Schumacher", "German legend with 7 titles, mostly with Ferrari."), ("Ayrton Senna", "Brazilian icon, considered by many the most naturally gifted ever."), ("Max Verstappen", "Dutch driver who dominated the early 2020s with Red Bull."), ("Lando Norris", "Popular British driver for McLaren."), ("Charles Leclerc", "Monaco-born Ferrari star.")],
        "lingo": [("Pole position", "Starting first."), ("Undercut", "Pitting earlier than a rival to gain time on fresh tires."), ("DNF", "Did Not Finish."), ("Paddock", "The behind-the-scenes area where teams, celebrities and VIPs gather.")],
        "smart": "“It's all about tire management.” This is true in nearly every race.",
    },
    {
        "slug": "rugby",
        "name": "Rugby",
        "emoji": "🏉",
        "color": "#4527a0",
        "tagline": "Football's tougher cousin: no pads, only backward passes.",
        "description": [
            "Rugby, here meaning rugby union, the most popular version, is a full-contact game where two teams of 15 carry, pass and kick an oval ball toward the opponent's goal line. The play flows continuously, and the players wear no helmets or pads.",
            "It's a national passion in New Zealand, South Africa, Wales, Ireland, France, England, Fiji and Argentina. Despite the brutal hits, rugby is famous for its sportsmanship: players respect the referee and shake hands after the game.",
        ],
        "facts": [("Players", "15 per team (7 in Olympic “rugby sevens”)"), ("Game length", "2 halves × 40 min"), ("Season", "Roughly September to June in Europe"), ("Biggest events", "The Rugby World Cup and the Six Nations")],
        "rules": [
            "You can run with the ball or kick it forward, but you can only <b>pass backward</b> (or sideways).",
            "<b>Try</b> (touch the ball down over the opponent's goal line): 5 points. Unlike in American football, you must ground it.",
            "<b>Conversion</b> (a kick through the posts after a try): 2 points. <b>Penalty kick</b> or <b>drop goal</b>: 3 points.",
            "When a player is tackled, they must release the ball, and both teams compete for it in a <b>ruck</b>.",
            "A <b>scrum</b> (the big pushing huddle) restarts play after minor mistakes. A <b>lineout</b> restarts it when the ball goes out the side.",
            "Tackles must be below the shoulders. Dangerous play can get a yellow card (10 minutes off) or a red card.",
        ],
        "leagues": [("Rugby World Cup", "Every four years. The biggest event in the sport."), ("Six Nations", "Yearly tournament: England, France, Ireland, Italy, Scotland and Wales."), ("The Rugby Championship", "Southern hemisphere: New Zealand, South Africa, Australia and Argentina."), ("Super Rugby / Premiership / Top 14", "Top club leagues in the southern hemisphere, England and France."), ("Rugby League (NRL)", "A related 13-a-side sport, huge in Australia.")],
        "teams_title": "Famous teams",
        "teams": [("New Zealand “All Blacks”", "Legendary winners who perform the haka war dance before games."), ("South Africa “Springboks”", "Four-time World Cup winners, a record."), ("England", "Won the 2003 World Cup."), ("Ireland", "A top-ranked side in recent years."), ("Toulouse", "France's most decorated club.")],
        "players": [("Jonah Lomu", "Giant, unstoppable All Blacks winger who made rugby a global spectacle."), ("Richie McCaw", "All Blacks captain who won two World Cups."), ("Dan Carter", "Perhaps the best fly-half (playmaker and kicker) ever."), ("Siya Kolisi", "South Africa's first Black Test captain, and a two-time World Cup winner."), ("Antoine Dupont", "French scrum-half, considered the best player in the world today.")],
        "lingo": [("Try", "Rugby's touchdown."), ("Haka", "The Māori challenge the All Blacks perform before kickoff."), ("Knock-on", "Dropping the ball forward. That gives a scrum to the other team."), ("Sin bin", "10 minutes off the field after a yellow card.")],
        "smart": "“The game is won up front.” It means the big forwards in the scrum decide matches.",
    },
]

THEME_TOGGLE = """<button class="theme-toggle" type="button" aria-label="Toggle dark mode" onclick="(function(){var r=document.documentElement;var d=r.dataset.theme==='dark'||(!r.dataset.theme&&matchMedia('(prefers-color-scheme: dark)').matches);r.dataset.theme=d?'light':'dark';try{localStorage.setItem('theme',r.dataset.theme)}catch(e){}})()">◐</button>"""
THEME_INIT = "<script>try{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}catch(e){}</script>"


def page(title, body, css_path, description, home_href):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="stylesheet" href="{css_path}">
{THEME_INIT}
</head>
<body>
<header class="site-header">
  <a class="brand" href="{home_href}"><span aria-hidden="true">🏟️</span> {SITE}</a>
  {THEME_TOGGLE}
</header>
{body}
<footer class="site-footer">
  <p>{SITE}: a friendly guide for the sports-curious. No prior knowledge required.</p>
</footer>
</body>
</html>
"""


def items(pairs):
    return "\n".join(f"<li><strong>{e(n)}</strong><span>{d}</span></li>" for n, d in pairs)


def sport_page(i, s):
    prev_s = SPORTS[i - 1]
    next_s = SPORTS[(i + 1) % len(SPORTS)]
    desc = "\n".join(f"<p>{p}</p>" for p in s["description"])
    facts = "\n".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in s["facts"])
    rules = "\n".join(f"<li>{r}</li>" for r in s["rules"])
    lingo = "\n".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in s["lingo"])
    body = f"""<main class="sport" style="--accent:{s['color']}">
  <nav class="crumbs"><a href="../index.html">← All sports</a></nav>
  <section class="hero">
    <div class="hero-emoji" aria-hidden="true">{s['emoji']}</div>
    <div>
      <h1>{e(s['name'])}</h1>
      <p class="tagline">{e(s['tagline'])}</p>
    </div>
  </section>

  <dl class="facts">{facts}</dl>

  <section class="block">
    <h2>What is it?</h2>
    {desc}
  </section>

  <section class="block">
    <h2>The basic rules</h2>
    <ol class="rules">{rules}</ol>
  </section>

  <div class="two-col">
    <section class="block">
      <h2>Major leagues &amp; competitions</h2>
      <ul class="list">{items(s['leagues'])}</ul>
    </section>
    <section class="block">
      <h2>{e(s['teams_title'])}</h2>
      <ul class="list">{items(s['teams'])}</ul>
    </section>
  </div>

  <section class="block">
    <h2>Famous names to know</h2>
    <ul class="players">{items(s['players'])}</ul>
  </section>

  <section class="block">
    <h2>Lingo you'll hear</h2>
    <dl class="lingo">{lingo}</dl>
  </section>

  <aside class="smart">
    <h2>💬 Sound smart at a party</h2>
    <p>{e(s['smart'])}</p>
  </aside>

  <nav class="pager">
    <a href="{prev_s['slug']}.html">← {prev_s['emoji']} {e(prev_s['name'])}</a>
    <a href="{next_s['slug']}.html">{next_s['emoji']} {e(next_s['name'])} →</a>
  </nav>
</main>"""
    return page(f"{s['name']} | {SITE}", body, "../styles.css", s["tagline"], "../index.html")


def index_page():
    cards = "\n".join(
        f"""<a class="card" href="sports/{s['slug']}.html" style="--accent:{s['color']}">
  <span class="card-emoji" aria-hidden="true">{s['emoji']}</span>
  <h2>{e(s['name'])}</h2>
  <p>{e(s['tagline'])}</p>
  <span class="card-cta">Learn the basics →</span>
</a>"""
        for s in SPORTS
    )
    body = f"""<main>
  <section class="intro">
    <h1>Sports, explained for the rest of us.</h1>
    <p>Got dragged to a game? Your coworkers won't stop talking about the playoffs? Pick a sport below for a plain-English overview of what it is, how it works, and the names everyone keeps mentioning.</p>
  </section>
  <section class="grid">
{cards}
  </section>
</main>"""
    return page(SITE, body, "styles.css", "Plain-English guides to the world's major sports.", "index.html")


def main():
    (ROOT / "index.html").write_text(index_page(), encoding="utf-8")
    out = ROOT / "sports"
    out.mkdir(exist_ok=True)
    for i, s in enumerate(SPORTS):
        (out / f"{s['slug']}.html").write_text(sport_page(i, s), encoding="utf-8")
    print(f"Built index.html and {len(SPORTS)} sport pages.")


if __name__ == "__main__":
    main()
