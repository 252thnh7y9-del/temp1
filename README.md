# Sports for Non-Sports People

A static website that explains the major sports in plain English. The homepage lists each sport, and each sport has its own page with:

- a description of the sport
- the basic rules
- major leagues and competitions
- famous teams (or big events)
- famous players
- lingo and a "sound smart at a party" line

## Viewing

Open `index.html` in a browser, or serve the folder with any static host (for example GitHub Pages). There is no build step needed to view it.

## Editing content

All sport content lives in the `SPORTS` list in `build.py`. After editing it, regenerate the pages:

```sh
python3 build.py
```

This rewrites `index.html` and `sports/*.html`. Styling is in `styles.css`.
