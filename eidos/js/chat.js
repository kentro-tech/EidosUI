// chat.js - Minimal chat JavaScript (HTMX + Alpine.js)
(function() {
    'use strict';
    
    // Auto-scroll chat containers when new messages arrive
    function initChatContainer(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        const observer = new MutationObserver(() => {
            container.scrollTop = container.scrollHeight;
        });
        observer.observe(container, { childList: true, subtree: true });
    }
    
    // Initialize chat containers on page load
    function initAllChats() {
        document.querySelectorAll('[data-chat-container]').forEach(el => {
            initChatContainer(el.id);
        });
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAllChats);
    } else {
        initAllChats();
    }
    
    document.body.addEventListener('htmx:afterSwap', initAllChats);
})();
