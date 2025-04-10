document.addEventListener('DOMContentLoaded', function () {
  const featureBlocks = document.querySelectorAll('.feature-block');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
         // отключаем наблюдение после появления
      }
    });
  }, { threshold: 0.2 });

  featureBlocks.forEach(block => {
    observer.observe(block);
  });
});
