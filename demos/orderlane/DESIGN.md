---
name: Orderlane
description: A restaurant service counter for a fictional ordering demonstration.
colors:
  paper: "#f8f5ed"
  ink: "#193d32"
  muted: "#4f655b"
  line: "#d8ddd2"
  orange: "#b9401b"
  white: "#fff"
  wash: "#edf0e7"
  orange-hover: "#973315"
  secondary-hover: "#dfe6d8"
  failure: "#a52816"
typography:
  display:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: "clamp(32px,4.4vw,56px)"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "-1.6px"
  body:
    fontFamily: '"Segoe UI", system-ui, sans-serif'
  label:
    fontSize: "12px"
rounded:
  surface: "14px"
  control: "8px"
spacing:
  pane-gap: "32px"
  receipt-padding: "28px"
components:
  button-primary:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.white}"
    rounded: "{rounded.control}"
    padding: "13px 18px"
  button-primary-hover:
    backgroundColor: "{colors.orange-hover}"
  button-secondary:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "13px 18px"
---

# Design System: Orderlane

## Overview

Operate mode: a restaurant service counter, with warm cream paper, dark forest ink and orange action controls. Serif headings pair with quiet sans-serif controls. Food is described through authored menu content, not decorative illustrations.

This record merges the original direction with implemented values from `static/app.css`. It is a source inspection, not a visual approval.

## Colors

Orange marks primary actions; forest ink carries text, active navigation and completed status. Paper is the page background, white the receipt and order surfaces, wash the quiet secondary regions. Muted text and line separators keep the working interface restrained. Failure red marks failed checks.

## Typography

Georgia headings accompany Segoe UI/system UI body and controls. Money, quantities and order identifiers use tabular numerals. Secondary headings use 28px and 23px sizes. Primary controls use 14px text at weight 600.

## Layout

Header and view switch precede a broad working pane and narrower receipt pane. The main container is capped at 1320px with 5% horizontal padding. The working grid uses 1.65fr and minmax(280px,1fr) columns. At a maximum width of 800px, the grids become one column and the receipt stacks beneath the task. The menu and order desk carry the first viewport without a marketing hero.

## Elevation & Depth

White surfaces, quiet separators and wash backgrounds provide most layering. The receipt alone carries a soft shadow. Its entry translates upward by 8px over .45s; reduced motion disables animation.

## Shapes

Soft surface corners use the surface radius; buttons, selects and navigation use the control radius. Quantity controls are circular. Receipt dividers are dashed.

## Components

Primary actions use orange with a darker hover. Secondary actions use wash with a slightly stronger hover. Active navigation uses forest ink and white text. Keyboard focus uses a 3px ink outline offset by 4px. Disabled buttons use .5 opacity. Fields have visible labels; status output uses polite live announcements.

## Do's and Don'ts

- Do retain the warm counter palette, serif headings and tabular money.
- Do keep semantic buttons, labelled fields and visible keyboard focus.
- Don't introduce decorative food illustrations into the established authored-menu treatment.
