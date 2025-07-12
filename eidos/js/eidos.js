// eidos.js - Main EidosUI JavaScript file
(function() {
    'use strict';
    
    class EidosUI {
        constructor() {
            this.initToggle();
            this.initScrollspy();
        }
        
        initToggle() {
            document.querySelectorAll('[data-toggle]').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetId = btn.dataset.toggle;
                    const target = document.querySelector(targetId);
                    if (target) {
                        const isHidden = target.classList.contains('hidden');
                        target.classList.toggle('hidden');
                        
                        // Update ARIA attributes
                        const toggleButtons = document.querySelectorAll(`[data-toggle="${targetId}"][role="button"]`);
                        toggleButtons.forEach(toggleBtn => {
                            toggleBtn.setAttribute('aria-expanded', isHidden);
                            
                            // Toggle menu icons if they exist
                            const openIcon = toggleBtn.querySelector('[data-menu-icon="open"]');
                            const closeIcon = toggleBtn.querySelector('[data-menu-icon="close"]');
                            if (openIcon && closeIcon) {
                                openIcon.classList.toggle('hidden');
                                closeIcon.classList.toggle('hidden');
                            }
                        });
                    }
                });
            });
            
            // Auto-close mobile menu when clicking a link
            document.querySelectorAll('[data-mobile-menu="true"] a').forEach(link => {
                link.addEventListener('click', () => {
                    const menu = link.closest('[data-mobile-menu="true"]');
                    if (menu && !menu.classList.contains('hidden')) {
                        menu.classList.add('hidden');
                        // Update toggle button state
                        const menuId = '#' + menu.id;
                        const toggleBtn = document.querySelector(`[data-toggle="${menuId}"][role="button"]`);
                        if (toggleBtn) {
                            toggleBtn.setAttribute('aria-expanded', 'false');
                            const openIcon = toggleBtn.querySelector('[data-menu-icon="open"]');
                            const closeIcon = toggleBtn.querySelector('[data-menu-icon="close"]');
                            if (openIcon && closeIcon) {
                                openIcon.classList.remove('hidden');
                                closeIcon.classList.add('hidden');
                            }
                        }
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
    }
    
    window.EidosUI = EidosUI;
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => new EidosUI());
    } else {
        new EidosUI();
    }
})();