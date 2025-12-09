# Phase 04 - JavaScript Interactions

## Objectives
- Implement mobile menu toggle
- Add smooth scroll navigation
- Validate contact form (frontend)
- Lazy load images
- Add scroll-to-top button
- Animate stats on scroll into view

## JavaScript File Organization

### 1. navigation.js
**Purpose:** Handle menu toggle and smooth scroll

```javascript
// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('.nav-menu');

menuToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
});

// Close menu when clicking nav link (mobile)
const navLinks = document.querySelectorAll('.nav-menu a');
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    if (window.innerWidth <= 767) {
      navMenu.classList.remove('active');
    }
  });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const headerHeight = document.querySelector('.header').offsetHeight;
      const targetPosition = target.offsetTop - headerHeight;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  });
});

// Sticky header shadow on scroll
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
});
```

**CSS Addition for scrolled header:**
```css
.header.scrolled {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
```

### 2. form.js
**Purpose:** Contact form validation and submission handling

```javascript
const contactForm = document.getElementById('contact-form');

// Validation rules
const validators = {
  name: (value) => {
    if (!value.trim()) return 'Vui lòng nhập họ và tên';
    if (value.length < 2) return 'Họ và tên phải có ít nhất 2 ký tự';
    return null;
  },

  phone: (value) => {
    if (!value.trim()) return 'Vui lòng nhập số điện thoại';
    const phoneRegex = /^[0-9]{10,11}$/;
    if (!phoneRegex.test(value.replace(/\s/g, ''))) {
      return 'Số điện thoại không hợp lệ (10-11 chữ số)';
    }
    return null;
  },

  email: (value) => {
    if (!value.trim()) return 'Vui lòng nhập email';
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(value)) {
      return 'Email không hợp lệ';
    }
    return null;
  },

  message: (value) => {
    if (!value.trim()) return 'Vui lòng nhập nội dung';
    if (value.length < 10) return 'Nội dung phải có ít nhất 10 ký tự';
    return null;
  }
};

// Show error message
function showError(input, message) {
  const formGroup = input.parentElement;
  const errorElement = formGroup.querySelector('.error-message');
  errorElement.textContent = message;
  errorElement.style.display = 'block';
  input.style.borderColor = '#dc3545';
}

// Clear error message
function clearError(input) {
  const formGroup = input.parentElement;
  const errorElement = formGroup.querySelector('.error-message');
  errorElement.textContent = '';
  errorElement.style.display = 'none';
  input.style.borderColor = '#e0e0e0';
}

// Validate single field
function validateField(input) {
  const fieldName = input.name;
  const value = input.value;
  const error = validators[fieldName](value);

  if (error) {
    showError(input, error);
    return false;
  } else {
    clearError(input);
    return true;
  }
}

// Real-time validation on blur
contactForm.querySelectorAll('input, textarea').forEach(input => {
  input.addEventListener('blur', () => {
    validateField(input);
  });

  // Clear error on input
  input.addEventListener('input', () => {
    if (input.style.borderColor === 'rgb(220, 53, 69)') {
      clearError(input);
    }
  });
});

// Form submission
contactForm.addEventListener('submit', (e) => {
  e.preventDefault();

  let isValid = true;
  const formData = {};

  // Validate all fields
  contactForm.querySelectorAll('input, textarea').forEach(input => {
    if (!validateField(input)) {
      isValid = false;
    }
    formData[input.name] = input.value;
  });

  if (isValid) {
    // Success message (since no backend)
    alert('Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi sớm nhất.');

    // Log form data (for demo purposes)
    console.log('Form submitted:', formData);

    // Reset form
    contactForm.reset();

    // Optional: Send to external service (e.g., Formspree, EmailJS)
    // fetch('https://formspree.io/f/YOUR_FORM_ID', {
    //   method: 'POST',
    //   body: JSON.stringify(formData),
    //   headers: { 'Content-Type': 'application/json' }
    // });
  } else {
    // Scroll to first error
    const firstError = contactForm.querySelector('.error-message[style*="block"]');
    if (firstError) {
      firstError.parentElement.querySelector('input, textarea').focus();
    }
  }
});
```

### 3. main.js
**Purpose:** Image lazy loading, scroll animations, scroll-to-top button

