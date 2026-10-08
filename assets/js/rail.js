// assets/js/rail.js
(function () {
  const essay = document.getElementById('essayBody');
  const rail  = document.getElementById('railSections');
  const fill  = document.getElementById('railFill');
  if (!rail) return;

  // ─── Auto-build from H2s if #essayBody exists ───
  if (essay) {
    const headings = Array.from(essay.querySelectorAll('h2'));
    if (headings.length) {
      headings.forEach((h, i) => {
        if (!h.id) h.id = 'sec-' + (i + 1);
        const num = String(i + 1).padStart(2, '0');
        const label = h.dataset.railLabel || h.textContent.trim();

        const a = document.createElement('a');
        a.href = '#' + h.id;
        a.className = 'rail-item' + (i === 0 ? ' active' : '');
        a.innerHTML = `<span class="rail-num">${num}</span><span class="rail-label">${label}</span>`;
        rail.appendChild(a);
      });
    }
  }

  // ─── Scroll spy + progress fill ───
  const items = Array.from(rail.querySelectorAll('.rail-item'));
  const targets = items.map(a => {
    const href = a.getAttribute('href');
    return href && href.startsWith('#') ? document.querySelector(href) : null;
  });

  function update() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? Math.min(100, Math.max(0, (scrollTop / docHeight) * 100)) : 0;
    if (fill) fill.style.width = pct + '%';

    let current = 0;
    targets.forEach((el, i) => {
      if (el && el.getBoundingClientRect().top <= 140) current = i;
    });
    items.forEach((it, i) => it.classList.toggle('active', i === current));
  }

  document.addEventListener('scroll', update, { passive: true });
  update();
})();