document.addEventListener('DOMContentLoaded', () => {
  const body = document.body;
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('is-open');
      body.classList.toggle('menu-open', isOpen);
      menuToggle.setAttribute('aria-expanded', String(isOpen));
      menuToggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
    });

    navMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('is-open');
        body.classList.remove('menu-open');
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.setAttribute('aria-label', 'Open menu');
      });
    });
  }

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (event) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        event.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  document.querySelectorAll('[data-current-year]').forEach((node) => {
    node.textContent = new Date().getFullYear();
  });

  const packageSelect = document.querySelector('[data-package-select]');
  if (packageSelect) {
    const helper = document.createElement('p');
    helper.className = 'microcopy';
    packageSelect.insertAdjacentElement('afterend', helper);

    const copy = {
      starter: 'Starter is a practical fit for smaller teams up to 25 users.',
      business: 'Business is recommended for growing teams that need onboarding, backups, and security hardening.',
      enterprise: 'Enterprise is best when migration, advanced security, documentation, or 100+ users are required.',
    };

    const updateHelper = () => {
      helper.textContent = copy[packageSelect.value] || 'Choose the package that best matches your current team size.';
    };

    packageSelect.addEventListener('change', updateHelper);
    updateHelper();
  }

  document.querySelectorAll('form').forEach((form) => {
    form.addEventListener('submit', () => {
      const button = form.querySelector('button[type="submit"]');
      if (button) {
        button.dataset.originalText = button.textContent;
        button.textContent = 'Submitting...';
      }
    });
  });
});
