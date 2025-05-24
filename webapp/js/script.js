/**
 * PreProPy Documentation - Main JavaScript
 * Enhances the website with interactive features and animations
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize smooth scrolling for anchor links
    initSmoothScroll();
    
    // Add animation classes to elements as they scroll into view
    initScrollAnimations();
    
    // Add copy functionality to code blocks
    initCodeCopy();
    
    // Initialize collapsible sections
    initCollapsible();
    
    // Add active state to current navigation item
    highlightActiveNavItem();
    
    // Initialize code syntax highlighting
    highlightCode();
    
    console.log('PreProPy documentation JS initialized');
});

/**
 * Implements smooth scrolling for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Close mobile menu if open
                const mobileMenu = document.getElementById('mobile-menu');
                if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
                    mobileMenu.classList.add('hidden');
                }
                
                // Scroll to the target with offset for fixed header
                const headerHeight = document.querySelector('header').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Adds animation classes to elements as they scroll into view
 */
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if (animatedElements.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fadeIn');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    animatedElements.forEach(el => {
        observer.observe(el);
    });
}

/**
 * Adds copy button functionality to code blocks
 */
function initCodeCopy() {
    document.querySelectorAll('pre').forEach(block => {
        // Create copy button
        const button = document.createElement('button');
        button.className = 'absolute right-2 top-2 bg-gray-200 dark:bg-gray-700 p-1 rounded text-sm';
        button.innerHTML = '<i class="fas fa-copy"></i>';
        button.setAttribute('aria-label', 'Copy code to clipboard');
        
        // Style the pre element to have relative positioning
        block.style.position = 'relative';
        block.appendChild(button);
        
        // Add click event
        button.addEventListener('click', () => {
            const code = block.querySelector('code') ? block.querySelector('code').innerText : block.innerText;
            navigator.clipboard.writeText(code).then(() => {
                // Visual feedback
                button.innerHTML = '<i class="fas fa-check"></i>';
                setTimeout(() => {
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy:', err);
                button.innerHTML = '<i class="fas fa-times"></i>';
                setTimeout(() => {
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            });
        });
    });
}

/**
 * Initializes collapsible sections
 */
function initCollapsible() {
    document.querySelectorAll('.collapsible-header').forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            if (content && content.classList.contains('collapsible-content')) {
                content.classList.toggle('hidden');
                
                // Toggle icon if present
                const icon = header.querySelector('.collapsible-icon');
                if (icon) {
                    icon.classList.toggle('fa-plus');
                    icon.classList.toggle('fa-minus');
                }
            }
        });
    });
}

/**
 * Highlights the active navigation item based on scroll position
 */
function highlightActiveNavItem() {
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('nav a[href^="#"]');
    
    if (sections.length === 0 || navItems.length === 0) return;
    
    window.addEventListener('scroll', () => {
        let current = '';
        const headerHeight = document.querySelector('header').offsetHeight;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - headerHeight - 100;
            const sectionHeight = section.offsetHeight;
            
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navItems.forEach(navItem => {
            navItem.classList.remove('text-primary-600', 'dark:text-primary-400');
            const href = navItem.getAttribute('href').substring(1);
            
            if (href === current) {
                navItem.classList.add('text-primary-600', 'dark:text-primary-400');
            }
        });
    });
}

/**
 * Simple syntax highlighting for code blocks
 * Note: This is a very basic implementation
 * For production, use a library like highlight.js or Prism
 */
function highlightCode() {
    document.querySelectorAll('pre code').forEach(block => {
        // This is where you'd typically use a proper syntax highlighter
        // For now, we'll just add a class to indicate it's ready for highlighting
        block.classList.add('hljs');
    });
}

/**
 * Search functionality 
 */
function initSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;
    
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const searchResults = document.getElementById('search-results');
        
        if (query.length < 2) {
            searchResults.innerHTML = '';
            searchResults.classList.add('hidden');
            return;
        }
        
        // Get all headings and their content
        const headings = document.querySelectorAll('h1, h2, h3, h4');
        const matches = [];
        
        headings.forEach(heading => {
            const text = heading.textContent.toLowerCase();
            const nextEl = heading.nextElementSibling;
            let contentText = '';
            
            if (nextEl && ['P', 'UL', 'OL'].includes(nextEl.tagName)) {
                contentText = nextEl.textContent.toLowerCase();
            }
            
            if (text.includes(query) || contentText.includes(query)) {
                const id = heading.closest('section').id || heading.id;
                matches.push({
                    title: heading.textContent,
                    link: id ? `#${id}` : null,
                    text: contentText.substring(0, 100) + '...'
                });
            }
        });
        
        // Display results
        if (matches.length > 0) {
            searchResults.innerHTML = matches.map(match => `
                <a href="${match.link}" class="block p-3 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
                    <div class="font-medium">${match.title}</div>
                    <div class="text-sm text-gray-600 dark:text-gray-400">${match.text}</div>
                </a>
            `).join('');
            searchResults.classList.remove('hidden');
        } else {
            searchResults.innerHTML = '<div class="p-3 text-gray-600 dark:text-gray-400">No results found</div>';
            searchResults.classList.remove('hidden');
        }
    });
    
    // Close search results when clicking outside
    document.addEventListener('click', (e) => {
        const searchResults = document.getElementById('search-results');
        const searchContainer = document.getElementById('search-container');
        
        if (searchResults && !searchResults.classList.contains('hidden') && !searchContainer.contains(e.target)) {
            searchResults.classList.add('hidden');
        }
    });
}
