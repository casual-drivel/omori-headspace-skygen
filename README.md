**README.md**

```markdown
# Noto Emoji Wallpaper Generator 🎉

Welcome to the **Noto Emoji Wallpaper Generator**, the ultimate meme‑powered tool for turning your screen into a kaleidoscope of emojis, stars, and custom color schemes! 🚀✨

## What’s This All About?

- **💥 Random Emoji Spread** – Let the emojis dance across your display like a TikTok trend.  
- **🖌️ Color & Background Schemes** – Choose a vibe (solid color + background *or* an epic preset scheme) – you can’t mix them, but that’s just to keep things tidy.  
- **⭐ Star‑tastic Overlays** – Sprinkle random stars over the empty spaces for that “galaxy vibes” look.  
- **🛠️ Easy CLI** – All options are handled via `argparse` (resolution, emojis list, color, background, scheme).  

## Core Components

| File | Role |
|------|------|
| **`argument.py`** | Handles CLI arguments with sanity checks (`color+bg` vs. `scheme`). |
| **`engine.py`** | The brain of the app – initializes functions, renders emojis (fillscreen or spread), handles events, and drives the main loop. |
| **`gui.py`** | Simple Pygame GUI for color picking (future sliders coming soon). |
| **`main.py`** | Entry point – sets up the `Engine`, runs the game loop, and quits gracefully. |
| **`notoFillscreen.py`** | Minimal rendering stub that prints three default characters (placeholder for full Noto implementation). |
| **`notoSpread.py`** | The heavy‑lifting class: creates emoji surfaces, spaces them out, adds stars, and can rotate emojis for extra flair. |

## How to Run

```bash
python main.py -r 1920x1080 -e "🖤 🖤 ❤ ⬛︎" -c "#ff69b4" -b "#000000"
# or use a preset scheme:
python main.py -s "galaxy"
```

> **Note:** You can’t specify both `-c/-b` *and* `-s`. The script will politely exit with a meme‑style warning if you try.

## Example Output

![example1.png](./example1.png)

*(That’s your screen now looking like a fresh TikTok feed of emojis and stars!)*

## Future Roadmap (Because we’re always vibing)

- **🔧 Slider Widgets** – Add real-time sliders for color/alpha tweaks.  
- **📱 Mobile‑Friendly Mode** – Make it work on phones via Kivy or PyGame mobile builds.  
- **🖼️ Emoji Picker UI** – Drag‑and‑drop your favorite emojis into the canvas.  

---

*Made with love, memes, and a sprinkle of nostalgia—just like that one‑second video you can’t stop replaying.* 🎈

--- 

Feel free to fork, contribute, or just brag about your new wallpaper on Discord! 🚀💬