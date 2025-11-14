// chat.js - Chat component JavaScript
(function() {
    'use strict';
    
    function initChatInput(textareaId) {
        const textarea = document.getElementById(textareaId);
        if (!textarea) return;
        
        const attachmentsDiv = document.getElementById(textareaId + '-attachments');
        const fileInput = document.getElementById(textareaId + '-files');
        const form = textarea.closest('form');
        
        // Auto-resize textarea
        textarea.addEventListener('input', function() {
            this.style.height = '44px';
            this.style.height = Math.min(this.scrollHeight, 200) + 'px';
        });
        
        // Handle file attachments
        if (fileInput && attachmentsDiv) {
            fileInput.addEventListener('change', function(e) {
                const files = Array.from(e.target.files);
                const maxFiles = parseInt(this.getAttribute('data-max-files') || '5');
                
                if (files.length > maxFiles) {
                    alert(`Maximum ${maxFiles} files allowed`);
                    this.value = '';
                    return;
                }
                
                if (files.length > 0) {
                    attachmentsDiv.classList.add('has-files');
                    attachmentsDiv.innerHTML = files.map((file, i) => `
                        <div class="eidos-chat-attachment">
                            <span class="eidos-chat-attachment-name">${file.name}</span>
                            <button type="button" 
                                class="eidos-chat-attachment-remove"
                                onclick="removeAttachment('${textareaId}', this)"
                                aria-label="Remove file">✕</button>
                        </div>
                    `).join('');
                } else {
                    attachmentsDiv.classList.remove('has-files');
                    attachmentsDiv.innerHTML = '';
                }
            });
        }
        
        // Submit on Enter (without Shift)
        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                form.requestSubmit();
            }
        });
        
        // Reset form after HTMX request
        if (form) {
            document.body.addEventListener('htmx:afterRequest', function(event) {
                if (event.detail.elt === form) {
                    form.reset();
                    textarea.style.height = '44px';
                    if (attachmentsDiv) {
                        attachmentsDiv.innerHTML = '';
                        attachmentsDiv.classList.remove('has-files');
                    }
                }
            });
        }
    }
    
    function initChatContainer(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        // Auto-scroll to bottom when new messages arrive
        const observer = new MutationObserver(() => {
            container.scrollTop = container.scrollHeight;
        });
        observer.observe(container, { childList: true, subtree: true });
    }
    
    // Global function for removing attachments
    window.removeAttachment = function(textareaId, button) {
        button.parentElement.remove();
        const attachmentsDiv = document.getElementById(textareaId + '-attachments');
        const fileInput = document.getElementById(textareaId + '-files');
        
        if (attachmentsDiv && !attachmentsDiv.children.length) {
            attachmentsDiv.classList.remove('has-files');
            if (fileInput) fileInput.value = '';
        }
    };
    
    // Initialize all chat inputs on page
    function initAllChats() {
        document.querySelectorAll('[data-chat-input]').forEach(el => {
            const textareaId = el.getAttribute('data-chat-input');
            initChatInput(textareaId);
        });
        
        document.querySelectorAll('[data-chat-container]').forEach(el => {
            const containerId = el.id;
            initChatContainer(containerId);
        });
    }
    
    // Run on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAllChats);
    } else {
        initAllChats();
    }
    
    // Re-initialize after HTMX swaps
    document.body.addEventListener('htmx:afterSwap', initAllChats);
})();
