---
name: Orderlane
description: A photo-led customer ordering demonstration.
colors:
  paper: "#faf9f6"
  white: "#fff"
  ink: "#222b26"
  muted: "#626c65"
  line: "#e4e7e1"
  green: "#253b31"
  orange: "#b64527"
  wash: "#f0f3ec"
  danger: "#a12f24"
  primary-hover: "#97391f"
  secondary-hover: "#e5eadf"
typography:
  body:
    fontFamily: "Manrope, sans-serif"
    fontSize: "14px"
  display:
    fontFamily: "Manrope, sans-serif"
    fontSize: "clamp(28px,3.2vw,42px)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-1.2px"
rounded:
  control: "7px"
  basket: "14px"
  hero: "16px"
  meal-image: "12px"
spacing:
  desktop-gap: "42px"
  basket-padding: "24px"
components:
  button-primary:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.white}"
    rounded: "{rounded.control}"
    padding: "14px 17px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.green}"
    rounded: "{rounded.control}"
    padding: "14px 17px"
---

# Design System: Orderlane

## Overview

Operate mode: a photo-led customer menu with a clear basket, confirmation and tracking. Warm white, forest and restrained orange support food photography and compact Manrope typography. The technical walkthrough is secondary.

This record replaces the earlier serif, text-only counter direction with the implementation in `static/storefront.css` and the ordering surface brief. Source inspection only: browser unavailable, no screenshots or visual approval. This remains a fictional, small ordering demonstration.

## Colors

Paper provides the page background; white supports menu controls, baskets and order cards. Ink and muted text establish hierarchy. Green marks selected filters, confirmation and completed stages; orange carries primary actions and keyboard focus. Wash provides quiet grouping; danger marks failures.

## Typography

Self-hosted Manrope supplies headings, body and controls, with weights 200 through 800 available. Its local font asset is `static/assets/manrope.ttf`, with license in `static/assets/OFL.txt`. Menu headings use 24px at weight 750; meal titles use 16px at weight 750. Money and quantities use tabular numerals. The display token describes the default hero heading; responsive rules override it at the documented breakpoints.

## Layout

The default main container is capped at 1280px with 40px horizontal padding. The menu occupies the flexible column beside a 330px basket, separated by the desktop gap token. The basket is sticky at 24px from the top. A split kitchen hero pairs copy with a cover-cropped photograph.

At min-width 1440px, the container grows to 1360px, basket to 350px and gap to 52px. At max-width 1080px, horizontal padding becomes 28px and the basket column 290px. At max-width 800px, ordering stacks, the basket becomes static, a fixed mobile basket action appears and other grids become one column. At max-width 450px, horizontal padding becomes 18px, search fills the menu heading and meal images narrow to 88px.

## Elevation & Depth

Borders and quiet backgrounds separate most surfaces. The fixed mobile basket action uses the recorded shadow. Confirmation enters from 7px below over .35s only when reduced motion is not requested. There is no receipt-entry animation in this stylesheet.

## Shapes

Controls have softly curved corners. The basket and kitchen hero use larger corners; meal photographs have rounded crops. Order cards and confirmation use 13px corners. Status markers and timeline dots are circular.

## Components

Primary buttons use orange and a darker hover; secondary buttons use wash and green text. Their CSS sets a minimum height of 44px, rather than a fixed height. Selected filters use green with white text. Active navigation uses an underline. Quantity controls are compact rectangular groups. Focus-visible uses a 3px orange outline with 4px offset; search focus-within uses a 2px orange outline with 2px offset. Disabled controls use .48 opacity.

Local food photographs and their source, artist and license records are in `static/assets/credits.json`: jollof, egusi, beans and chicken are recorded as CC BY-SA 4.0; suya as CC0. Preserve these records and the font license alongside the assets.

## Do's and Don'ts

- Do retain the photo-led menu, visible basket, confirmation and tracking hierarchy.
- Do preserve attribution records and local font licensing.
- Do keep visible keyboard focus and tabular money.
- Don't imply real orders, payments, delivery, production accounts, ratings or discounts.


