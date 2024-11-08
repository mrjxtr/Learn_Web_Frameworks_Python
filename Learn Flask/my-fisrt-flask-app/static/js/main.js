// Theme management
class ThemeManager {
    constructor() {
        this.isDark = localStorage.getItem('isDark') !== 'false';
        this.themeToggle = document.getElementById('theme-toggle');
        this.init();
    }

    init() {
        this.applyTheme();
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', () => this.toggleTheme());
        }
    }

    applyTheme() {
        const root = document.documentElement;
        if (this.isDark) {
            root.style.setProperty('--background-color', '#121212');
            root.style.setProperty('--text-color', '#e0e0e0');
            root.style.setProperty('--surface-color', '#1e1e1e');
        } else {
            root.style.setProperty('--background-color', '#ffffff');
            root.style.setProperty('--text-color', '#121212');
            root.style.setProperty('--surface-color', '#f5f5f5');
        }
        
        if (this.themeToggle) {
            this.themeToggle.textContent = this.isDark ? '🌙' : '☀️';
        }
    }

    toggleTheme() {
        this.isDark = !this.isDark;
        localStorage.setItem('isDark', this.isDark);
        this.applyTheme();
    }
}

// Form validation
class FormValidator {
    constructor(form) {
        this.form = form;
        this.init();
    }

    init() {
        this.form.querySelectorAll('input').forEach(input => {
            input.addEventListener('input', () => this.validateField(input));
            input.addEventListener('blur', () => this.validateField(input));
        });

        this.form.addEventListener('submit', (e) => {
            if (!this.validateForm()) {
                e.preventDefault();
            }
        });
    }

    validateField(input) {
        const validationMessage = input.nextElementSibling;
        let isValid = true;
        let message = '';

        if (input.hasAttribute('required') && !input.value) {
            isValid = false;
            message = 'This field is required';
        } else if (input.type === 'email' && !this.isValidEmail(input.value)) {
            isValid = false;
            message = 'Please enter a valid email';
        }

        input.classList.toggle('valid', isValid);
        input.classList.toggle('invalid', !isValid);
        
        if (validationMessage) {
            validationMessage.textContent = message;
        }

        return isValid;
    }

    validateForm() {
        const inputs = this.form.querySelectorAll('input');
        let isValid = true;

        inputs.forEach(input => {
            if (!this.validateField(input)) {
                isValid = false;
            }
        });

        return isValid;
    }

    isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }
}

// Loading state manager
class LoadingManager {
    static showLoading(button) {
        button.disabled = true;
        const spinner = document.createElement('span');
        spinner.className = 'spinner';
        button.prepend(spinner);
    }

    static hideLoading(button) {
        button.disabled = false;
        const spinner = button.querySelector('.spinner');
        if (spinner) {
            spinner.remove();
        }
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme
    new ThemeManager();

    // Initialize form validation for all forms
    document.querySelectorAll('form').forEach(form => {
        new FormValidator(form);
    });

    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href'))?.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Feature item animations
    document.querySelectorAll('.feature-item').forEach(item => {
        item.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 200);
        });
    });
}); 
