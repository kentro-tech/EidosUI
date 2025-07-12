// eidos.js - Main EidosUI JavaScript file
(function() {
    'use strict';
    
    class EidosUI {
        constructor() {
            this.initToggle();
            this.initScrollspy();
            // Future features will be added here
        }
        
        initToggle() {
            document.querySelectorAll('[data-toggle]').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetId = btn.dataset.toggle;
                    const target = document.querySelector(targetId);
                    if (target) {
                        target.classList.toggle('hidden');
                        // Update ARIA attributes
                        const isExpanded = !target.classList.contains('hidden');
                        btn.setAttribute('aria-expanded', isExpanded);
                    }
                });
            });
        }
        
        initScrollspy() {
            const containers = document.querySelectorAll('[data-scrollspy="true"]');
            if (!containers.length) return;
            
            const sections = document.querySelectorAll('section[id], [data-scrollspy-target]');
            if (!sections.length) return;
            
            const observerOptions = {
                rootMargin: '-20% 0px -70% 0px',
                threshold: [0, 0.1, 0.5, 1]
            };
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.intersectionRatio > 0.1) {
                        const id = entry.target.id;
                        containers.forEach(container => {
                            const links = container.querySelectorAll('a[href^="#"]');
                            links.forEach(link => {
                                const isActive = link.getAttribute('href') === `#${id}`;
                                link.classList.toggle('eidos-active', isActive);
                            });
                        });
                    }
                });
            }, observerOptions);
            
            sections.forEach(section => observer.observe(section));
            
            // Smooth scrolling for nav links
            containers.forEach(container => {
                container.querySelectorAll('a[href^="#"]').forEach(link => {
                    link.addEventListener('click', (e) => {
                        const targetId = link.getAttribute('href');
                        const target = document.querySelector(targetId);
                        if (target) {
                            e.preventDefault();
                            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        }
                    });
                });
            });
        }
        
        // Future methods for other components
        // initModals() { }
        // initTooltips() { }
        // initDropdowns() { }
    }
    
    // Initialize EidosUI
    window.EidosUI = EidosUI;
    
    // Auto-initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => new EidosUI());
    } else {
        new EidosUI();
    }
})();