```javascript
// Lazy load images
const lazyImages = document.querySelectorAll('img[loading="lazy"]');

if ('IntersectionObserver' in window) {
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src || img.src;
        img.classList.add('loaded');
        observer.unobserve(img);
      }
    });
  });

  lazyImages.forEach(img => imageObserver.observe(img));
} else {
  // Fallback for older browsers
  lazyImages.forEach(img => {
    img.src = img.dataset.src || img.src;
  });
}

// Animate stats counter on scroll into view
const statsSection = document.querySelector('.stats');
const statNumbers = document.querySelectorAll('.stat-number');
let statsAnimated = false;

function animateStats() {
  statNumbers.forEach(stat => {
    const target = parseInt(stat.textContent);
    const increment = target / 50; // Animate over ~50 frames
    let current = 0;

    const updateCounter = () => {
      current += increment;
      if (current < target) {
        stat.textContent = Math.floor(current) + '+';
        requestAnimationFrame(updateCounter);
      } else {
        stat.textContent = target + '+';
      }
    };

    updateCounter();
  });
}

// Observe stats section
if (statsSection) {
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !statsAnimated) {
        animateStats();
        statsAnimated = true;
      }
    });
  }, { threshold: 0.5 });

  statsObserver.observe(statsSection);
}

// Scroll-to-top button
const scrollTopBtn = document.createElement('button');
scrollTopBtn.className = 'scroll-top-btn';
scrollTopBtn.innerHTML = '↑';
scrollTopBtn.setAttribute('aria-label', 'Scroll to top');
document.body.appendChild(scrollTopBtn);

// Show/hide button based on scroll position
window.addEventListener('scroll', () => {
  if (window.scrollY > 500) {
    scrollTopBtn.classList.add('visible');
  } else {
    scrollTopBtn.classList.remove('visible');
  }
});

// Scroll to top on click
scrollTopBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});

// Fade-in animation for sections on scroll
const sections = document.querySelectorAll('section');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('fade-in');
    }
  });
}, { threshold: 0.1 });

sections.forEach(section => {
  section.classList.add('fade-in-init');
  sectionObserver.observe(section);
});
```

**CSS Additions for scroll-to-top and fade-in:**
```css
/* Scroll-to-top button */
.scroll-top-btn {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  background: var(--primary-orange);
  color: var(--accent-white);
  border: none;
  border-radius: 50%;
  font-size: 24px;
  cursor: pointer;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 999;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.scroll-top-btn.visible {
  opacity: 1;
  visibility: visible;
}

.scroll-top-btn:hover {
  background: #e55f00;
  transform: translateY(-3px);
}

/* Fade-in animation */
.fade-in-init {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.fade-in {
  opacity: 1;
  transform: translateY(0);
}
```

## Feature Summary

### 1. Mobile Menu Toggle
- Hamburger icon toggles `.active` class on nav menu
- Menu closes automatically when nav link clicked (mobile only)
- Smooth transitions for open/close

### 2. Smooth Scroll Navigation
- All anchor links scroll smoothly to target section
- Accounts for sticky header height
- Works with all internal links (nav, CTA buttons)

### 3. Contact Form Validation
- Real-time validation on blur
- Vietnamese error messages
- Validates: name (min 2 chars), phone (10-11 digits), email (format), message (min 10 chars)
- Prevents submission if invalid
- Shows success message on valid submission
- Resets form after submission

### 4. Lazy Loading
- Uses Intersection Observer API
- Images load only when entering viewport
- Fallback for older browsers

### 5. Stats Counter Animation
- Numbers animate from 0 to target value
- Triggers once when section enters viewport
- Uses requestAnimationFrame for smooth animation

### 6. Scroll-to-Top Button
- Appears after scrolling 500px down
- Fixed position bottom-right
- Smooth scroll to page top
- Orange circular button with arrow icon

### 7. Scroll Animations
- Sections fade in as they enter viewport
- Uses Intersection Observer
- Subtle translateY animation

## Performance Considerations
- Debounce scroll events if needed
- Use passive event listeners where possible
- Minimize DOM queries (cache selectors)
- Use CSS transforms for animations (GPU accelerated)

## Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Fallbacks for Intersection Observer (IE11 not supported)
- ES6 features (arrow functions, const/let, template literals)
- Polyfills can be added if legacy support needed
