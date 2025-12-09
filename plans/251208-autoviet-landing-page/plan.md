# AutoViet Landing Page - Implementation Plan

## Project Overview
Single-page responsive landing for AutoViet vending machine services. Pure HTML/CSS/JS, no frameworks, mobile-first design with orange/black color scheme.

## Company Details
- Name: CÔNG TY TNHH DỊCH VỤ & CÔNG NGHỆ TỰ ĐỘNG VIỆT
- Founded: 04/11/2025
- Tax ID: 0111272009
- Phone: 0865771995
- Address: Số 10 ngõ Cây Đa 6, Thôn Lập Trí, Xã Kim Anh, Hà Nội
- Services: Vending machine sales, rental, repair, maintenance

## Tech Stack
- HTML5 semantic markup
- CSS3 (Flexbox, Grid, custom properties)
- Vanilla JavaScript (ES6+)
- No build tools, no dependencies
- Mobile-first responsive (320px → 1920px+)

## Color Palette
- Primary: #FF6B00 (Orange)
- Secondary: #000000, #1a1a1a (Black)
- Accent: #FFFFFF (White)
- Neutrals: #f5f5f5, #333333

## Page Sections (11 Total)
1. **Header** - Sticky nav, logo, menu, CTA button
2. **Hero** - Headline, tagline, primary CTA
3. **Stats** - 3-4 key metrics (machines deployed, partners, years)
4. **Services** - 4 cards (Bán, Cho thuê, Sửa chữa, Bảo trì)
5. **Products** - 13 vending machines (Unsplash placeholders)
6. **Projects** - Deployed installations (Unsplash placeholders)
7. **Partners** - 35+ company logos grid
8. **Suppliers** - Supplier logos grid
9. **About** - Company story, mission, values
10. **Contact** - Form + phone + address + map embed option
11. **Footer** - MST, links, copyright, social

## Key Features
- Smooth scroll navigation
- Mobile hamburger menu
- Lazy loading images
- Contact form validation (frontend)
- SEO meta tags
- Fast load (<3s on 3G)
- Accessible (WCAG 2.1 AA)

## Implementation Phases
1. **Phase 01** - Project structure, folder setup, asset organization
2. **Phase 02** - HTML semantic markup, content structure
3. **Phase 03** - CSS styling, responsive design, orange/black theme
4. **Phase 04** - JavaScript interactions, form validation, smooth scroll
5. **Phase 05** - Image optimization, placeholders, performance tuning

## Success Criteria
- Mobile-first responsive (passes Google Mobile-Friendly Test)
- All sections functional with real content
- Contact form validates input (name, phone, email, message)
- Partners/suppliers logos organized in grids
- Fast loading with optimized assets
- Clean, maintainable codebase

## File Structure
```
atvvending/
├── index.html
├── css/
│   ├── reset.css
│   ├── variables.css
│   ├── main.css
│   └── responsive.css
├── js/
│   ├── main.js
│   ├── navigation.js
│   └── form.js
├── images/
│   ├── logo.png
│   ├── products/
│   ├── projects/
│   ├── partners/
│   └── suppliers/
└── plans/
    └── 251208-autoviet-landing-page/
