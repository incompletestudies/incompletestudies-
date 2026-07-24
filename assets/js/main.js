// ─── main.js ───
// Journal of Incomplete Studies - Interactive Enhancements
// All features are progressive enhancements - site works without JS

document.addEventListener('DOMContentLoaded', function() {
  
  // ─── Check if we're in a browser environment ───
  if (typeof window === 'undefined') return;
  
  // ─── 1. TOPBAR NAVIGATION ───
  // Highlight active nav tab based on current page
  const navTabs = document.querySelectorAll('.nav-tab');
  const currentPath = window.location.pathname;
  
  navTabs.forEach(tab => {
    const tabHref = tab.getAttribute('data-href') || tab.getAttribute('href');
    if (tabHref && currentPath.includes(tabHref) && tabHref !== '/') {
      tab.classList.add('active');
    } else if (tabHref === '/' && currentPath === '/') {
      tab.classList.add('active');
    }
    
    // Click handler for nav tabs
    tab.addEventListener('click', function(e) {
      const href = this.getAttribute('data-href') || this.getAttribute('href');
      if (href && !href.startsWith('#')) {
        // Let the browser handle navigation
        return;
      }
      e.preventDefault();
      navTabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');
    });
  });
  
  // ─── 2. PULSE ANIMATION ───
  // Ensure pulse animations run smoothly
  const pulses = document.querySelectorAll('.topbar-mark-pulse, .pill.live, .home-index-status.live');
  pulses.forEach(pulse => {
    // Add a small random delay to avoid all pulsing at once
    const delay = Math.random() * 0.5;
    pulse.style.animationDelay = delay + 's';
  });
  
  // ─── 3. PROJECT CARDS ───
  // Add click feedback to project cards
  const projectCards = document.querySelectorAll('.home-project-card, .card, .proj-card, .sg-card');
  projectCards.forEach(card => {
    card.addEventListener('click', function(e) {
      // Don't interfere with internal links
      if (e.target.closest('a')) return;
      
      // Add a subtle scale effect
      this.style.transform = 'scale(0.98)';
      setTimeout(() => {
        this.style.transform = '';
      }, 150);
    });
  });
  
  // ─── 4. BREADCRUMB NAVIGATION ───
  // Smooth scroll to top when clicking breadcrumb home
  const breadcrumbLinks = document.querySelectorAll('.breadcrumb a');
  breadcrumbLinks.forEach(link => {
    if (link.getAttribute('href') === '/' || link.getAttribute('href') === '#') {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }
  });
  
  // ─── 5. FEED ENTRY INTERACTIONS ───
  // Highlight feed entries on hover with visual feedback
  const feedEntries = document.querySelectorAll('.feed-entry');
  feedEntries.forEach(entry => {
    entry.addEventListener('mouseenter', function() {
      const dateCol = this.querySelector('.feed-date-col');
      if (dateCol) {
        dateCol.style.transition = 'color 0.3s ease';
        dateCol.style.color = 'var(--gold-dim)';
      }
    });
    entry.addEventListener('mouseleave', function() {
      const dateCol = this.querySelector('.feed-date-col');
      if (dateCol) {
        dateCol.style.color = '';
      }
    });
  });
  
  // ─── 6. TIMELINE INTERACTIONS ───
  // Make timeline items interactive
  const timelineItems = document.querySelectorAll('.timeline-inst');
  timelineItems.forEach(item => {
    item.addEventListener('click', function() {
      const link = this.querySelector('a');
      if (link) {
        window.location.href = link.href;
      }
    });
    item.style.cursor = 'pointer';
  });
  
  // ─── 7. SEASON ENTRIES ───
  // Add hover effect to season entries
  const seasonEntries = document.querySelectorAll('.season-entry');
  seasonEntries.forEach(entry => {
    entry.addEventListener('mouseenter', function() {
      const num = this.querySelector('.season-num');
      if (num) {
        num.style.transition = 'color 0.3s ease, transform 0.3s ease';
        num.style.color = 'var(--gold)';
        num.style.transform = 'scale(1.05)';
      }
    });
    entry.addEventListener('mouseleave', function() {
      const num = this.querySelector('.season-num');
      if (num) {
        num.style.color = '';
        num.style.transform = '';
      }
    });
  });
  
  // ─── 8. COPY CODE SNIPPETS ───
  // Allow copying of code snippets (for style guide)
  const codeBlocks = document.querySelectorAll('.style-code, .sg-code');
  codeBlocks.forEach(block => {
    block.style.cursor = 'pointer';
    block.title = 'Click to copy';
    
    block.addEventListener('click', function() {
      const text = this.textContent.trim();
      if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
          const originalText = this.textContent;
          this.textContent = '✓ Copied!';
          this.style.color = 'var(--sage)';
          
          setTimeout(() => {
            this.textContent = originalText;
            this.style.color = '';
          }, 1500);
        }).catch(() => {
          // Fallback for older browsers
          fallbackCopy(text, this);
        });
      } else {
        fallbackCopy(text, this);
      }
    });
  });
  
  function fallbackCopy(text, element) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand('copy');
      const originalText = element.textContent;
      element.textContent = '✓ Copied!';
      element.style.color = 'var(--sage)';
      setTimeout(() => {
        element.textContent = originalText;
        element.style.color = '';
      }, 1500);
    } catch (err) {
      // Silent fail
    }
    document.body.removeChild(textarea);
  }
  
  // ─── 9. DETAILS/ACCORDION PERSISTENCE ───
  // Remember open/closed state of details elements
  const details = document.querySelectorAll('details');
  details.forEach(detail => {
    const id = detail.id || 'detail-' + Math.random().toString(36).substr(2, 9);
    if (!detail.id) detail.id = id;
    
    // Restore state
    const savedState = localStorage.getItem('detail-' + id);
    if (savedState === 'open') {
      detail.open = true;
    }
    
    // Save state on toggle
    detail.addEventListener('toggle', function() {
      localStorage.setItem('detail-' + id, this.open ? 'open' : 'closed');
    });
  });
  
  // ─── 10. KEYBOARD NAVIGATION ───
  // Allow keyboard navigation through cards
  document.addEventListener('keydown', function(e) {
    // Escape key closes any open details
    if (e.key === 'Escape') {
      const openDetails = document.querySelectorAll('details[open]');
      openDetails.forEach(detail => {
        detail.open = false;
      });
    }
  });
  
  // ─── 11. SCROLL PROGRESS INDICATOR ───
  // Optional: Show scroll progress on long pages
  const createScrollProgress = () => {
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
      position: fixed;
      top: 48px;
      left: 0;
      height: 2px;
      background: var(--gold);
      z-index: 99;
      width: 0%;
      transition: width 0.1s ease;
      box-shadow: 0 0 10px rgba(212, 184, 122, 0.3);
    `;
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', function() {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / docHeight) * 100;
      progressBar.style.width = progress + '%';
    });
  };
  
  // Uncomment to enable scroll progress bar
  // if (document.body.scrollHeight > window.innerHeight * 2) {
  //   createScrollProgress();
  // }
  
  // ─── 12. RESPONSIVE TABLE WRAPPER ───
  // Wrap tables for horizontal scrolling on mobile
  const tables = document.querySelectorAll('.post-content table');
  tables.forEach(table => {
    if (!table.closest('.table-wrapper')) {
      const wrapper = document.createElement('div');
      wrapper.className = 'table-wrapper';
      wrapper.style.cssText = `
        overflow-x: auto;
        margin: 1.5rem 0;
        -webkit-overflow-scrolling: touch;
      `;
      table.parentNode.insertBefore(wrapper, table);
      wrapper.appendChild(table);
    }
  });
  
  // ─── 13. LAZY LOAD IMAGES ───
  // Lazy load images for better performance
  if ('IntersectionObserver' in window) {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    });
    
    images.forEach(img => imageObserver.observe(img));
  }
  
  // ─── 14. CONSOLE LOG (Optional) ───
  // Add a subtle console message
  console.log('📖 Journal of Incomplete Studies');
  console.log('🏷️  "Completion is not a prerequisite for publication."');
  
  // ─── 15. ERROR HANDLING ───
  // Catch and log errors without breaking the site
  window.addEventListener('error', function(e) {
    console.warn('A non-critical error occurred:', e.message);
    // Don't break the site
    return true;
  });
  
  // ─── 16. MOBILE MENU TOGGLE (if needed) ───
  // Add mobile menu toggle for small screens
  const topbarMark = document.querySelector('.topbar-mark');
  const topbarNav = document.querySelector('.topbar-nav');
  
  if (topbarMark && topbarNav && window.innerWidth < 768) {
    topbarMark.addEventListener('click', function() {
      topbarNav.classList.toggle('open');
      // Add a class to body for styling
      document.body.classList.toggle('nav-open');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.topbar')) {
        topbarNav.classList.remove('open');
        document.body.classList.remove('nav-open');
      }
    });
  }
  
  console.log('✅ Journal of Incomplete Studies loaded successfully.');
});