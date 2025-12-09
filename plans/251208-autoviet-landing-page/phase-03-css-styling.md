# Phase 03 - CSS Styling (Orange/Black Theme)

## Objectives
- Implement mobile-first responsive design
- Apply orange (#FF6B00) and black (#000, #1a1a1a) color scheme
- Create consistent spacing, typography, component styles
- Ensure smooth transitions and hover effects

## CSS File Organization

### 1. reset.css
```css
/* CSS normalization */
- Reset default browser styles
- Box-sizing: border-box for all elements
- Remove margins/paddings on body, headings, lists
- Set line-height: 1.6 for better readability
```

### 2. variables.css
```css
:root {
  /* Colors */
  --primary-orange: #FF6B00;
  --primary-black: #000000;
  --secondary-black: #1a1a1a;
  --accent-white: #FFFFFF;
  --gray-light: #f5f5f5;
  --gray-dark: #333333;
  --border-color: #e0e0e0;

  /* Typography */
  --font-primary: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  --font-size-base: 16px;
  --font-size-sm: 14px;
  --font-size-lg: 18px;
  --font-size-xl: 24px;
  --font-size-2xl: 32px;
  --font-size-3xl: 48px;

  /* Spacing */
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 32px;
  --spacing-xl: 48px;
  --spacing-2xl: 64px;

  /* Layout */
  --container-width: 1200px;
  --border-radius: 8px;
  --box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
}
```

### 3. main.css

#### Global Styles
```css
body {
  font-family: var(--font-primary);
  font-size: var(--font-size-base);
  color: var(--secondary-black);
  background: var(--accent-white);
  line-height: 1.6;
}

.container {
  width: 100%;
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 var(--spacing-sm);
}

h1, h2, h3 { font-weight: 700; line-height: 1.2; }
h1 { font-size: var(--font-size-3xl); }
h2 { font-size: var(--font-size-2xl); margin-bottom: var(--spacing-lg); }
h3 { font-size: var(--font-size-xl); }

section { padding: var(--spacing-2xl) 0; }
```

#### Header & Navigation
```css
.header {
  position: sticky;
  top: 0;
  background: var(--accent-white);
  box-shadow: var(--box-shadow);
  z-index: 1000;
}

.navbar {
  padding: var(--spacing-sm) 0;
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo img {
  height: 50px;
  width: auto;
}

.menu-toggle {
  display: none; /* Show on mobile */
  background: none;
  border: none;
  font-size: var(--font-size-2xl);
  cursor: pointer;
}

.nav-menu {
  display: flex;
  gap: var(--spacing-md);
  list-style: none;
}

.nav-menu a {
  text-decoration: none;
  color: var(--secondary-black);
  font-weight: 500;
  transition: var(--transition);
}

.nav-menu a:hover {
  color: var(--primary-orange);
}

.cta-button {
  background: var(--primary-orange);
  color: var(--accent-white) !important;
  padding: var(--spacing-xs) var(--spacing-md);
  border-radius: var(--border-radius);
}

.cta-button:hover {
  background: #e55f00;
}
```

#### Hero Section
```css
.hero {
  background: linear-gradient(135deg, var(--primary-black) 0%, var(--secondary-black) 100%);
  color: var(--accent-white);
  text-align: center;
  padding: var(--spacing-2xl) 0;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero h1 {
  margin-bottom: var(--spacing-md);
  color: var(--accent-white);
}

.hero .tagline {
  font-size: var(--font-size-lg);
  margin-bottom: var(--spacing-lg);
  color: var(--gray-light);
}

.hero-cta {
  display: inline-block;
  background: var(--primary-orange);
  color: var(--accent-white);
  padding: var(--spacing-sm) var(--spacing-xl);
  text-decoration: none;
  border-radius: var(--border-radius);
  font-size: var(--font-size-lg);
  font-weight: 600;
  transition: var(--transition);
}

.hero-cta:hover {
  background: #e55f00;
  transform: translateY(-2px);
}
```

#### Stats Section
```css
.stats {
  background: var(--gray-light);
}

.stats .container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-lg);
  text-align: center;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-number {
  font-size: var(--font-size-3xl);
  font-weight: 700;
  color: var(--primary-orange);
}

.stat-label {
  font-size: var(--font-size-lg);
  color: var(--gray-dark);
  margin-top: var(--spacing-xs);
}
```

#### Services Section
```css
.services { text-align: center; }

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--spacing-md);
}

.service-card {
  background: var(--accent-white);
  padding: var(--spacing-lg);
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  transition: var(--transition);
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.service-icon {
  font-size: 48px;
  margin-bottom: var(--spacing-sm);
}

.service-card h3 {
  color: var(--primary-orange);
  margin-bottom: var(--spacing-sm);
}
```

#### Products Section
```css
.products { background: var(--gray-light); }

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--spacing-md);
}

.product-card {
  background: var(--accent-white);
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--box-shadow);
  transition: var(--transition);
}

.product-card:hover {
  transform: scale(1.03);
}

.product-card img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.product-card h3 {
  padding: var(--spacing-sm);
  text-align: center;
  color: var(--secondary-black);
}
```

#### Projects Section
```css
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: var(--spacing-lg);
}

.project-card {
  position: relative;
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--box-shadow);
}

.project-card img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  transition: var(--transition);
}

.project-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
  padding: var(--spacing-md);
  color: var(--accent-white);
  transform: translateY(100%);
  transition: var(--transition);
}

.project-card:hover .project-overlay {
  transform: translateY(0);
}

.project-card:hover img {
  transform: scale(1.1);
}
```

#### Partners & Suppliers Sections
```css
.partners, .suppliers {
  background: var(--accent-white);
}

.partners-grid, .suppliers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: var(--spacing-md);
}

.partner-logo, .supplier-logo {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-md);
  background: var(--gray-light);
  border-radius: var(--border-radius);
  min-height: 100px;
}

.logo-placeholder {
  font-size: var(--font-size-sm);
  font-weight: 600;
  color: var(--gray-dark);
  text-align: center;
}
```

#### About Section
```css
.about { background: var(--gray-light); }

.about-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--spacing-xl);
}

.about-text p {
  margin-bottom: var(--spacing-md);
  line-height: 1.8;
}

.about-info {
  background: var(--accent-white);
  padding: var(--spacing-lg);
  border-radius: var(--border-radius);
  border-left: 4px solid var(--primary-orange);
}

.about-info p {
  margin-bottom: var(--spacing-sm);
}
```

#### Contact Section
```css
.contact { background: var(--accent-white); }

.contact-wrapper {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--spacing-xl);
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: var(--spacing-xs);
  font-weight: 600;
  color: var(--secondary-black);
}

.form-group input,
.form-group textarea {
  padding: var(--spacing-sm);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  font-size: var(--font-size-base);
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-orange);
}

.error-message {
  color: #dc3545;
  font-size: var(--font-size-sm);
  margin-top: var(--spacing-xs);
  display: none;
}

.submit-button {
  background: var(--primary-orange);
  color: var(--accent-white);
  padding: var(--spacing-sm) var(--spacing-lg);
  border: none;
  border-radius: var(--border-radius);
  font-size: var(--font-size-lg);
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}

.submit-button:hover {
  background: #e55f00;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-lg);
}

.contact-item h3 {
  color: var(--primary-orange);
  margin-bottom: var(--spacing-xs);
}
```

#### Footer
```css
.footer {
  background: var(--primary-black);
  color: var(--accent-white);
  padding: var(--spacing-xl) 0 var(--spacing-md);
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-lg);
}

.footer-section h3 {
  color: var(--primary-orange);
  margin-bottom: var(--spacing-sm);
}

.footer-section ul {
  list-style: none;
}

.footer-section a {
  color: var(--accent-white);
  text-decoration: none;
  transition: var(--transition);
}

.footer-section a:hover {
  color: var(--primary-orange);
}

.footer-bottom {
  text-align: center;
  padding-top: var(--spacing-md);
  border-top: 1px solid var(--gray-dark);
}
```

### 4. responsive.css

#### Tablet (768px - 1023px)
```css
@media (max-width: 1023px) {
  .services-grid { grid-template-columns: repeat(2, 1fr); }
  .footer-content { grid-template-columns: repeat(2, 1fr); }
  .about-content { grid-template-columns: 1fr; }
  .contact-wrapper { grid-template-columns: 1fr; }
  .partners-grid, .suppliers-grid {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  }
}
```

#### Mobile (320px - 767px)
```css
@media (max-width: 767px) {
  :root {
    --font-size-3xl: 32px;
    --font-size-2xl: 24px;
    --font-size-xl: 20px;
  }

  .menu-toggle { display: block; }

  .nav-menu {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    flex-direction: column;
    background: var(--accent-white);
    box-shadow: var(--box-shadow);
    padding: var(--spacing-sm);
    display: none;
  }

  .nav-menu.active { display: flex; }

  .hero { padding: var(--spacing-xl) 0; min-height: 400px; }
  .stats .container { grid-template-columns: 1fr; gap: var(--spacing-md); }
  .services-grid { grid-template-columns: 1fr; }
  .products-grid { grid-template-columns: 1fr; }
  .projects-grid { grid-template-columns: 1fr; }
  .partners-grid, .suppliers-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .footer-content { grid-template-columns: 1fr; }
}
```

## Design Principles
- **Mobile-first**: Base styles for 320px+, progressively enhance for larger screens
- **Orange accents**: Use #FF6B00 for CTAs, headings, hover states
- **High contrast**: Black/white for readability, orange for emphasis
- **Consistent spacing**: Use CSS variables for uniform margins/padding
- **Smooth transitions**: 0.3s ease on interactive elements
- **Card-based**: Services, products, projects use card components
- **Grid layouts**: Flexible, responsive grids with auto-fit/auto-fill
