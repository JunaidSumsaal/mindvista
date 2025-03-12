document.addEventListener('DOMContentLoaded', function () {
  const navbar = document.getElementById('navbar');
  const navTitle = document.getElementById('nav-title');
  const loginBtn = document.getElementById('login-btn');
  const navLinks = document.querySelectorAll('.nav-link');

  // sourcery skip: avoid-function-declarations-in-blocks
  function handleScroll () {
    if (window.scrollY === 0) {
      navbar.classList.remove('bg-white', 'border-gray-200');
      navbar.classList.add('bg-transparent', 'border-transparent');
      navTitle.classList.remove('text-gray-900');
      navTitle.classList.add('text-white');
      if (loginBtn) {
        loginBtn.classList.remove(
          'text-gray-800',
          'hover:bg-gray-50',
          'focus:ring-gray-300'
        );
        loginBtn.classList.add(
          'text-white',
          'hover:bg-gray-700',
          'focus:ring-gray-600'
        );
      }
      navLinks.forEach((link) => {
        link.classList.remove('text-gray-700', 'hover:text-primary-700');
        link.classList.add('text-white', 'hover:text-gray-300');
      });
    } else {
      navbar.classList.remove('bg-transparent', 'border-transparent');
      navbar.classList.add(
        'bg-white',
        'border-gray-200',
        'border-b',
        'border-gray-300',
        'shadow-md'
      );
      navTitle.classList.remove('text-white');
      navTitle.classList.add('text-gray-900');
      if (loginBtn) {
        loginBtn.classList.remove(
          'text-white',
          'hover:bg-gray-700',
          'focus:ring-gray-600'
        );
        loginBtn.classList.add(
          'text-gray-800',
          'hover:bg-gray-50',
          'focus:ring-gray-300'
        );
      }
      navLinks.forEach((link) => {
        link.classList.remove('text-white', 'hover:text-gray-300');
        link.classList.add('text-gray-700', 'hover:text-primary-700');
      });
    }
  }

  function toggleNavbar (collapseID) {
    document.getElementById(collapseID).classList.toggle('hidden');
    document.getElementById(collapseID).classList.toggle('block');
  }

  function dateFooter () {
    document.getElementById('date').textContent = new Date().getFullYear();
  }

  window.addEventListener('scroll', handleScroll);
  handleScroll();
  toggleNavbar();
  dateFooter();
});
