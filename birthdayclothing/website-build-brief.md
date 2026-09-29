# Birthday Universe: Complete Website Build Brief

*Version 1 · September 29, 2026 · Store: Shopify · Domain: birthdayuniverse.co*

This document is the single source of truth for building the Birthday Universe website.
It is written so it can be pasted into any AI website builder (GLM, ChatGPT, Claude) or handed to a designer.
Every builder gets this same brief, so the results can be compared fairly (see Section 14).

---

## 0. Master prompt (paste this first, then paste the rest of the document)

```
You are a senior Shopify e-commerce designer and front-end developer who builds
high-converting, mobile-first stores for American gift brands.

Build the website for "Birthday Universe" (birthdayuniverse.co), a US online birthday store,
exactly as described in the brief below. Deliver:
1. The HOMEPAGE, fully designed, with every section in Section 4 in that order.
2. The COLLECTION PAGE template (Section 5).
3. The PRODUCT PAGE template (Section 6), using "Hello 60 Birthday Shirt" as the example product.
4. The mobile navigation menu and the desktop mega menu (Section 3).

Rules:
- Mobile first: 88% of visitors are on phones. Design every section at 390px width first.
- Use the brand colors, fonts, tone and copy from the brief. Use the exact copy where given.
- Use realistic placeholder images described in the brief; never invent reviews, ratings,
  customer counts, awards or press logos.
- Output must be clean, production-ready code: either a Shopify Online Store 2.0 theme
  (Liquid sections + JSON templates, editable in the theme editor) or a single-folder
  HTML/CSS/JS prototype if Shopify code is not possible. Say which one you delivered.
- Page speed matters: lazy-load images, hero video under 4 MB, no heavy libraries.
- Accessible: real text (not text baked into images), alt text, 4.5:1 contrast, visible focus.
```

---

## 1. The brand

| | |
|---|---|
| **Name** | Birthday Universe |
| **Domain** | birthdayuniverse.co |
| **What we are** | America's birthday store: shirts, gifts, accessories and party pieces for every birthday worth celebrating. |
| **Positioning line** | *Everything for the big day, in one place.* |
| **Main tagline** | **Because you were born.** |
| **Campaign lines** | *For one day, the world revolves around you.* · *It's her turn.* (for Mom & Grandma campaigns) · *Every age deserves a party.* |

### Who we serve
Anyone in the US who wants to celebrate a birthday, whether they are celebrating **someone they love** or **themselves**.

1. **Gift givers** (the biggest group): daughters, sons, husbands, sisters, best friends and coworkers looking for a birthday gift that gets a real reaction and arrives on time.
2. **Self-celebrators**: people turning 21, 30, 40, 50, 60, 70 or 80+ who want to look and feel amazing on their day.
3. **The crew**: friend groups and families who want matching shirts for the party, brunch, cruise or trip.

*Today the catalog is mostly women's shirts and gifts (our best sellers are milestone birthdays 40–65). The site structure must make it easy to add Men, Kids, Family and Party categories later without a redesign.*

### Brand voice
Warm like a best friend, playful and a little sassy, confident, and always clear about dates and delivery.
- **Use:** celebrate, milestone, iconic, queen, crew, your year, the big day, birthday star.
- **Avoid:** "old", "over the hill", anything that makes age sound sad; pushy shouting ("BUY NOW!!!"); vague delivery language.

### Brand story (About page)

> **There's a moment on every birthday.**
>
> The candles are lit. Everyone is singing a little off-key. And for a few seconds, the whole room turns toward one person.
>
> It's the moment that says: **I'm so glad you were born.**
>
> Birthday Universe exists for that moment.
>
> For the daughter who has been planning her mom's 60th for months.
> For the best friends who show up to brunch in matching shirts.
> For the husband who forgot last year, and won't forget this year.
> For the woman turning 40 who decided this is *her* year.
> For grandma, who always says *"don't make a fuss,"* and deserves the biggest fuss of all.
>
> Whether you're celebrating someone you love, or finally celebrating yourself, everything for the big day is here: the shirt they'll wear all day, the crown, the gifts, and the matching tees for the whole crew.
>
> Because the day someone was born is worth celebrating out loud.
>
> **Welcome to Birthday Universe.**
> **For one day, the world revolves around you.**

