// ─── style-guide.js ───

document.addEventListener('DOMContentLoaded', function() {
  
  // ─── Smooth scrolling for navigation ───
  const tocLinks = document.querySelectorAll('.style-toc a');
  
  tocLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        const offset = 80; // Account for fixed header
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - offset;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
  
  // ─── Active state for navigation ───
  const sections = document.querySelectorAll('.style-section');
  const navLinks = document.querySelectorAll('.style-toc a');
  
  function updateActiveNav() {
    let current = '';
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 100;
      if (window.pageYOffset >= sectionTop) {
        current = section.getAttribute('id');
      }
    });
    
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  }
  
  window.addEventListener('scroll', updateActiveNav);
  
  // ─── Interactive: Copy code snippets ───
  const codeBlocks = document.querySelectorAll('.style-code');
  
  codeBlocks.forEach(block => {
    block.style.cursor = 'pointer';
    block.title = 'Click to copy';
    
    block.addEventListener('click', function() {
      const text = this.textContent.trim();
      navigator.clipboard.writeText(text).then(() => {
        const originalText = this.textContent;
        this.textContent = '✓ Copied!';
        this.style.color = 'var(--sage)';
        
        setTimeout(() => {
          this.textContent = originalText;
          this.style.color = '';
        }, 1500);
      });
    });
  });
  
  // ─── Interactive: Details/Accordion tracking ───
  const details = document.querySelectorAll('.demo-details');
  
  details.forEach(detail => {
    detail.addEventListener('toggle', function() {
      const summary = this.querySelector('summary');
      if (this.open) {
        summary.style.color = 'var(--gold)';
      } else {
        summary.style.color = '';
      }
    });
  });
  
  // ─── Interactive: Tooltip enhancement ───
  const tooltips = document.querySelectorAll('.demo-tooltip');
  
  tooltips.forEach(tooltip => {
    tooltip.addEventListener('mouseenter', function() {
      // Add a subtle glow effect
      this.style.textShadow = '0 0 20px rgba(212, 184, 122, 0.2)';
    });
    
    tooltip.addEventListener('mouseleave', function() {
      this.style.textShadow = 'none';
    });
  });
  
  // ─── Interactive: Card click feedback ───
  const cards = document.querySelectorAll('.card.interactive-demo');
  
  cards.forEach(card => {
    card.addEventListener('click', function() {
      // Add a quick pulse effect
      this.style.transition = 'transform 0.1s ease';
      this.style.transform = 'scale(0.98)';
      
      setTimeout(() => {
        this.style.transform = '';
      }, 150);
    });
  });
  
});