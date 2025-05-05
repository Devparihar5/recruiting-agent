/**
 * Recruiting Agent - Main JavaScript
 */

// DOM Elements
const jdForm = document.getElementById('jdForm');
const loader = document.getElementById('loader');

// Show loader when form is submitted
function showLoader() {
  if (loader) {
    loader.style.display = 'flex';
    document.body.style.overflow = 'hidden'; // Prevent scrolling when loader is visible
  }
}

// Initialize email generation functionality
function initEmailGeneration() {
  const emailButtons = document.querySelectorAll('.generate-email');
  if (!emailButtons.length) return;
  
  const emailModal = new bootstrap.Modal(document.getElementById('emailModal'));
  const emailLoading = document.getElementById('emailLoading');
  const emailContentWrapper = document.getElementById('emailContentWrapper');
  const emailContent = document.getElementById('emailContent');
  
  emailButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Show modal with loading state
      emailLoading.style.display = 'block';
      emailContentWrapper.style.display = 'none';
      emailModal.show();
      
      const resume = button.getAttribute('data-resume');
      const position = button.getAttribute('data-position');
      
      // Call the API to generate email
      fetch('/generate_mail', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ resume: resume, position_name: position })
      })
      .then(res => {
        if (!res.ok) {
          throw new Error('Server error');
        }
        return res.json();
      })
      .then(data => {
        // Hide loading, show content
        emailLoading.style.display = 'none';
        emailContentWrapper.style.display = 'block';
        
        // Display the email
        emailContent.textContent = data.email;
      })
      .catch(err => {
        // Handle errors
        emailLoading.style.display = 'none';
        emailContentWrapper.style.display = 'block';
        emailContent.textContent = 'Error generating email. Please try again.';
        console.error('Email generation error:', err);
      });
    });
  });
}

// Copy email to clipboard
function copyEmail() {
  const emailText = document.getElementById('emailContent').textContent;
  navigator.clipboard.writeText(emailText)
    .then(() => {
      const copyBtn = document.getElementById('copyEmailBtn');
      const originalText = copyBtn.innerHTML;
      
      // Change button text to indicate success
      copyBtn.innerHTML = '<i class="fas fa-check me-2"></i>Copied!';
      
      // Reset button text after 2 seconds
      setTimeout(() => {
        copyBtn.innerHTML = originalText;
      }, 2000);
    })
    .catch(err => {
      console.error('Failed to copy: ', err);
      alert('Failed to copy email. Please try again.');
    });
}

// Initialize tooltips and popovers
function initBootstrapComponents() {
  // Initialize tooltips
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
  
  // Initialize popovers
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
  });
}

// Document ready
document.addEventListener('DOMContentLoaded', function() {
  // Initialize form submission
  if (jdForm) {
    jdForm.addEventListener('submit', showLoader);
  }
  
  // Initialize email generation
  initEmailGeneration();
  
  // Initialize Bootstrap components
  initBootstrapComponents();
  
  // Make copyEmail function globally available
  window.copyEmail = copyEmail;
});