### Brand story (homepage version, ~50 words)
> **I'm so glad you were born.**
> That's what every birthday really says. Birthday Universe is here for that moment: the shirt they'll wear all day, the gift that gets the happy tears, and matching tees for the whole crew. Whoever you're celebrating, even if it's you.
> **[Read our story →]**

### Our promises (only publish once the vendor has proven them)
1. **Here before the big day**: estimated delivery date shown before checkout. **[confirm production + shipping days]**
2. **A real person within 24 hours**: every email and chat answered within one business day.
3. **Wrong size? We'll swap it**: one free size exchange. **[confirm return shipping terms]**

---

## 2. Visual identity

| Element | Spec |
|---|---|
| **Primary colors** | Midnight Plum `#241B33` (night sky, "universe") · Candle Gold `#E3B25B` (celebration, buttons) · Blush Pink `#F4C7D0` (best-selling pink tees) · Cream `#FBF6EF` (backgrounds) |
| **Support colors** | Ink `#1D1B2E` (text) · Soft Lilac `#E9E1F3` (section backgrounds) · Success Green `#2F7D5B` (delivery-date messages) |
| **Headline font** | *Young Serif* (Google Fonts). Fallback: Georgia, serif |
| **Body font** | *Instrument Sans* (Google Fonts). Fallback: system-ui, sans-serif |
| **Buttons** | Candle Gold background with Ink text, 12px radius, 48px min height (thumb friendly). Secondary: plum outline |
| **Photography** | Real, joyful, candid moments: people laughing, candles, confetti, family tables, brunch with friends. Warm golden light. Diverse ages and backgrounds. Always one clean flat-lay of each product too. |
| **Motion ("cinematic")** | Slow and smooth. Full-screen looping hero video. Sections fade up gently on scroll. Product cards lift slightly on hover. One confetti burst when someone signs up or adds a squad pack. Respect "reduced motion" settings. |
| **Mood** | The page starts dark and candle-lit (the moment before "Surprise!") and gets brighter and more colorful as you scroll down (the party). |
| **Logo direction** | Wordmark "Birthday Universe" in the headline font, with a small gold star or candle flame as the dot or accent. |

---

## 3. Site map & navigation

### Announcement bar (rotating, thin, plum background, gold text)
1. 🎉 Birthday coming up? See your delivery date before you check out.
2. Matching shirts for the crew: buy 4+, save 15%. **[confirm]**
3. Free US shipping on orders over $**[50]**. **[confirm]**

### Header
Logo (center on mobile, left on desktop) · Search · Account · Cart (with item count).

### Main menu (desktop mega menu / mobile slide-out)

**1. Shop by Birthday**
- 21st · 30th · 40th · 50th · 60th · 65th · 70th · 75th · 80th+
- Every age, 18 to 90+ (a grid of all numbers)
- Birth Year shirts (Vintage 1946–2005)
- *Mega menu image: "What birthday are we celebrating?" with number bubbles.*

**2. Shirts & Apparel**
- Hello Collection (e.g. "hello FIFTY")
- Queen Collection (e.g. "The Queen is 79")
- Vintage Birth Year
- Sassy & Funny
- Sweatshirts
- Tank Tops
- Plus Size
- Matching Squad Shirts

**3. Accessories**
- Birthday Hats
- Crowns & Tiaras
- Jewelry (Birthstone necklaces)
- Socks
- Tote Bags
- Travel & Toiletry Bags
- *Coming soon: Sashes · Tumblers & Mugs · Birthday Buttons*

