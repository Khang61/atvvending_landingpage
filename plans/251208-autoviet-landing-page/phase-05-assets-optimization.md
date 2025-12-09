# Phase 05 - Assets & Optimization

## Objectives
- Organize image assets (logo, products, projects, partners, suppliers)
- Use Unsplash placeholders for products/projects
- Create logo placeholder text for partners/suppliers
- Optimize for fast loading and SEO
- Implement performance best practices

## Image Asset Structure

### Directory Organization
```
images/
├── logo.png                      # AutoViet logo (200x80px)
├── favicon.ico                   # 32x32px browser icon
├── products/
│   ├── product-01.jpg            # Unsplash: vending-machine,drinks
│   ├── product-02.jpg            # Unsplash: vending-machine,snacks
│   ├── product-03.jpg            # Unsplash: vending-machine,coffee
│   ├── product-04.jpg            # Unsplash: vending-machine,food
│   ├── product-05.jpg            # Unsplash: vending-machine,beverages
│   ├── product-06.jpg            # Unsplash: vending-machine,automated
│   ├── product-07.jpg            # Unsplash: vending-machine,technology
│   ├── product-08.jpg            # Unsplash: vending-machine,modern
│   ├── product-09.jpg            # Unsplash: vending-machine,retail
│   ├── product-10.jpg            # Unsplash: vending-machine,commercial
│   ├── product-11.jpg            # Unsplash: vending-machine,dispenser
│   ├── product-12.jpg            # Unsplash: vending-machine,kiosk
│   └── product-13.jpg            # Unsplash: vending-machine,smart
├── projects/
│   ├── project-01.jpg            # Unsplash: office,vending,corporate
│   ├── project-02.jpg            # Unsplash: hospital,cafeteria
│   ├── project-03.jpg            # Unsplash: factory,break-room
│   ├── project-04.jpg            # Unsplash: university,campus
│   ├── project-05.jpg            # Unsplash: hotel,lobby
│   ├── project-06.jpg            # Unsplash: airport,terminal
│   ├── project-07.jpg            # Unsplash: mall,shopping
│   └── project-08.jpg            # Unsplash: gym,fitness-center
├── partners/                     # Placeholder divs (no images initially)
└── suppliers/                    # Placeholder divs (no images initially)
```

## Unsplash Placeholder URLs

### Products Section (13 Machines)
```html
<!-- Use Unsplash Source API for random images -->
<img src="https://source.unsplash.com/400x300/?vending-machine,drinks&sig=1"
     alt="Máy bán nước giải khát" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,snacks&sig=2"
     alt="Máy bán đồ ăn vặt" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,coffee&sig=3"
     alt="Máy pha cà phê tự động" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,food&sig=4"
     alt="Máy bán thực phẩm" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,beverages&sig=5"
     alt="Máy bán nước uống" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,automated&sig=6"
     alt="Máy bán hàng tự động thông minh" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,technology&sig=7"
     alt="Máy vending công nghệ cao" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,modern&sig=8"
     alt="Máy bán hàng hiện đại" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,retail&sig=9"
     alt="Máy bán lẻ tự động" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,commercial&sig=10"
     alt="Máy vending thương mại" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,dispenser&sig=11"
     alt="Máy phân phối tự động" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,kiosk&sig=12"
     alt="Kiosk bán hàng tự động" loading="lazy">
<img src="https://source.unsplash.com/400x300/?vending-machine,smart&sig=13"
     alt="Máy vending thông minh" loading="lazy">
```

### Projects Section (8 Installations)
```html
<img src="https://source.unsplash.com/600x400/?office,modern,interior&sig=1"
     alt="Dự án văn phòng Luxshare ICT" loading="lazy">
<img src="https://source.unsplash.com/600x400/?hospital,corridor&sig=2"
     alt="Dự án bệnh viện Việt Đức" loading="lazy">
<img src="https://source.unsplash.com/600x400/?factory,industrial&sig=3"
     alt="Dự án nhà máy Foxconn" loading="lazy">
<img src="https://source.unsplash.com/600x400/?university,campus&sig=4"
     alt="Dự án trường Đại học Thương Mại" loading="lazy">
<img src="https://source.unsplash.com/600x400/?hotel,lobby&sig=5"
     alt="Dự án khách sạn Keangnam" loading="lazy">
<img src="https://source.unsplash.com/600x400/?airport,terminal&sig=6"
     alt="Dự án sân bay" loading="lazy">
<img src="https://source.unsplash.com/600x400/?mall,shopping&sig=7"
     alt="Dự án trung tâm thương mại" loading="lazy">
<img src="https://source.unsplash.com/600x400/?gym,fitness&sig=8"
     alt="Dự án phòng tập" loading="lazy">
```

