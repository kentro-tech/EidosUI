// eidos.js - EidosUI JavaScript using Alpine.js
document.addEventListener('alpine:init', () => {
    Alpine.store('scrollspy', {
        activeId: null,
        setActive(id) {
            this.activeId = id;
        }
    });
});

// Scrollspy functionality with Alpine.js store
function initScrollspy() {
    const containers = document.querySelectorAll('[data-scrollspy="true"]');
    if (!containers.length) return;
    
    const sections = document.querySelectorAll('section[id], [data-scrollspy-target]');
    if (!sections.length) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.intersectionRatio > 0.1 && window.Alpine) {
                Alpine.store('scrollspy').setActive(entry.target.id);
            }
        });
    }, {
        rootMargin: '-20% 0px -70% 0px',
        threshold: [0, 0.1, 0.5, 1]
    });
    
    sections.forEach(section => observer.observe(section));
    
    // Smooth scrolling
    containers.forEach(container => {
        container.querySelectorAll('a[href^="#"]').forEach(link => {
            link.addEventListener('click', (e) => {
                const target = document.querySelector(link.getAttribute('href'));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    });
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollspy);
} else {
    initScrollspy();
}