**4. Party & Printables**
- Photo Collage Signs (custom, instant download)
- *Coming soon: Banners · Balloons · Table Decor · Cake Toppers*

**5. Gifts For**
- Mom · Grandma · Wife · Sister · Best Friend · Daughter · Coworker · Myself
- Gifts under $25 · Gifts under $50
- *Later: For Him · For Kids*

**6. Our Story**

**Mobile menu:** a full-height slide-out with big tap targets. At the top, a horizontal row of age bubbles (30 · 40 · 50 · 60 · 70 · 80+). Then the 6 menu groups as expandable accordions. At the bottom: Track My Order · Help · Contact.

### Footer
- **Shop:** Shop by Birthday · Shirts · Accessories · Party & Printables · Gift Cards
- **Help:** Track My Order · Shipping & Delivery Dates · Size Guide · Exchanges & Returns · FAQ · Contact Us
- **Birthday Universe:** Our Story · Birthday Reminders · Squad Packs
- **Legal:** Privacy Policy · Terms of Service · Refund Policy · Your Privacy Choices
- Email signup: *"Get birthday reminders + 10% off your first order."*
- Tagline: *Because you were born.* · Payment icons · Social icons (Instagram, Facebook, TikTok, Pinterest)

---

## 4. Homepage (section by section, in this order)

### 4.1 Hero: cinematic video
- **Layout:** full-screen looping video (9:16 on mobile, 16:9 on desktop), soft dark gradient at the bottom, text on top as real HTML text.
- **Video:** a candle-lit room at night, family around a table, a woman opens a gift box, lifts out her birthday shirt, laughs; gold confetti in slow motion. 6–8 seconds, no sound, seamless loop, under 4 MB, with a poster image while loading.
- **Headline:** **Because you were born.**
- **Subheadline:** Birthday shirts, gifts and party pieces for every age, and everyone who loves them.
- **Buttons:** **[Shop by Birthday]** (gold) · **[Find a Gift]** (outline)
- *Alternate headline to A/B test:* **For one day, the world revolves around you.**

### 4.2 "What birthday are we celebrating?" (age picker)
- **Layout:** cream background. Big round number bubbles: **21 · 30 · 40 · 50 · 60 · 65 · 70 · 75 · 80+**, plus a "Birth year →" bubble. Horizontal swipe on mobile (like Instagram stories); a single centered row on desktop.
- **Interaction:** tap goes to that age collection; a tiny gold sparkle on hover or tap.
- **Subtext:** *Tap the big number. We'll show you everything made for it.*

### 4.3 Order-by delivery banner
- **Layout:** slim gold strip with a calendar icon.
- **Copy:** **Birthday on [Oct 18]? Order by [Oct 8].** Every product shows its delivery date before checkout.
- **Button:** [Check delivery dates] → Shipping & Delivery page.

### 4.4 Shop by collection (the main categories)
- **Layout:** 6 large image tiles (2 columns on mobile, 3 on desktop), each with a title and a small "Shop →".
- **Tiles:** Hello Collection · Queen Collection · Vintage Birth Year · Sassy & Funny · Accessories · Party & Printables
- **Heading:** **Find their birthday look**

### 4.5 Who's the birthday star? (shop by recipient)
- **Layout:** swipeable tall photo cards (4:5), with a slow zoom as they scroll into view.
- **Cards and captions:**
  - **For Mom**: Because she deserves the whole party.
  - **For Grandma**: Crowns are officially required.
  - **For My Wife**: Make her feel like the queen she is.
  - **For My Best Friend**: Matching shirts. Obviously.
  - **For My Sister**: Built-in best friend, built-in party.
  - **For Me**: It's my birthday and I'll shop if I want to.

### 4.6 Best sellers
- **Heading:** **The birthday favorites**
- **Layout:** product grid (2 columns on mobile, 4 on desktop) with tabs: **All · Hello · Queen · Vintage · Accessories**.
- **Product card:** flat-lay image, then a worn/lifestyle image on hover or swipe; title; price; color swatch dots; badge (`Best seller` · `Most gifted` · `New`); quick "Add" button.
- **Button:** [Shop all best sellers]

