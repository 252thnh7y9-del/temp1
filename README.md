# Sports for Non-Sports People

A fully static website (plain HTML and CSS, no JavaScript, no build step) that explains the major sports in plain English. It's ready to host on GitHub Pages.

- `index.html`: the homepage, listing every sport
- `sports/*.html`: one page per sport, with a description, basic rules, major leagues, famous teams and players, and common lingo
- `styles.css`: shared styling (dark mode follows your device setting)

To edit content, open the sport's HTML file and change the text directly. To add a sport, copy an existing page in `sports/`, edit it, and add a card for it in `index.html`.

## Publishing on GitHub Pages

In the repository, go to **Settings → Pages**, choose **Deploy from a branch**, and pick the branch and the `/ (root)` folder.
