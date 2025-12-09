# Phase 02 - HTML Content Structure

## Objectives
- Semantic HTML5 markup
- Proper heading hierarchy (h1 → h6)
- SEO meta tags
- Accessibility attributes (alt, aria-labels)
- Content structure for all 11 sections

## HTML Document Structure

### Head Section
```html
- Meta charset, viewport, description
- Title: "AutoViet - Dịch Vụ Máy Bán Hàng Tự Động | Bán, Thuê, Sửa Chữa"
- Meta description (150-160 chars)
- Open Graph tags for social sharing
- Favicon link
- CSS files: reset.css, variables.css, main.css, responsive.css
```

### Body Sections

#### 1. Header
```html
<header id="header" class="header">
  <nav class="navbar">
    <div class="container">
      <a href="#" class="logo">
        <img src="images/logo.png" alt="AutoViet Logo">
      </a>
      <button class="menu-toggle" aria-label="Menu">☰</button>
      <ul class="nav-menu">
        <li><a href="#hero">Trang Chủ</a></li>
        <li><a href="#services">Dịch Vụ</a></li>
        <li><a href="#products">Sản Phẩm</a></li>
        <li><a href="#projects">Dự Án</a></li>
        <li><a href="#about">Về Chúng Tôi</a></li>
        <li><a href="#contact" class="cta-button">Liên Hệ</a></li>
      </ul>
    </div>
  </nav>
</header>
```

#### 2. Hero Section
```html
<section id="hero" class="hero">
  <div class="container">
    <h1>Giải Pháp Máy Bán Hàng Tự Động Hàng Đầu Việt Nam</h1>
    <p class="tagline">Chuyên cung cấp, cho thuê và bảo trì máy vending chuyên nghiệp</p>
    <a href="#contact" class="hero-cta">Nhận Tư Vấn Miễn Phí</a>
  </div>
</section>
```

#### 3. Stats Section
```html
<section id="stats" class="stats">
  <div class="container">
    <div class="stat-item">
      <span class="stat-number">500+</span>
      <span class="stat-label">Máy Triển Khai</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">35+</span>
      <span class="stat-label">Đối Tác</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">5+</span>
      <span class="stat-label">Năm Kinh Nghiệm</span>
    </div>
  </div>
</section>
```

#### 4. Services Section
```html
<section id="services" class="services">
  <div class="container">
    <h2>Dịch Vụ Của Chúng Tôi</h2>
    <div class="services-grid">
      <div class="service-card">
        <div class="service-icon">🛒</div>
        <h3>Bán Máy Vending</h3>
        <p>Cung cấp đa dạng loại máy bán hàng tự động chất lượng cao</p>
      </div>
      <div class="service-card">
        <div class="service-icon">📦</div>
        <h3>Cho Thuê Máy</h3>
        <p>Giải pháp linh hoạt cho doanh nghiệp và sự kiện ngắn hạn</p>
      </div>
      <div class="service-card">
        <div class="service-icon">🔧</div>
        <h3>Sửa Chữa</h3>
        <p>Dịch vụ sửa chữa nhanh chóng, chuyên nghiệp 24/7</p>
      </div>
      <div class="service-card">
        <div class="service-icon">⚙️</div>
        <h3>Bảo Trì</h3>
        <p>Gói bảo trì định kỳ đảm bảo máy hoạt động tối ưu</p>
      </div>
    </div>
  </div>
</section>
```

#### 5. Products Section
```html
<section id="products" class="products">
  <div class="container">
    <h2>Sản Phẩm Máy Vending</h2>
    <div class="products-grid">
      <!-- Repeat 13 times with different product names -->
      <div class="product-card">
        <img src="https://source.unsplash.com/400x300/?vending-machine,1"
             alt="Máy bán nước giải khát" loading="lazy">
        <h3>Máy Bán Nước Giải Khát</h3>
      </div>
      <!-- Additional 12 products with unique images -->
    </div>
  </div>
</section>
```

#### 6. Projects Section
```html
<section id="projects" class="projects">
  <div class="container">
    <h2>Dự Án Đã Triển Khai</h2>
    <div class="projects-grid">
      <!-- 6-8 project images from Unsplash -->
      <div class="project-card">
        <img src="https://source.unsplash.com/600x400/?office,vending"
             alt="Dự án tại văn phòng" loading="lazy">
        <div class="project-overlay">
          <h3>Văn Phòng Luxshare ICT</h3>
        </div>
      </div>
      <!-- Additional projects -->
    </div>
  </div>
</section>
```

#### 7. Partners Section
```html
<section id="partners" class="partners">
  <div class="container">
    <h2>Đối Tác Của Chúng Tôi</h2>
    <div class="partners-grid">
      <!-- 35+ logos (use placeholder divs with company names) -->
      <div class="partner-logo">
        <div class="logo-placeholder">Luxshare ICT</div>
      </div>
      <div class="partner-logo">
        <div class="logo-placeholder">Foxconn</div>
      </div>
      <!-- Repeat for all 35+ partners -->
    </div>
  </div>
</section>
```

