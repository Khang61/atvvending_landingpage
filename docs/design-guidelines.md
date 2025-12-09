# AutoViet Design Guidelines

Design system for AutoViet vending machine services landing page.

## Brand Identity

**Company:** AutoViet (CONG TY TNHH DICH VU & CONG NGHE TU DONG VIET)
**Industry:** Vending machine services (sales, rental, repair)
**Target:** B2B (factories, hospitals, universities, companies)
**Tone:** Professional, trustworthy, modern, industrial/tech

---

## Color Palette

### Primary Colors
| Name | Hex | Usage |
|------|-----|-------|
| Orange Primary | `#FF6B00` | CTAs, highlights, key accents |
| Orange Hover | `#E65F00` | Button hover states |
| Orange Light | `#FFF4EB` | Light backgrounds, tags |

### Secondary Colors
| Name | Hex | Usage |
|------|-----|-------|
| Black Deep | `#0A0A0A` | Hero sections, premium areas |
| Black Primary | `#111111` | Headers, footers |
| Black Soft | `#1A1A1A` | Card backgrounds (dark mode) |
| Gray Dark | `#2D2D2D` | Secondary text on dark |
| Gray Medium | `#6B6B6B` | Body text, captions |
| Gray Light | `#E5E5E5` | Borders, dividers |

### Accent Colors
| Name | Hex | Usage |
|------|-----|-------|
| White | `#FFFFFF` | Text on dark, backgrounds |
| Off-White | `#FAFAFA` | Section backgrounds |
| Success | `#22C55E` | Positive indicators |
| Error | `#EF4444` | Error states |

---

## Typography

### Font Stack
```css
--font-heading: 'Be Vietnam Pro', sans-serif;
--font-body: 'Be Vietnam Pro', sans-serif;
--font-accent: 'Space Grotesk', sans-serif;
```

**Be Vietnam Pro** - Primary font, excellent Vietnamese support, modern geometric sans-serif.
**Space Grotesk** - Accent font for tech elements, numbers, stats.

### Type Scale (Desktop)
| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| H1 | 56px / 3.5rem | 700 | 1.1 |
| H2 | 40px / 2.5rem | 700 | 1.2 |
| H3 | 28px / 1.75rem | 600 | 1.3 |
| H4 | 20px / 1.25rem | 600 | 1.4 |
| Body | 16px / 1rem | 400 | 1.6 |
| Body Small | 14px / 0.875rem | 400 | 1.5 |
| Caption | 12px / 0.75rem | 500 | 1.4 |

### Mobile Type Scale
| Element | Size |
|---------|------|
| H1 | 36px / 2.25rem |
| H2 | 28px / 1.75rem |
| H3 | 22px / 1.375rem |
| Body | 16px / 1rem |

---

## Spacing System (8px Grid)

```css
--space-1: 4px;    /* Tight spacing */
--space-2: 8px;    /* Element gaps */
--space-3: 16px;   /* Component padding */
--space-4: 24px;   /* Section gaps */
--space-5: 32px;   /* Card padding */
--space-6: 48px;   /* Section padding */
--space-7: 64px;   /* Large sections */
--space-8: 96px;   /* Hero padding */
--space-9: 128px;  /* Section separators */
```

---

## Components

### Buttons

**Primary Button (Orange)**
```css
background: #FF6B00;
color: #FFFFFF;
padding: 14px 28px;
border-radius: 8px;
font-weight: 600;
font-size: 16px;
transition: all 0.2s ease;
/* Hover: background #E65F00, transform translateY(-2px) */
```

**Secondary Button (Outline)**
```css
background: transparent;
color: #FF6B00;
border: 2px solid #FF6B00;
padding: 12px 26px;
border-radius: 8px;
/* Hover: background rgba(255,107,0,0.1) */
```

**Ghost Button (Dark theme)**
```css
background: transparent;
color: #FFFFFF;
border: 1px solid rgba(255,255,255,0.3);
/* Hover: border-color #FF6B00, color #FF6B00 */
```

### Cards

**Service Card**
```css
background: #FFFFFF;
border-radius: 16px;
padding: 32px;
box-shadow: 0 4px 24px rgba(0,0,0,0.06);
border: 1px solid #E5E5E5;
/* Hover: box-shadow 0 8px 32px rgba(255,107,0,0.12), border-color #FF6B00 */
```

**Dark Feature Card**
```css
background: #1A1A1A;
border-radius: 16px;
padding: 32px;
border: 1px solid #2D2D2D;
/* Accent line: border-left 4px solid #FF6B00 */
```

---

## Section Layouts

### Hero Section
- Full viewport height on desktop (100vh)
- Dark background (`#0A0A0A`)
- Large headline with orange accent words
- CTA buttons below headline
- Product image or video on right (desktop)

### Alternating Sections
- Light (`#FAFAFA`) and dark (`#111111`) alternating
- Max content width: `1200px`
- Padding: `96px 0` desktop, `64px 0` mobile

### Grid System
- 12-column grid
- Gutter: `24px`
- Content cards: 3-column desktop, 2-column tablet, 1-column mobile

---

## Breakpoints

```css
--mobile: 320px;
--mobile-lg: 480px;
--tablet: 768px;
--desktop: 1024px;
--desktop-lg: 1280px;
--desktop-xl: 1440px;
```

---

## Icons

**Style:** Outlined, 2px stroke, rounded caps
**Size:** 24px default, 20px small, 32px large
**Color:** Inherit from parent or `#FF6B00` for accents
**Recommended:** Lucide Icons, Phosphor Icons

---

## Image Treatment

**Hero Images**
- High contrast, dramatic lighting
- Dark overlays: `linear-gradient(rgba(10,10,10,0.7), rgba(10,10,10,0.9))`
- Orange accent lighting preferred

**Product Photos**
- Clean white or dark gray backgrounds
- Consistent angle (3/4 view)
- Subtle shadows

**Aspect Ratios**
- Hero: 16:9
- Cards: 4:3
- Thumbnails: 1:1

---

## Animation Guidelines

**Transitions**
```css
--transition-fast: 150ms ease;
--transition-base: 200ms ease;
--transition-slow: 300ms ease-out;
```

**Micro-interactions**
- Button hover: slight lift (`translateY(-2px)`)
- Card hover: shadow expansion, border color change
- Links: underline animation left-to-right

**Scroll Animations**
- Fade up on scroll (subtle, 20px movement)
- Stagger delays for card groups (100ms intervals)
- Respect `prefers-reduced-motion`

---

## Logo Guidelines

**Placement**
- Header: left-aligned, max height 40px
- Footer: left-aligned, max height 48px
- Clear space: minimum 16px on all sides

**Variants Needed**
- Full color (orange + black)
- White (for dark backgrounds)
- Black (for light backgrounds)

---

## Accessibility

- Minimum contrast ratio: 4.5:1 (text), 3:1 (large text)
- Focus states: `outline: 2px solid #FF6B00; outline-offset: 2px;`
- Touch targets: minimum 44x44px
- Alt text required for all images
- Semantic HTML structure

---

## Quick Reference

```css
/* Core variables */
:root {
  --color-primary: #FF6B00;
  --color-primary-hover: #E65F00;
  --color-black: #111111;
  --color-black-deep: #0A0A0A;
  --color-white: #FFFFFF;
  --color-gray: #6B6B6B;
  --font-heading: 'Be Vietnam Pro', sans-serif;
  --font-accent: 'Space Grotesk', sans-serif;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
}
```