### 4.7 Our story (emotional moment)
- **Layout:** back to dark plum, full-width. On the left (top on mobile) a slow 6-second clip of someone making a wish and blowing out candles. On the right, the homepage story text fades in line by line as you scroll.
- **Copy:** the homepage version of the brand story (Section 1). Button: [Read our story].

### 4.8 Complete the celebration (accessories)
- **Heading:** **Complete the look**
- **Layout:** horizontal row of accessory products (crown, birthday hat, birthstone necklace, socks, tote bag).
- **Subtext:** *The shirt is the start. The crown makes it a party.*

### 4.9 Squad pack
- **Layout:** wide image of a friend group or family in matching shirts, text beside it.
- **Heading:** **Bring the whole crew.**
- **Copy:** Matching shirts for the party, the brunch or the cruise. Order 4 or more and save **[15]%**. Mix any sizes and colors.
- **Button:** [Build your squad pack]

### 4.10 Real birthdays (reviews & customer photos)
- **Layout:** swipeable strip of customer photos with star rating and a short quote.
- **Rule:** **show only real reviews from real orders.** At launch the section stays hidden and turns on after the first real reviews arrive.
- **Heading:** **Real birthdays. Real stars.** · *Tag @birthdayuniverse for a chance to be featured.*

### 4.11 Our promises
- **Layout:** 3 columns (stacked on mobile) with simple gold line icons: gift box, chat bubble, size tag.
- **Copy:** Here before the big day · A real person within 24 hours · Wrong size? We'll swap it.

### 4.12 Birthday reminder signup
- **Layout:** plum background, gold button, confetti burst on success.
- **Heading:** **Never miss a birthday again.**
- **Copy:** Tell us whose big day is coming up. We'll remind you 3 weeks before, with 10% off their gift.
- **Fields:** Your email · Their name · Their birthday (month + day) · Which birthday? (optional)
- **Button:** Remind me · **Success:** 🎉 Got it! We'll remind you 3 weeks before [Name]'s big day.

### 4.13 Footer (see Section 3)

---

## 5. Collection page template

Used for every collection: ages (e.g. "60th Birthday"), styles (Hello, Queen, Vintage), accessories and "Gifts for".

1. **Collection banner**: short (not full screen). Title + one warm line.
   - *Example, 60th Birthday:* **Sixty looks good on you.** Shirts, crowns and gifts for the big 6-0.
2. **Age chip row** (on all apparel collections): 30 · 40 · 50 · 60 · 65 · 70 · 80+, which lets shoppers jump between ages.
3. **Delivery line:** *Order by [date] for delivery by [date].*
4. **Filters** (a drawer on mobile, a sidebar on desktop): Birthday age · Style (Hello, Queen, Vintage, Sassy) · Product type (T-shirt, V-neck, Sweatshirt, Tank, Accessory) · Color · Size · Price.
5. **Sort:** Best selling (default) · Newest · Price.
6. **Product grid:** same card as the homepage best sellers. 2 columns on mobile.
7. **Mid-grid banner** after the 8th product: "Bring the whole crew: 4+ shirts, save 15%."
8. **SEO text block** at the bottom: 100–150 words about celebrating that birthday, plus an FAQ accordion (sizes, delivery times, exchanges).
9. **Cross-links:** "Shop other birthdays" · "Complete the look" accessories.

---

## 6. Product page template (example: Hello 60 Birthday Shirt)

### Layout (mobile order; on desktop the gallery is on the left and the details are on the right)
1. **Gallery:** swipeable images with dots.
   - (1) Clean flat-lay showing the true print · (2) Worn by a model · (3) Lifestyle/party photo · (4) Color options · (5) Size chart image · (6) Optional short video.