#### 8. Suppliers Section
```html
<section id="suppliers" class="suppliers">
  <div class="container">
    <h2>Nhà Cung Cấp</h2>
    <div class="suppliers-grid">
      <!-- 25+ supplier logos (placeholder divs) -->
      <div class="supplier-logo">
        <div class="logo-placeholder">Chí Vĩ</div>
      </div>
      <!-- Repeat for all suppliers -->
    </div>
  </div>
</section>
```

#### 9. About Section
```html
<section id="about" class="about">
  <div class="container">
    <h2>Về AutoViet</h2>
    <div class="about-content">
      <div class="about-text">
        <p>CÔNG TY TNHH DỊCH VỤ & CÔNG NGHỆ TỰ ĐỘNG VIỆT (AutoViet) được thành lập
        ngày 04/11/2025, chuyên cung cấp giải pháp máy bán hàng tự động toàn diện.</p>
        <p>Với kinh nghiệm và đội ngũ chuyên môn cao, chúng tôi cam kết mang đến
        dịch vụ tốt nhất cho khách hàng.</p>
      </div>
      <div class="about-info">
        <p><strong>MST:</strong> 0111272009</p>
        <p><strong>Điện thoại:</strong> 0865771995</p>
        <p><strong>Địa chỉ:</strong> Số 10 ngõ Cây Đa 6, Thôn Lập Trí,
        Xã Kim Anh, Hà Nội</p>
      </div>
    </div>
  </div>
</section>
```

#### 10. Contact Section
```html
<section id="contact" class="contact">
  <div class="container">
    <h2>Liên Hệ Với Chúng Tôi</h2>
    <div class="contact-wrapper">
      <form id="contact-form" class="contact-form">
        <div class="form-group">
          <label for="name">Họ và Tên *</label>
          <input type="text" id="name" name="name" required>
          <span class="error-message"></span>
        </div>
        <div class="form-group">
          <label for="phone">Số Điện Thoại *</label>
          <input type="tel" id="phone" name="phone" required>
          <span class="error-message"></span>
        </div>
        <div class="form-group">
          <label for="email">Email *</label>
          <input type="email" id="email" name="email" required>
          <span class="error-message"></span>
        </div>
        <div class="form-group">
          <label for="message">Nội Dung *</label>
          <textarea id="message" name="message" rows="5" required></textarea>
          <span class="error-message"></span>
        </div>
        <button type="submit" class="submit-button">Gửi Liên Hệ</button>
      </form>
      <div class="contact-info">
        <div class="contact-item">
          <h3>📞 Hotline</h3>
          <p>0865771995</p>
        </div>
        <div class="contact-item">
          <h3>📍 Địa Chỉ</h3>
          <p>Số 10 ngõ Cây Đa 6, Thôn Lập Trí<br>
          Xã Kim Anh, Hà Nội</p>
        </div>
        <div class="contact-item">
          <h3>⏰ Giờ Làm Việc</h3>
          <p>Thứ 2 - Thứ 6: 8:00 - 17:30<br>
          Thứ 7: 8:00 - 12:00</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

#### 11. Footer
```html
<footer id="footer" class="footer">
  <div class="container">
    <div class="footer-content">
      <div class="footer-section">
        <h3>AutoViet</h3>
        <p>Giải pháp máy bán hàng tự động hàng đầu</p>
      </div>
      <div class="footer-section">
        <h3>Liên Kết</h3>
        <ul>
          <li><a href="#services">Dịch Vụ</a></li>
          <li><a href="#products">Sản Phẩm</a></li>
          <li><a href="#projects">Dự Án</a></li>
          <li><a href="#about">Về Chúng Tôi</a></li>
        </ul>
      </div>
      <div class="footer-section">
        <h3>Thông Tin</h3>
        <p>MST: 0111272009</p>
        <p>ĐT: 0865771995</p>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 AutoViet. All rights reserved.</p>
    </div>
  </div>
</footer>
```

### JavaScript References
```html
<!-- Before closing </body> -->
<script src="js/navigation.js"></script>
<script src="js/form.js"></script>
<script src="js/main.js"></script>
```

## Content Guidelines
- All text in Vietnamese
- Use proper Vietnamese diacritics
- Phone format: 0865771995 (no spaces/dashes)
- Tax ID: 0111272009
- Professional tone, customer-focused messaging

## Accessibility Requirements
- All images have descriptive alt text
- Form inputs have associated labels
- Semantic HTML5 elements (header, nav, section, footer)
- ARIA labels for icon buttons
- Keyboard navigation support
