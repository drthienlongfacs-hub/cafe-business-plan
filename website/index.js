/* 
================================================================================
CAFE CÓ GU - INTERACTIVE SCRIPT
Created: 2026-05-27
================================================================================
*/

document.addEventListener('DOMContentLoaded', () => {
  
  // --- Sticky Header on Scroll ---
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // --- Mobile Navigation Toggle ---
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  mobileToggle.addEventListener('click', () => {
    mobileToggle.classList.toggle('open');
    navMenu.classList.toggle('open');
  });

  // Close menu when clicking a link
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileToggle.classList.remove('open');
      navMenu.classList.remove('open');
    });
  });

  // --- Navigation Link Active Highlighter on Scroll ---
  const sections = document.querySelectorAll('section');
  
  const options = {
    root: null,
    threshold: 0.25,
    rootMargin: "-80px 0px 0px 0px"
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, options);

  sections.forEach(section => {
    observer.observe(section);
  });

  // --- F&B Menu Tab Switcher ---
  const tabButtons = document.querySelectorAll('.menu-tab-btn');
  const menuContainers = document.querySelectorAll('.menu-container');

  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const tabTarget = button.getAttribute('data-tab');
      
      // Toggle active button
      tabButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');

      // Toggle active menu container
      menuContainers.forEach(container => {
        if (container.getAttribute('id') === `${tabTarget}-menu`) {
          container.classList.add('active');
        } else {
          container.classList.remove('active');
        }
      });
    });
  });

  // --- English Programs Accordion ---
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isActive = item.classList.contains('active');

      // Close all items
      document.querySelectorAll('.accordion-item').forEach(accItem => {
        accItem.classList.remove('active');
      });

      // Toggle current item
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // --- Image Lightbox Modal ---
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.querySelector('.lightbox');
  const lightboxImg = document.querySelector('.lightbox-img');
  const lightboxCaption = document.querySelector('.lightbox-caption');
  const lightboxClose = document.querySelector('.lightbox-close');

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const imgSrc = item.querySelector('img').getAttribute('src');
      const captionText = item.querySelector('.gallery-overlay h4').textContent;
      
      lightboxImg.setAttribute('src', imgSrc);
      lightboxCaption.textContent = captionText;
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden'; // Lock scroll
    });
  });

  const closeLightbox = () => {
    lightbox.classList.remove('active');
    document.body.style.overflow = ''; // Unlock scroll
  };

  lightboxClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });

  // --- FAMILY COMBO DYNAMIC CALCULATOR ---
  const beveragesInput = document.getElementById('beverages-qty');
  const kidzoneInput = document.getElementById('kidzone-qty');
  const englishInput = document.getElementById('english-qty');
  const dayTypeItems = document.querySelectorAll('.selector-item');
  
  const labelBeverages = document.getElementById('label-beverages');
  const labelKidzone = document.getElementById('label-kidzone');
  const labelEnglish = document.getElementById('label-english');
  
  const resultBeveragesVal = document.getElementById('res-beverages-val');
  const resultKidzoneVal = document.getElementById('res-kidzone-val');
  const resultEnglishVal = document.getElementById('res-english-val');
  const resultSubtotalVal = document.getElementById('res-subtotal-val');
  const resultDiscountVal = document.getElementById('res-discount-val');
  const resultTotalVal = document.getElementById('res-total-val');
  
  let activeDayType = 'weekday'; // Default

  // Pricing constants (matches SOT/Business Plan)
  const PRICE_BEVERAGE = 49000;   // Average drink (latte, tea, juice)
  const PRICE_KIDZONE_WEEKDAY = 69000;
  const PRICE_KIDZONE_WEEKEND = 89000;
  const PRICE_ENGLISH_SESSION = 79000; // Average session price (Mini Quiz/After-School)
  const PROMO_DISCOUNT_RATE = 0.30;     // 30% Month 1 Opening discount

  // Format currency VN number style (e.g. 150.000)
  const formatCurrency = (number) => {
    return new Intl.NumberFormat('vi-VN').format(number);
  };

  const calculateCombo = () => {
    const qtyBeverages = parseInt(beveragesInput.value);
    const qtyKidzone = parseInt(kidzoneInput.value);
    const qtyEnglish = parseInt(englishInput.value);
    
    // Determine kidzone unit price based on selected day type
    const unitPriceKidzone = activeDayType === 'weekday' ? PRICE_KIDZONE_WEEKDAY : PRICE_KIDZONE_WEEKEND;
    
    // Calculate intermediate sums
    const costBeverages = qtyBeverages * PRICE_BEVERAGE;
    const costKidzone = qtyKidzone * unitPriceKidzone;
    const costEnglish = qtyEnglish * PRICE_ENGLISH_SESSION;
    
    const subtotal = costBeverages + costKidzone + costEnglish;
    const discount = subtotal * PROMO_DISCOUNT_RATE;
    const total = subtotal - discount;

    // Update Slider Labels
    labelBeverages.textContent = `${qtyBeverages} cốc`;
    labelKidzone.textContent = `${qtyKidzone} bé`;
    labelEnglish.textContent = `${qtyEnglish} ca`;

    // Update Results Sidebar
    resultBeveragesVal.textContent = `${qtyBeverages} × ${formatCurrency(PRICE_BEVERAGE)} đ = ${formatCurrency(costBeverages)} đ`;
    resultKidzoneVal.textContent = `${qtyKidzone} × ${formatCurrency(unitPriceKidzone)} đ = ${formatCurrency(costKidzone)} đ`;
    resultEnglishVal.textContent = `${qtyEnglish} × ${formatCurrency(PRICE_ENGLISH_SESSION)} đ = ${formatCurrency(costEnglish)} đ`;
    
    resultSubtotalVal.textContent = `${formatCurrency(subtotal)} đ`;
    resultDiscountVal.textContent = `-${formatCurrency(discount)} đ`;
    resultTotalVal.textContent = `${formatCurrency(total)} đ`;
  };

  // Setup selector listeners
  dayTypeItems.forEach(item => {
    item.addEventListener('click', () => {
      dayTypeItems.forEach(el => el.classList.remove('active'));
      item.classList.add('active');
      activeDayType = item.getAttribute('data-day');
      calculateCombo();
    });
  });

  // Setup input slider listeners
  beveragesInput.addEventListener('input', calculateCombo);
  kidzoneInput.addEventListener('input', calculateCombo);
  englishInput.addEventListener('input', calculateCombo);

  // Run initial calculation
  calculateCombo();

  // --- CONTACT FORM & SUBMISSION ---
  const contactForm = document.getElementById('cafe-contact-form');
  
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('form-name').value;
      const phone = document.getElementById('form-phone').value;
      const message = document.getElementById('form-message').value;

      if (!name || !phone) {
        alert('Vui lòng nhập đầy đủ Tên và Số điện thoại liên hệ.');
        return;
      }

      // Simulate sending
      const submitBtn = contactForm.querySelector('.submit-btn');
      const originalText = submitBtn.textContent;
      submitBtn.textContent = 'Đang gửi thông tin...';
      submitBtn.disabled = true;

      setTimeout(() => {
        submitBtn.textContent = 'Đã gửi thành công ✅';
        submitBtn.style.backgroundColor = '#16a34a';
        submitBtn.style.color = '#ffffff';

        // Clear fields
        contactForm.reset();

        setTimeout(() => {
          submitBtn.textContent = originalText;
          submitBtn.style.backgroundColor = '';
          submitBtn.style.color = '';
          submitBtn.disabled = false;
          alert(`Cảm ơn anh/chị ${name}! Cafe Có Gu đã nhận được thông tin đặt bàn/đóng góp ý kiến và sẽ phản hồi lại ngay qua số điện thoại ${phone}.`);
        }, 2000);
      }, 1500);
    });
  }

  // --- SCROLL REVEAL ANIMATIONS ---
  const revealElements = document.querySelectorAll('.reveal');
  
  const revealOptions = {
    root: null,
    threshold: 0.15,
    rootMargin: "0px"
  };

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        revealObserver.unobserve(entry.target); // Animate only once
      }
    });
  }, revealOptions);

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });
});
