# Vibe-coding a better Spotify homepage

*Source: https://wow.pjh.is/journal/vibe-spotify*  ·  *Published: 2025-11-03*

---

The Spotify homepage doesn't do it for me. There's too much choice, an advert at the top, playlists, podcasts, audiobooks... and somehow their recommendations rarely hit.

**Most of the time, what I actually want is a physical table with about 10 records on it.** Some should be familiar, others new.

So I made an app. To start, it crawled \~2000 songs from my playlists, then saved the \~800 unique artists to a database. Now, once a day, the app takes nine random artists from that database, looks up all of their albums on Spotify, and picks one at random.

Here's today's selection:

It's not a physical table with physical records—I travel too much for that. But by `build time : Hartree utilons`, it's my most successful vibe-coding project so far.

Want a copy of the codebase? [Email me](mailto:wow@pjh.is).

Or you can just [try something from the table](https://vibe.pjh.is/records).
