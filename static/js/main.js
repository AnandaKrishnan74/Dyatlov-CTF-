// DYATLOV PASS CTF - Frontend interactions only
// Flag validation is always server-side

document.addEventListener('DOMContentLoaded', function() {
    // Timeline expand/collapse
    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach(item => {
        item.addEventListener('click', function() {
            this.classList.toggle('open');
        });
    });

    // Document expanders
    const docToggles = document.querySelectorAll('[data-toggle-doc]');
    docToggles.forEach(btn => {
        btn.addEventListener('click', function() {
            const targetId = this.getAttribute('data-toggle-doc');
            const target = document.getElementById(targetId);
            if (target) {
                target.classList.toggle('hidden');
                this.textContent = target.classList.contains('hidden') ? 'Open Document' : 'Close Document';
            }
        });
    });

    // Subtle typewriter effect for mystery text if present
    const typeTargets = document.querySelectorAll('[data-typewriter]');
    typeTargets.forEach(el => {
        const text = el.textContent;
        el.textContent = '';
        let i = 0;
        const speed = 30;
        function type() {
            if (i < text.length) {
                el.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        type();
    });
});
