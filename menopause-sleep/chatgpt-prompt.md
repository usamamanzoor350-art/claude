You are a senior product designer and front-end developer who specializes in calm, sleep-focused digital experiences. Build me a complete, working digital product in ONE self-contained HTML file (HTML + CSS + JavaScript inline, no external images, no frameworks; Google Fonts allowed).

## The product
**Name:** Softly to Sleep
**Headline on the welcome screen:** "Softly to Sleep"
**Sub-headline:** "Nothing to track. Nothing to fix. Just a slow, quiet way back to sleep."
**Audience:** American women aged 50+ in perimenopause or post-menopause who struggle to fall asleep, wake every couple of hours, or wake around 3 AM. They open this on their phone, in bed, with the lights off, instead of scrolling social media.

## The single most important rule
This product must CALM the brain, never activate it.
- NO trackers, logs, diaries, scores, charts, statistics or sleep data of any kind.
- NO to-do lists, journaling prompts, quizzes, decisions or anything that makes her think or plan.
- NEVER mention her problems, symptoms, insomnia, hormones or "what's wrong". She already knows.
- Only gentle, positive, beautiful, dreamy, slow things that lead her toward closing her eyes.

## Experience structure
Show ONE scene at a time, full screen, with no page scrolling. Scenes fade into each other slowly (about 1.5 seconds). A tiny row of dots at the bottom shows progress (no numbers).

**Welcome screen**
- Headline, sub-headline
- "Tonight's place" picker with 4 places (see below); remember the last choice
- Two path buttons:
  1. "Wind down for bed" (about 15 minutes)
  2. "Back to sleep" (about 5 minutes, for waking in the night)

**Path 1, Wind down for bed:** Settle in → Breathe with the moon → Color the picture → Place activity → Imagination journey → Drift → Goodnight
**Path 2, Back to sleep:** Settle back in → Breathe with the moon → Drift → Goodnight

### Scene details
1. **Settle in**: 5 soft lines appear one at a time, about 6.5 seconds apart, older lines fading to 30% opacity. Example: "The day is done." / "Whatever happened today, you did enough." / "Let your shoulders drop, just a little." / "Let your jaw go soft." / "There is nowhere you need to be now."
   The "Back to sleep" version: "Hello again." / "You don't need to know what time it is." / "Let the pillow hold your head." / "Rest is still rest, even with your eyes open." / "Let's go slowly back down."
2. **Breathe with the moon**: a softly glowing moon grows for 4 seconds ("Breathe in, slowly…") and shrinks for 6 seconds ("And out, longer and softer…"), on a loop.
3. **Color the picture**: an SVG illustration of the chosen place, with 10–12 tappable regions. She picks from 9 soft colors and taps a region; it fills with a slow 1.4-second fade. Caption: "There's no wrong color." Remember her colors per place.
4. **Place activity**: one gentle canvas interaction per place (see below).
5. **Imagination journey**: 10 slow lines, same line-by-line style. Every journey includes a COOL sensation (cool air, cool water, cool sand, a breeze), because many women in menopause feel hot at night.
6. **Drift**: one gentle image phrase appears every 9 seconds with a slow cross-fade ("a sleeping cat", "a lantern in a window"…), randomized from 30–40 phrases per place. Above the button, the caption: "Feeling sleepy? Just close your eyes. If you drift off, the screen will dim and go dark on its own." Button: "I'm getting sleepy".
7. **Goodnight**: "Now close your eyes." in large italic text, then "Put the screen down. Sleep will find you." The text slowly fades and the whole screen dims to nearly black.

### The 4 places
| Place | Coloring picture | Activity | Imagination journey | Sound |
|---|---|---|---|---|
| Quiet Valley | moon, hills, small cottage with a lit window, pine trees, still lake | **Light the stars**: 9 dim stars; tapping each one makes it glow and draws a faint line to the previous one, and a soft word appears (soft, still, warm, safe, slow, quiet, easy, gentle, rest) | a cool, still lake at night | soft rain |
| Snowy Cabin | snowy mountains, cabin, chimney, two lit windows, pines, snow path | **Let the snow fall**: tapping the sky releases slow snowflakes that drift with a sway and pile softly on the ground | crisp cool air through a slightly open window, silent snow | soft wind |
| Ocean Night | moon and its reflection, sea, wave, sand, lighthouse, rocks, shell, starfish | **Draw in the cool sand**: finger drawing leaves soft glowing lines that the tide slowly erases over about 7 seconds | cool sand, breathing with the waves, a distant lighthouse | soft waves (noise with a slow swell) |
| Lavender Field | moon, hills, tree, farmhouse, rows of lavender, a lane | **Gather the fireflies**: about 12 fireflies wander and blink; tapping one makes it float slowly into a glass jar that glows brighter with each one | lavender at dusk, cool evening breeze | evening breeze |

Each activity shows a gentle encouraging word after a few taps, and a closing line when complete (e.g. "Your sky is full. Rest here a moment."). There is no failing, no timer and no score.

### Controls (top corners, small and quiet)
- **Sound button**: generate the sound in the browser with the Web Audio API (filtered noise; no audio files). Fade in over 3 seconds. Only start after a tap.
- **Dim screen button**: 3 levels of a black overlay (0%, 35%, 60%).
- **Start over** button (hidden on the welcome screen).

### Falling asleep automatically
- If she doesn't touch the screen for 3 minutes during Drift, go to Goodnight on its own.
- On Goodnight, dim the screen to 60% after 12 seconds and to 90% after 1 minute.
- If sound is on, fade it out over 90 seconds after 20 minutes (sleep timer), and tell her so on the Goodnight screen.

## Visual design
- A deliberately dark, warm, LOW-BLUE night palette: deep plum-indigo backgrounds (around #17131F), warm moonlight text (around #EBDDC2), and a soft amber glow. Each place shifts only the glow color (snow: pale silver, ocean: soft sea-green, lavender: lilac).
- No pure white and no bright blue anywhere, so it is gentle on eyes adjusted to the dark.
- Typography: an elegant serif such as Cormorant Garamond for headlines and calm lines (italic for cues), and a soft rounded sans such as Nunito for small text. Base size 19px, large and readable for women over 50.
- A few faint stars scattered in the background.
- Beautiful, hand-crafted SVG/canvas illustrations: soft, simple, storybook style.
- Large tap targets, mobile-first, works at 375px width with no horizontal scroll. Respect `prefers-reduced-motion` and the phone's safe-area insets.

## Tone of all words
Warm, slow, kind, second person, very short sentences. Like a gentle friend reading a bedtime story. No medical claims and no exclamation marks.

## Deliverable
1. The complete single HTML file, ready to open on a phone.
2. A short list of everything that is interactive.
3. One illustrated cover image for the product (mockup of the welcome screen on a phone, dark cozy bedroom setting) for an Etsy listing.