## Partner/Supplier Logo Placeholders

### Partners List (35 Companies)
**Use CSS-styled text placeholders initially, replace with logos later**

```html
<!-- Sample partner cards -->
<div class="partner-logo"><div class="logo-placeholder">Luxshare ICT</div></div>
<div class="partner-logo"><div class="logo-placeholder">Foxconn</div></div>
<div class="partner-logo"><div class="logo-placeholder">Shunyun</div></div>
<div class="partner-logo"><div class="logo-placeholder">M.C Electronic</div></div>
<div class="partner-logo"><div class="logo-placeholder">UIL Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Samsung Electronic</div></div>
<div class="partner-logo"><div class="logo-placeholder">SDV</div></div>
<div class="partner-logo"><div class="logo-placeholder">SEMV</div></div>
<div class="partner-logo"><div class="logo-placeholder">Tenma Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Inoac Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Toyota Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Tập Đoàn Đóng Tàu Đại Dương</div></div>
<div class="partner-logo"><div class="logo-placeholder">BV Phúc Yên</div></div>
<div class="partner-logo"><div class="logo-placeholder">BV Việt Đức</div></div>
<div class="partner-logo"><div class="logo-placeholder">BV Ung Bướu HN</div></div>
<div class="partner-logo"><div class="logo-placeholder">Bảo Tàng Lịch Sử VN</div></div>
<div class="partner-logo"><div class="logo-placeholder">Keangnam Hà Nội</div></div>
<div class="partner-logo"><div class="logo-placeholder">PVI Cầu Giấy</div></div>
<div class="partner-logo"><div class="logo-placeholder">TTHN Quốc Gia</div></div>
<div class="partner-logo"><div class="logo-placeholder">NM Khóa Huy Hoàng</div></div>
<div class="partner-logo"><div class="logo-placeholder">Terumo Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Vietnam Post</div></div>
<div class="partner-logo"><div class="logo-placeholder">Mitsubishi VN</div></div>
<div class="partner-logo"><div class="logo-placeholder">Matsuo Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Fukang Hồng Hải</div></div>
<div class="partner-logo"><div class="logo-placeholder">Kyocera Hải Phòng</div></div>
<div class="partner-logo"><div class="logo-placeholder">Yazaki Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Shin-Etsu VN</div></div>
<div class="partner-logo"><div class="logo-placeholder">Pegatron Hải Phòng</div></div>
<div class="partner-logo"><div class="logo-placeholder">KCN Việt Nam</div></div>
<div class="partner-logo"><div class="logo-placeholder">Nakashima</div></div>
<div class="partner-logo"><div class="logo-placeholder">TKR Manufacturing</div></div>
<div class="partner-logo"><div class="logo-placeholder">Sakura Hongming</div></div>
<div class="partner-logo"><div class="logo-placeholder">Kyoei Manufacturing</div></div>
<div class="partner-logo"><div class="logo-placeholder">ĐH Thương Mại HN</div></div>
<!-- Abbreviated for brevity -->
```

### Suppliers List (25+ Companies)
```html
<div class="supplier-logo"><div class="logo-placeholder">Chí Vĩ</div></div>
<div class="supplier-logo"><div class="logo-placeholder">VHTek</div></div>
<div class="supplier-logo"><div class="logo-placeholder">TCN</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Xyngyuan</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Baiden</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Micron</div></div>
<div class="supplier-logo"><div class="logo-placeholder">L.E Vend</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Coca-Cola</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Pepsi</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Tân Hiệp Phát</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Masan</div></div>
<div class="supplier-logo"><div class="logo-placeholder">CP</div></div>
<div class="supplier-logo"><div class="logo-placeholder">NAVA</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Vihamark</div></div>
<div class="supplier-logo"><div class="logo-placeholder">PTT Foods</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Lof</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Nestlé</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Ajinomoto</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Kirin</div></div>
<div class="supplier-logo"><div class="logo-placeholder">TCP Redbull</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Taisho</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Hà Lương</div></div>
<div class="supplier-logo"><div class="logo-placeholder">Quang Hanh</div></div>
<div class="supplier-logo"><div class="logo-placeholder">VNPAY</div></div>
<div class="supplier-logo"><div class="logo-placeholder">BaoKim</div></div>
<div class="supplier-logo"><div class="logo-placeholder">MoMo</div></div>
```

