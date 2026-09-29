# Birthday Universe: Cinematic Homepage Blueprint

How each homepage section should look and move, what visual it needs, and which AI makes it.
The words for each section are in `brand-story-and-homepage-copy.md`.

**The big idea:** the whole homepage tells the "Her Turn" story as you scroll down.
Dark, warm, candle-lit at the top (the moment before the surprise), then brighter and more colorful as you scroll (the party).

---

## Look & feel

| | Choice | Why |
|---|---|---|
| **Colors** | Midnight plum `#241B33` · Candle gold `#E3B25B` · Blush pink `#F4C7D0` · Cream `#FBF6EF` | Plum + gold = "universe" and night-time surprise. Pink ties to your best-selling pink tees. |
| **Headline font** | *Young Serif* or *Gloock* (Google Fonts, free) | Warm, elegant, a bit nostalgic, which suits women 50+. |
| **Body font** | *Instrument Sans* or *DM Sans* | Clean and easy to read on a phone. |
| **Motion** | Slow and soft: fade-ups on scroll, gentle hover lift, one confetti burst on signup | Cinematic means *slow and smooth*, not busy. |
| **Phone first** | Design every section at phone width first | Nearly all traffic comes from Facebook and Instagram on phones. |

---

## Section by section

### 1. Hero: "Her Turn" video (full-screen)
**Display:** a full-width looping video with a soft dark gradient at the bottom. The headline and buttons sit *on top* of the video as real text (not baked into the video), so they stay sharp and editable.

**Recommended headline (new, matches the story):**
> # It's her turn.
> Birthday shirts & gifts for the woman who celebrates everyone.
> **[Shop by birthday]**  **[Shop gifts for Mom]**