2. **Badge:** `Best seller`
3. **Title:** **Hello 60 Birthday Shirt**
4. **Rating line:** ★★★★★ (number of reviews), shown only when real reviews exist.
5. **Price:** $25.99 · *"Pairs with the Birthday Crown, +$12.99"* (small link)
6. **Short hook** (1–2 lines): *Sixty never looked this good. The shirt she'll wear to dinner, in every photo, and all weekend long.*
7. **Choose the birthday:** a row of age buttons linking sister products (50 · 55 · 60 · 63 · 65 · 70…), so shoppers can switch age without searching.
8. **Color:** color swatch circles (Black, White, Light Pink, Navy Blue, Charcoal Gray).
9. **Style:** Round neck / V-neck (where available).
10. **Size:** size buttons (S–5XL) + a **"Size guide"** link that opens a modal with a chart and a "Between sizes? Size up" tip.
11. **Delivery estimate (green):** 🎁 *Order in the next 5h 20m, get it by **Thu, Oct 9**.*
12. **Quantity + Add to Cart** (gold, full width) · **Buy it now** (outline).
13. **Trust row** (small icons): Free size swap · Real humans in 24h · Secure checkout.
14. **"Complete the look" add-ons:** checkboxes for Birthday Crown ($12.99) · Birthday Socks ($15.99) · Matching Tote ($34.99), plus "Add all to cart".
15. **Squad upsell:** *Buying for the crew? Add 4+ and save 15%.*
16. **Accordions:**
    - *Description:* 3 short paragraphs (see the product copy template below)
    - *Fit & Fabric:* unisex/ladies fit, fabric, care instructions **[confirm with vendor]**
    - *Size Chart*
    - *Shipping & Delivery:* production time + shipping time, order-by guidance
    - *Exchanges:* the free size swap promise
17. **Reviews with photos** (real only).
18. **"Also celebrating…"**: the same design in other ages.
19. **"You might also love"**: the Queen and Vintage versions of the same age.
20. **Sticky Add to Cart bar** on mobile once the main button scrolls out of view.

### Product copy template
- **Title format:** `[Design] [Age] Birthday [Product type]`, e.g. *Hello 60 Birthday Shirt*, *Queen is 79 Birthday Shirt*, *Vintage 1966 60th Birthday Shirt*, *60th Birthday Tote Bag*.
- **Description (example):**
  > **Sixty never looked this good.**
  > Say hello to the big 6-0 in style. Our *Hello 60* shirt pairs a flowing script "hello" with bold "SIXTY" lettering and a little heart, because this birthday deserves a statement.
  >
  > **Made for the whole celebration:** soft, comfortable and made to wear all day, from the morning coffee to the birthday dinner. **[confirm fabric]**
  >
  > **The perfect gift:** for moms, grandmas, sisters, wives and best friends, or for yourself, because you earned this one.

---

## 7. Other pages

| Page | What it needs |
|---|---|
| **Our Story** | Full brand story, photos of real celebrations, the 3 promises, founder note (only if true, written by the founder). |
| **Track My Order** | Order number + email lookup (a Shopify order-status link or tracking app). |
| **Shipping & Delivery Dates** | Simple table: production time + shipping method + total days; an "order-by" calendar for the next 4 weeks; holiday cut-off dates. |
| **Size Guide** | Charts per product type (T-shirt, V-neck, sweatshirt, tank), with a "how to measure" illustration and a "between sizes" tip. |
| **Exchanges & Returns** | The free size swap, how it works in 3 steps, and what's not returnable (custom/printable items). |
| **FAQ** | Delivery, sizing, colors, custom orders, bulk/squad orders, gift notes, contact. |
| **Contact** | Form + email + "we reply within 24 hours". |
| **Squad Pack** | Pick a design and age, then add each person's size and color in one form. 4+ items get the discount automatically. |
| **Birthday Reminders** | Same form as homepage section 4.12, with a longer explanation. |
| **Gift Cards** | Shopify gift card product with birthday-themed card designs. |

