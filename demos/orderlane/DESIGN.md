---
name: Orderlane
description: A cool white and indigo collection counter.
colors:
  neutral-0: "#fff"
  neutral-50: "#f5f6fb"
  neutral-100: "#eceef5"
  neutral-200: "#dce0ec"
  neutral-500: "#666e85"
  neutral-700: "#3c455d"
  neutral-900: "#20273b"
  blue-50: "#eef0ff"
  blue-100: "#e1e6ff"
  blue-600: "#4059d8"
  blue-700: "#3048bc"
  green-50: "#e8f5ed"
  green-700: "#276545"
  red-50: "#fff0ed"
  red-700: "#ab3528"
typography:
  body:
    fontFamily: "Outfit, sans-serif"
    fontSize: "1rem"
  small:
    fontSize: ".875rem"
  caption:
    fontSize: ".8125rem"
  title:
    fontSize: "1.25rem"
  heading:
    fontSize: "clamp(2rem,3.2vw,2.75rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-.03em"
rounded:
  sm: "8px"
  md: "14px"
  lg: "20px"
  action: "10px"
spacing:
  basket-padding: "24px"
  desktop-gap: "30px"
components:
  button-primary:
    backgroundColor: "{colors.blue-600}"
    textColor: "{colors.neutral-0}"
    rounded: "{rounded.action}"
    padding: "13px 18px"
  button-primary-hover:
    backgroundColor: "{colors.blue-700}"
  button-secondary:
    backgroundColor: "{colors.neutral-0}"
    textColor: "{colors.neutral-700}"
    rounded: "{rounded.action}"
    padding: "13px 18px"
---

# Design System: Orderlane

## Overview

A crisp contemporary collection counter: Outfit, cool white surfaces, an indigo action accent, a compact kitchen identity, Cooking illustration, dish photographs and tabular naira prices. Choose a kitchen, add a meal, inspect the basket, place an order and follow its status. Kitchen actions and API evidence remain secondary tasks.

The full overhaul replaces the warm Manrope identity. The user delegated illustration and overhaul choices. The formal concept-roll and decision-card stage was not run; no retrospective comp approval or full workflow compliance is claimed. Implementation authority is `templates/counter.html`, `static/counter.css`, `static/storefront.js` and `.impeccable/surfaces/counter-overhaul.md`.

## Colors

Neutral-50 is the canvas; neutral-0 supplies white surfaces. Neutral-900 carries main text, neutral-500 secondary text and neutral-200 separators. Blue-600 marks actions and focus; blue-50 and blue-100 provide selected and interactive backgrounds. Green pairs mark confirmation and completed orders; red pairs mark errors. CSS semantic aliases map these primitives to page, surface, text, line, accent and focus roles.

## Typography

Self-hosted Outfit variable WOFF2 supplies weights 400 through 800. The font asset is 32,292 bytes. Headings use compact tracking and weights 600 or 700; menu titles use 16px at weight 600. Body and input text remain readable, and prices, counts and timestamps use tabular numerals. Mobile search and selectors use 16px text. The heading token is overridden by the explicit responsive sizes in the stylesheet.

## Layout

The shell is capped at 1660px. Default desktop navigation occupies a sticky 190px rail; the content area has 40px horizontal padding. The flexible menu sits beside a 310px sticky basket, with the desktop gap token. A split kitchen identity pairs copy and illustration. Menu cards form three columns by default.

At min-width 1500px, the rail grows to 210px, content padding to 48px and basket to 340px. At max-width 1250px, the rail is 166px, basket 280px and menu two columns. At max-width 960px, navigation becomes a top row. At max-width 740px, ordering stacks, basket becomes static, the inset basket shortcut appears and order timelines become vertical with readable times. At max-width 460px, meals become horizontal photo cards in one column. At max-width 350px, image width becomes 95px, search fills its row and the collection label hides.

Desktop first view exposes kitchen identity, artwork, photo menu and basket together. Phone prioritises kitchen and menu, with the basket shortcut appearing after an item is added. Narrow layouts reflow controls.

## Elevation & Depth

Tonal surfaces supply most separation. Search and selected filters have subtle shadows. The mobile basket shortcut uses a larger shadow; secondary actions use an inset border shadow. There are no entry animations. Under no-preference motion settings, pointer press scales buttons to .96 over 150ms using cubic-bezier(.2,0,0,1). Keyboard activation disables this movement and transitions; reduced-motion settings do not enable them. Hover treatments apply only to fine pointers supporting hover.

## Shapes

Small corners serve navigation and grouping, medium corners serve meals, baskets and orders, and large corners serve the kitchen identity. Actions use the action radius. Photographs use cover crops; Cooking uses contain sizing. Timeline markers are circular.

## Components

Adding a meal replaces its add control with an inline quantity group, retains focus and updates basket count and total. Final quantity buttons are 44px square. Add controls have a 44px minimum target; primary and secondary actions have a 48px minimum height. Selects, filters, text buttons and credits summary have a 44px minimum height. Search input has a 48px minimum height.

Focus-visible uses a 3px accent outline offset by 4px; search focus-within uses 2px offset by 3px. Forced-colors rules use Highlight for focus and selected navigation, and CanvasText borders for meals and basket. Disabled buttons use .45 opacity. Status announcements and labelled fields retain their semantic implementation.

All assets are self-hosted. The official unDraw Cooking SVG is recoloured to the blue-600 accent; its credit remains in About & credits. Food source, artist and license records remain in `static/assets/credits.json`, with font licensing alongside local font assets. One portfolio-demo disclosure lives in About; the API lab and project documentation carry technical boundaries. This is a small demonstration without real fulfilment, payment or production authentication.

## Do's and Don'ts

- Do preserve the collection-order sequence, inline quantity interaction and phone timeline.
- Do retain visible keyboard focus, readable inputs, tabular prices and asset credits.
- Don't add fabricated reviews, promotional metrics, payment, delivery or affiliation claims.
- Don't scatter repeated demo disclaimers through ordering tasks.

Verification: a fresh reviewer opened eight actual browser screenshots covering menu widths 1440, 1280, 390 and 320, plus phone basket, orders, kitchen and API views. No material visual defect was found against the written direction. Images and font loaded, no horizontal overflow was observed, and menu controls met the 44px minimum. Twenty-four API checks and thirteen DOM checks passed. These are targeted checks, not a full accessibility audit.
