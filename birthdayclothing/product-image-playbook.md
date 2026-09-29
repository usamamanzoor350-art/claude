# Birthday Universe: Product Image Playbook

How every product page should look, so a shopper instantly understands *"this is how it will look on me"*,
and so nobody recognises the old store's photos.

---

## 1. The big rule: never ask AI to write the print

AI image tools (ChatGPT, Gemini, etc.) often misspell or change text and numbers. With ~400 products that differ only by the age ("Hello 58", "Hello 63"…), that is a disaster: one wrong number and the customer gets a shirt that doesn't match the photo.

**So we split the work in two:**

| Job | Tool | Why |
|---|---|---|
| Make the **scene**: model, blank shirt in each color, background, props, light | **ChatGPT images** | AI is great at people, light and mood |
| Put the **real design** on the shirt | **Canva** (or your vendor's mockup generator) | The design file is pasted exactly, so every letter and number is correct |

You make each scene **once**, then reuse it for every age by swapping the design file. That's how 400 products become possible before Q4.

> **Check first:** if your vendor is a print-on-demand company (Printful, Printify, Gelato, etc.), their mockup generator already puts your exact design on real model photos in every color. Use it for the variant images and save AI for the lifestyle shots.

---

## 2. New look vs old look (so customers see a new brand)

| Old store | Birthday Universe |
|---|---|
| Wooden floor, jeans, fake flowers flat lays | **Cream or plum seamless background** with gold confetti, candles, a gift box, a tiny gold star |
| Mostly flat lays, no people | **Real-looking women of the right age wearing the shirt** (a 60-something model for Hello 60) |
| Random crops and lighting | **One style everywhere:** 4:5 portrait, warm soft light, same backdrop per image type |
| Colors shown one by one | **One "6 colors" grid image** + color swatches that change the photo |

Keep this style identical across every product. Consistency is what makes a store look like a brand.

---

## 3. The image set for every shirt (8 images)

Order matters: the first image shows on collection pages and in ads.

| # | Image | What it shows | Made with |
|---|---|---|---|
| **1** | **On-model hero** | A woman of the right age wearing the shirt in the best-selling color (Light Pink for Hello), waist-up, smiling, cream backdrop | ChatGPT scene + Canva design |
| **2** | **Styled flat lay** | The shirt laid flat on cream, with gold confetti, a small gift box and a birthday candle. The print must be 100% readable | ChatGPT scene + Canva design |
| **3** | **Print close-up** | Tight crop of the print on fabric: shows quality and exact wording | Crop of image 2 |
| **4** | **"Available in 6 colors" grid** | All 6 colors folded side by side (or 2×3 grid), each with its name underneath | Canva template |
| **5** | **Second model, different body type** | A curvy/plus-size woman in a different color, so shoppers see the fit on a body like theirs | ChatGPT scene + Canva design |
| **6** | **Birthday moment** | Lifestyle: birthday dinner, candles, family or friends around her | ChatGPT scene + Canva design |
| **7** | **Size & fit card** | Size chart + "Model is 5'6" and wearing M" + "Between sizes? Size up" | Canva template |
| **8** | **Complete the look** | Shirt with the crown, socks and tote: the add-ons from the product page | Canva template |

**Plus one image per color (6 images), linked to the color variants.**
When a shopper taps the Navy swatch, the gallery jumps to the navy shirt. Use the on-model photo (best) or the flat lay for each color.

So one product = **8 shared images + 6 color images = 14 images**, but only the design changes between products, so almost everything is reused.

---

## 4. The 6 colors: how to show them well

**Your colors:** White · Light Pink · Sand · Charcoal Gray · Navy Blue · Black

1. **Ink color per shirt color.** Black print on light shirts (White, Light Pink, Sand); white print on dark shirts (Charcoal, Navy, Black). The "Queen is 79" on charcoal already does this. You need **two versions of every design file**: black ink and white ink.
2. **Swatch circles** on the product page (not a dropdown), in this order: Light Pink, White, Sand, Charcoal Gray, Navy Blue, Black.
3. **Link each color variant to its image** in Shopify (Product → Variants → click the image). Then the swatch changes the photo.
4. **Collection cards** show small swatch dots under each product so people see "6 colors" before they click.
5. **Same color names everywhere.** Right now the store mixes "Pink" / "Light Pink" and "Grey" / "Charcoal Gray" across products. Pick one name per color, or the swatches and filters break.
6. **You don't need every image in every color.** Hero, lifestyle and model shots can each use a different color; that shows variety naturally. Only the 6 variant images need to cover all colors.

---

## 5. ChatGPT prompts (make these scenes ONCE, reuse forever)

**Always attach:** one photo of your blank shirt (or your current flat lay) so the shirt shape and neckline match.
**Always add at the end of every prompt:**
> *The T-shirt front must be completely blank, with no text, logo or print. Keep the shirt front flat, facing the camera and not covered by hair, hands or objects. Photorealistic, 4:5 portrait, 2000×2500.*

### A. On-model hero (make 6: one per color)
```
Photorealistic e-commerce photo, waist-up, of a warm, confident American woman in her early
60s with shoulder-length silver-blonde hair, natural makeup and a genuine happy smile, wearing
a plain [LIGHT PINK] crew-neck women's T-shirt tucked loosely into light-wash jeans. Seamless
warm cream studio background (#FBF6EF), soft diffused window light from the left, a few blurred
gold confetti pieces in the foreground. Shot on 85mm lens, shallow depth of field, clean and
premium.
```
*Make versions for different ages to match your collections: late 30s (for 40th), about 50,
about 60, about 70. Same scene, same light, so everything looks like one photoshoot.*

### B. Styled flat lay (make 6: one per color)
```
Top-down flat lay of a plain [NAVY BLUE] women's crew-neck T-shirt, neatly laid out and
slightly styled with the sleeves folded in, on a warm cream seamless paper background. Around
it: scattered gold confetti, a small white gift box with a gold satin ribbon, one lit gold
birthday candle and a tiny gold star. Soft even light, gentle natural shadows, luxury
gift-brand look.
```

### C. Second model, curvy (make 2–3)
```
Photorealistic e-commerce photo, waist-up, of a joyful curvy plus-size American woman in her
50s with dark curly hair, laughing, wearing a plain [CHARCOAL GRAY] crew-neck T-shirt that fits
comfortably, with dark jeans. Same warm cream studio background and soft light as a premium
clothing brand catalog.
```

### D. Birthday moment (make 4–5, different colors and scenes)
```
Candid lifestyle photo at a warm, candle-lit birthday dinner at home. A delighted woman in her
60s wearing a plain [BLACK] crew-neck T-shirt sits at the table as her family (adult daughter,
grandchildren) cheers around her; a birthday cake with lit candles is in front of her. Warm
golden light, soft bokeh from string lights, gold confetti in the air. Real, joyful,
not posed. The woman faces the camera so her T-shirt front is clearly visible.
```
Other scenes to rotate: brunch with best friends (matching shirts) · backyard party with balloons · cruise ship deck at sunset · opening a gift box on the couch.

### E. Color grid base
```
Six plain women's crew-neck T-shirts neatly folded into identical squares and arranged in a
single row on a warm cream background, in this order left to right: light pink, white, sand,
charcoal gray, navy blue, black. Top-down view, soft even light, lots of empty space below the
row for labels.
```

**Tip:** if ChatGPT changes the shirt color, add *"exact color HEX [#...]"* and attach a photo of the real shirt in that color.

---

## 6. Canva: putting the real design on the shirt

**Set up once:**
1. Create a **Brand Kit**: colors (plum `#241B33`, gold `#E3B25B`, blush `#F4C7D0`, cream `#FBF6EF`), fonts (Young Serif, Instrument Sans) and logo.
2. Create one design at **2000 × 2500 px** for each scene (hero, flat lay, lifestyle…).
3. Put the ChatGPT scene as the background and lock it.
4. Place your **design PNG (transparent background)** on the shirt chest:
   - Size it the same as the real print (roughly the width of the chest, from armpit to armpit minus about a hand's width).
   - Set transparency to about **92–95%** so fabric texture shows through slightly and it looks printed, not pasted.
   - Rotate it a tiny bit if the shirt is angled.
5. Save each of these as a **Template** ("Hero – Light Pink", "Flat lay – Navy", etc.).

**For every product after that:**
1. Open the template → **Replace** the design PNG with the new age (e.g. Hello 63) → export.
2. A few seconds per image. With **Canva Bulk Create** (Canva Pro), you can connect a folder of design PNGs and make all ages at once.

**Canva-only templates (no AI needed):**
- **6-color grid:** the grid base + the design on each shirt + color names in Instrument Sans
- **Size & fit card:** size chart table, model info, "Between sizes? Size up", Birthday Universe logo
- **Complete the look:** shirt + crown + socks + tote on cream, with prices
- **Collection banners** for Hello, Queen, Vintage, Sassy and each age

**Export:** JPG, quality ~80, under 500 KB each. File name example: `hello-60-birthday-shirt-light-pink-hero.jpg` (good for Google too).

---

## 7. Other product types

| Product | Key images |
|---|---|
| **Sweatshirts** | On-model in a cozy autumn setting (Q4!), flat lay, close-up of the fabric, color grid, size card |
| **Tank tops** | On-model outdoors (pool/vacation/cruise), flat lay, color grid, size card |
| **Tote bags** | Carried on the shoulder, flat lay with gift items spilling out, "how big is it" photo next to a phone/book |
| **Socks** | Worn with sneakers, in a gift box, pair laid flat |
| **Crown / Hat** | Worn by a smiling woman at a party, close-up detail, "one size fits most" card |
| **Birthstone necklace** | Close-up worn on neck, all 12 months grid, gift box shot |
| **Photo collage printable** | Example filled with real-looking family photos, "how it works in 3 steps" card, framed on a party table |

---

## 8. Honesty rules (they protect the new brand)

- The print, colors and shirt style in every photo must match what the customer receives.
- AI-made models are fine for showing fit and mood; don't present them as real customers or reviews.
- Replace AI lifestyle photos with real customer photos as they come in (post-purchase email).

---

## 9. Plan to finish before Q4 rush

Black Friday is **Nov 27, 2026**, and Q4 gift traffic climbs from mid-October.

| When | What |
|---|---|
| **This week** | Get all design files as transparent PNG (black ink + white ink). Fix color names across the store. Make the ChatGPT base scenes (≈ 6 heroes, 6 flat lays, 3 curvy, 5 lifestyle, 1 color grid). |
| **Week 1 (by Oct 9)** | Build the Canva templates. Finish full image sets for the **top 20 sellers**: Hello 60, 65, 50, 63, 59, 40, 58, 64, 55, 45, 49, 57, 62, 52, 56, the top Queen ages, and the vintage 1976 / 1966 shirts. |
| **Week 2 (by Oct 16)** | The rest of the Hello and Queen lines (swap-and-export with the templates). |
| **Week 3 (by Oct 23)** | Vintage, Sassy, sweatshirts, tanks. |
| **Week 4 (by Oct 30)** | Accessories, totes, socks, printables. Final check on phone. |

**Where I help:**
- Write the alt text and image file names for every product.
- Check your images: send me the first batch and I'll check print accuracy, color names and consistency.
- Once the images are uploaded (or have public links), link them to the right color variants and fix variant names across all products through the Shopify connector.
- Tweak prompts whenever ChatGPT gets something wrong.