---

## 8. Cart & checkout

- **Cart drawer** (slides in from the right) instead of a separate cart page.
- **Free-shipping progress bar:** *You're $12 away from free shipping!* **[confirm threshold]**
- **One smart upsell** in the drawer: the crown or socks, chosen by what's in the cart.
- **Gift note** checkbox + message field.
- Delivery estimate repeated in the drawer.
- Trust icons + payment icons under the Checkout button.
- **Thank-you page message:** *You just made someone's birthday. 🎂 We'll email tracking as soon as it ships.*

---

## 9. Ad & marketing copy bank

### Meta ad angles (primary text + headline)
| Angle | Hook / primary text | Headline |
|---|---|---|
| **Gift for Mom** | She planned every one of your birthdays. Now plan hers. 🎂 The Hello shirt she'll wear all day, delivered before the party. | Get Mom her birthday shirt |
| **Self-celebration** | Turning 40 this year? Make it loud. Shirts, crowns and everything for your big day. | It's your year. Dress like it. |
| **Squad** | The whole crew showed up matching, and the birthday girl cried happy tears. 4+ shirts, 15% off. | Matching shirts for the crew |
| **Last minute** | Birthday in 2 weeks and still no gift? Order by [date] and it arrives in time. | Arrives before the big day |
| **Queen** | She's not getting older. She's getting royal. 👑 The Queen collection, every age from 30 to 90. | Crown her birthday |
| **Vintage year** | Born in 1966? Aged to perfection. Vintage birth-year shirts for every year. | Find their birth year |
| **Sassy** | For the friend who says "I'm 39+1" with a straight face. 😏 | Birthday shirts with attitude |

### Video hooks (first 2 seconds)
- "What year were you born? Stop scrolling when you see it."
- "I gave my mom her 60th birthday shirt, and she cried."
- "POV: your whole friend group shows up matching."
- "She said 'don't make a fuss.' So we made a fuss."
- "Ordered Monday. Arrived Friday. Birthday Saturday."