## Performance Optimization

### 1. Image Optimization Guidelines
- **Logo**: PNG with transparency, max 50KB
- **Products**: JPEG, 400x300px, quality 80%, ~30-50KB each
- **Projects**: JPEG, 600x400px, quality 80%, ~50-80KB each
- **Total initial page weight target**: <500KB (before images load)
- **Lazy loading**: All images below fold use `loading="lazy"`

### 2. SEO Optimization

#### Meta Tags (in `<head>`)
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="AutoViet - Chuyên cung cấp dịch vụ máy bán hàng tự động: Bán, cho thuê, sửa chữa, bảo trì máy vending chuyên nghiệp tại Hà Nội. Liên hệ: 0865771995">
<meta name="keywords" content="máy bán hàng tự động, máy vending, cho thuê máy vending, sửa chữa máy vending, AutoViet, Hà Nội">
<meta name="author" content="AutoViet">

<!-- Open Graph (Facebook, LinkedIn) -->
<meta property="og:type" content="website">
<meta property="og:title" content="AutoViet - Dịch Vụ Máy Bán Hàng Tự Động">
<meta property="og:description" content="Chuyên cung cấp, cho thuê và bảo trì máy vending chuyên nghiệp">
<meta property="og:url" content="https://autoviet.vn">
<meta property="og:image" content="https://autoviet.vn/images/logo.png">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="AutoViet - Dịch Vụ Máy Bán Hàng Tự Động">
<meta name="twitter:description" content="Chuyên cung cấp, cho thuê và bảo trì máy vending chuyên nghiệp">

<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="/images/favicon.ico">
<link rel="apple-touch-icon" href="/images/logo.png">
```

#### Semantic HTML
- Use `<header>`, `<nav>`, `<section>`, `<article>`, `<footer>`
- One `<h1>` per page (hero headline)
- Proper heading hierarchy (h1 → h2 → h3)
- Descriptive alt text for all images

### 3. Performance Best Practices

#### CSS Optimization
```css
/* Use CSS containment for sections */
section { contain: layout style paint; }

/* Optimize animations */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

#### JavaScript Loading
```html
<!-- Load JS files at end of <body> -->
<script src="js/navigation.js" defer></script>
<script src="js/form.js" defer></script>
<script src="js/main.js" defer></script>
```

#### Critical CSS (Inline in `<head>`)
```html
<style>
  /* Inline critical above-fold styles */
  body { margin: 0; font-family: sans-serif; }
  .header { position: sticky; top: 0; background: white; }
  .hero { min-height: 500px; background: #000; }
</style>
```

### 4. Loading Strategy
1. **Immediate**: HTML, critical CSS, logo
2. **Deferred**: Non-critical CSS, JavaScript
3. **Lazy**: All images below hero section
4. **Preconnect**: Unsplash CDN
   ```html
   <link rel="preconnect" href="https://source.unsplash.com">
   ```

### 5. Accessibility
- ARIA labels for icon buttons
- Color contrast ratio ≥4.5:1 (WCAG AA)
- Focus visible styles for keyboard navigation
- Skip to content link (optional)

## Asset Replacement Roadmap

### Phase 1 (Launch)
- Use Unsplash placeholders for products/projects
- Text placeholders for partner/supplier logos
- Simple text-based logo if needed

### Phase 2 (Post-Launch)
- Replace Unsplash with real product photos
- Add actual company logos (with permission)
- Create custom AutoViet logo (or commission design)

### Phase 3 (Enhancement)
- Optimize all images with WebP format
- Add image srcset for responsive images
- Implement Progressive Web App (PWA) features

## Testing Checklist
- [ ] Google PageSpeed Insights score >90
- [ ] Mobile-friendly test passes
- [ ] All images have alt text
- [ ] Page loads in <3s on 3G
- [ ] No console errors
- [ ] Forms validate correctly
- [ ] Smooth scroll works on all browsers
- [ ] Responsive on 320px - 1920px+ screens
