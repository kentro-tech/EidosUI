// chat.js - Minimal chat JavaScript (HTMX + Alpine.js friendly)
// Purpose: Keep any chat message list scrolled to the bottom as new messages arrive.
// Works with HTMX swaps (re-initializes after content is replaced) and plays nicely with Alpine.

/* Wrap everything in an IIFE to avoid leaking variables into the global scope */
(function() {
    'use strict';
    
    /**
     * Auto-scroll a chat container whenever its children change.
     * Uses a MutationObserver so it reacts to DOM changes caused by:
     * - HTMX swaps/updates
     * - Alpine updates
     * - Manual DOM inserts (e.g., appendChild)
     * UX impact: Keeps the most recent messages in view without user effort.
     */
    function initChatContainer(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return; // Safe-guard: skip if not found
        
        // Observe additions/removals in the container subtree (messages list)
        const observer = new MutationObserver(() => {
            // Always stick to the bottom when new nodes are added
            container.scrollTop = container.scrollHeight;
        });
        observer.observe(container, { childList: true, subtree: true });
    }
    
    /**
     * Find all chat containers marked with [data-chat-container]
     * and initialize auto-scroll behavior on each.
     * Using a data-attribute avoids coupling to specific classes/IDs.
     */
    function initAllChats() {
        document.querySelectorAll('[data-chat-container]').forEach(el => {
            // Assumes each container has a stable id attribute
            initChatContainer(el.id);
        });
    }
    
    // Initialize once the DOM is ready (covers normal page loads)
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAllChats);
    } else {
        initAllChats();
    }
    
    /**
     * HTMX integration: after HTMX swaps content into the DOM,
     * we need to re-run initialization because the previous nodes
     * (and their observers) may have been replaced.
     * Event: htmx:afterSwap fires after any swap operation completes.
     */
    document.body.addEventListener('htmx:afterSwap', initAllChats);
})();