### Email subject lines
- Welcome: *Welcome to Birthday Universe 🎉 (here's 10% off)*
- Abandoned cart: *Their birthday is coming up…*
- Reminder: *🎂 [Name]'s birthday is in 3 weeks*
- Post-purchase: *You just made someone's birthday*
- Review request: *Did they love it? Show us the birthday photos 📸*

---

## 10. SEO basics

- **Homepage title:** Birthday Universe | Birthday Shirts & Gifts for Every Age
- **Collection title pattern:** `[Age]th Birthday Shirts & Gifts for Women | Birthday Universe`
- **Product title pattern:** `[Product Name] | Birthday Universe`
- **Meta description pattern:** *Celebrate [her/his/your] [age]th birthday with [product]. Soft, fun and delivered before the big day. Free size swaps.*
- **URL handles:** short and readable, e.g. `/collections/60th-birthday`, `/products/hello-60-birthday-shirt`.
- Every image has descriptive alt text (e.g. "Pink Hello 60 birthday shirt, flat lay").

---

## 11. Current catalog (from the Shopify store, Sep 29, 2026)

About **400 active products**, prices mostly $15.99–$44.99:

| Family | Examples | Price | Notes |
|---|---|---|---|
| Hello birthday tees | Hello 22 → Hello 80+ ("Birthday Gift For Women") | $25.99 | **Top sellers:** Hello 60, 65, 50, 63 |
| Queen tees (47) | Queen is 55 / 58 / 60 / 79 | $25.99 | Round + V-neck, 5 colors |
| Vintage birth-year tees | 40th Birthday Shirt Vintage 1986 | $25.99 | One per year |
| Sassy & funny tees (~60) | "39+1", snarky designs | $25.99 | |
| Sweatshirts & plus sweatshirts | 45th Birthday Sweatshirt | $39.99 | |
| Tank tops | 45th / 50th Tank Top | $31.99 | |
| Socks | 35th / 40th / 50th Birthday Socks | $15.99 | |
| Tote bags (23) | 41st Birthday Tote Bag | $34.99–44.99 | |
| Toiletry bag | 40th Birthday Toiletry Bag | | |
| Photo collage printables (31) | 30th Birthday Photo Collage | $24.99 | Digital download |
| Accessories | Birthstone Necklace ($35), Birthday Crown ($12.99), Birthday Hat ($23.99) | | |

### Catalog clean-up before launch
- Duplicate products (e.g. two "43rd Birthday Shirt 1983", two "47th Birthday Shirt 1979").
- Typos: "46tth Birthday Photo Collage", "50th Birthday Shirt Vinatge", vendor "Birthday Celeberation".
- Mixed vendor names ("My Store", "Birthday Clothing", "Birthday Celeberation"). Change all to **Birthday Universe**.
- Many products have an empty Product Type. Set it (T-Shirt, V-Neck, Sweatshirt, Tank, Socks, Tote Bag, Accessory, Printable) so filters work.
- Rename titles to the new pattern ("Hello 60 Birthday Shirt" instead of "60th Birthday Gift For Women").
- Remove the "over the hill" tags (off-brand); keep tags for age, style and recipient.
- One anniversary product: move it to a hidden "More celebrations" collection for later.

---

## 12. Tech & apps

| Need | Recommendation |
|---|---|
| Theme | Shopify free theme **Dawn** or **Horizon** (fast, flexible), with custom sections for the age picker, order-by banner, story scroll and reminder form |
| Reviews | Judge.me (photo reviews) |
| Email & SMS | Klaviyo (welcome, abandoned cart, reminder, post-purchase, review request) |
| Delivery date | A delivery-date estimator app |
| Bundles / squad discount | Shopify automatic discount (buy 4+, save 15%), or a bundles app |
| Speed | WebP/AVIF images, lazy loading, hero video under 4 MB, target Lighthouse mobile score of 70+ |
| Tracking | Meta Pixel + Conversions API, Google Analytics 4, tested with one real order |

---

## 13. Launch checklist

- [ ] Brand story approved
- [ ] Hero video (mobile + desktop) made
- [ ] Lifestyle images for 6 recipient cards + 6 collection tiles + squad banner
- [ ] Theme installed, colors and fonts set
- [ ] Homepage, collection and product templates built
- [ ] Menus built exactly as Section 3
- [ ] Catalog clean-up done (Section 11)
- [ ] Policies and help pages written
- [ ] Apps installed and tested
- [ ] 3 test orders placed and delivered on time
- [ ] Phone test on iPhone + Android, checkout end to end

---

## 14. How we compare the builders (GLM vs ChatGPT vs Claude)

Score each builder's result from 1 to 5 on each line (maximum 50):

| # | Criterion | What "5" looks like |
|---|---|---|
| 1 | **Mobile experience** | Everything reads and taps easily at phone width, with no sideways scrolling |
| 2 | **First impression** | The hero makes you feel "a birthday is happening" within 3 seconds |
| 3 | **Finding the right product** | Age picker, menus and filters get you to "Hello 60, pink, size L" in under 3 taps |
| 4 | **Product page** | Size, color, delivery date, add-ons and trust info are clear and above the fold |
| 5 | **Brand feel** | Colors, fonts, copy and voice match this brief |
| 6 | **Trust** | Delivery dates, promises and help are visible; nothing fake |
| 7 | **Speed** | Loads fast on a phone, video is light |
| 8 | **Code quality** | Clean, editable in the Shopify theme editor, no broken sections |
| 9 | **Completeness** | Every section in this brief is present, in the right order |
| 10 | **Room to grow** | Easy to add Men, Kids and Party categories later |

The best-scoring build becomes the master, and we move its best ideas from the others into it.