**Video specs:**
- Two versions: **9:16 for phone** and **16:9 for desktop** (Shopify's video section can show a different video on mobile)
- 6–8 seconds, seamless loop, **no sound**, MP4
- Compress to **under 4 MB** (use HandBrake, or CapCut export at 1080p) so the page stays fast
- Export the first frame as a JPG "poster" image, which shows while the video loads

**AI:** Omni Flash (first choice). Higgsfield as a backup if Omni Flash struggles with faces.

**Omni Flash prompt: hero video (attach the pink "hello FIFTY" or "Hello 60" tee image as reference):**
```
Cinematic 8-second seamless loop, [9:16 vertical / 16:9 widescreen], shot like a
premium perfume commercial. Warm, dark, candle-lit living room at night. Shallow depth
of field, soft golden bokeh from string lights, slow gentle camera push-in, 24fps film
look, rich warm tones of plum, gold and blush pink.

A graceful American woman in her early 60s with silver-blonde hair sits at a dinner
table. Many loving hands (family, different ages) slide a gift box toward her. She
opens it slowly and lifts out a soft pink T-shirt (exactly matching the attached
reference image: same pink color and black print). She presses the shirt to her chest,
eyes shining, laughing with pure joy. Gold confetti drifts down in slow motion through
the candlelight. End on the same framing as the first frame so the video loops smoothly.

No text on screen, no logos, no watermark. Natural, realistic faces and hands, elegant
and emotional, not cheesy.
```
*If the shirt print comes out wrong, that's OK here: the shirt can be folded or turned slightly, because the hero is about her reaction, not the print. The product close-ups come later in the page.*

---

### 2. "What birthday are we celebrating?" (age picker)
**Display:** a cream background (the lights just came on). A row of big round number buttons: **30 · 40 · 50 · 55 · 60 · 65 · 70 · 75 · 80+**. On a phone they scroll sideways like story bubbles. Tapping a number opens that age's collection. On hover or tap, the number lifts and a tiny gold sparkle appears.

**AI:** none needed. **I write the code** (a custom Shopify section you paste in), and I set up the age collections through the Shopify connector.

---

### 3. Order-by banner
**Display:** a thin gold strip: *"Birthday on Oct 18? Order by Oct 8."* with a small calendar icon.

**AI:** none. A delivery-date app later; until then, **I write a small section** you update weekly.

---

### 4. "Who's the birthday star?" (5 photo cards)
**Display:** 5 tall photo cards (For Mom · Grandma · Best Friend · For Me · The Whole Crew). On a phone, swipe sideways. Each card has a subtle slow zoom when it comes into view.

**AI:** Google image generation (Nano Banana / Imagen in Gemini or Google AI Studio). Attach the real shirt image as a reference. Optional: turn each into a 3-second moving photo with Omni Flash.

**Image prompts (all 4:5 vertical, warm natural light, candid lifestyle photography, no text or logos):**
- **For Mom:** *Adult daughter hugging her smiling mother in her 60s in a sunny kitchen, the mother wearing the attached pink birthday T-shirt, balloons softly out of focus behind them.*
- **For Grandma:** *Joyful grandmother in her late 70s wearing a small gold party crown and the attached charcoal "Queen" T-shirt, grandchildren laughing around her at a garden party.*
- **For My Best Friend:** *Two women in their 50s laughing together at a brunch table, clinking mimosa glasses, both wearing matching birthday T-shirts.*
- **For Me:** *Confident woman in her mid-50s walking down a city sidewalk in golden-hour light, wearing the attached birthday T-shirt with jeans and sunglasses, carrying a small gift bag, big carefree smile.*
- **The Whole Crew:** *Group of six women in their 50s and 60s in matching birthday T-shirts posing and laughing at a restaurant, one blowing out candles on a cake.*

---

### 5. Best sellers
**Display:** a product grid (2 columns on a phone, 4 on desktop). Each card shows a flat-lay photo first, then a photo of the shirt worn on hover or swipe. Small badges: `Best seller` · `Most gifted`.

**AI:** Google image generation to put each real shirt design on a model. Keep the real flat-lay mockups as the *first* image, since that one shows the true print.

---

### 6. "Her Turn" story section (the emotional moment)
**Display:** back to dark plum for one full-screen moment. On the left or top, a slow cinematic clip; on the right or below, the short story text fades in line by line as you scroll. Ends with **[Read her story]**.

**AI:** Omni Flash.
```
Cinematic 6-second clip, [9:16 / 16:9], dark warm room lit only by birthday candles.
Close-up of an elegant woman in her 60s, her face glowing in candlelight, family
blurred in the background. She closes her eyes, smiles softly, makes a wish and gently
blows out the candles. Soft smoke curls up in slow motion. Film look, shallow depth of
field, plum and gold tones. No text, no logos. Seamless loop.
```

---

### 7. Real birthdays (reviews)
**Display:** a sideways-scrolling strip of customer photos with a short quote each.

**AI:** **none. Real customers only.** Since this is a new store, hide this section at launch and switch it on once the first real reviews and photos arrive (the post-purchase email will ask for them).

---

### 8. Squad pack
**Display:** one wide image of the "whole crew" with the text beside it and a **[Build your squad pack]** button.

**AI:** Google image generation (the "Whole Crew" prompt above, in 16:9).

---

### 9. Our promises
**Display:** three simple gold line icons in a row: gift box, chat bubble, size tag. Short text under each.

**AI:** none. Use simple icons (I can provide clean SVG icons in the code).

---

### 10. Birthday reminder signup
**Display:** plum background, gold button. When she submits, a small confetti burst plays and the success message appears.

**AI:** none. A Klaviyo signup form; **I write the confetti code and the reminder email.**

---

### 11. Footer
**Display:** cream, simple, with the tagline *"For the one who celebrates everyone."*

---

## Build order (what we do together, one by one)

| # | Step | Who | Tool |
|---|---|---|---|
| 1 | Approve the "Her Turn" story + hero headline | You | — |
| 2 | Generate the hero video (both sizes) with the prompt above | You | Omni Flash |
| 3 | Send me the video; I check it and give fixes/re-prompts | Together | — |
| 4 | Generate the 5 "birthday star" images + squad image | You | Google image AI |
| 5 | Install the theme on the new store, set colors & fonts | You, with my step-by-step | Shopify |
| 6 | Custom sections: age picker, order-by banner, story scroll, promises | Claude | Shopify Liquid code |
| 7 | Upload videos & images, paste the copy | You | Shopify |
| 8 | Phone speed test and final polish | Together | — |

**Before step 5, tell me:**
1. Is the new store a **new Shopify account**, or the same account with a new domain?
2. Which **theme** is installed (Dawn, Horizon, or something else)?
