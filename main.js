document.addEventListener('DOMContentLoaded', () => {
    const typeFilter = document.getElementById('typeFilter');
    const materialFilter = document.getElementById('materialFilter');
    const catalogCards = Array.from(document.querySelectorAll('.catalog-card'));

    const applyFilters = () => {
        const typeValue = typeFilter ? typeFilter.value : 'Todas';
        const materialValue = materialFilter ? materialFilter.value : 'Todos';

        catalogCards.forEach((card) => {
            const matchesType = typeValue === 'Todas' || card.dataset.type === typeValue;
            const matchesMaterial = materialValue === 'Todos' || card.dataset.material === materialValue;
            card.style.display = matchesType && matchesMaterial ? '' : 'none';
        });
    };

    if (typeFilter) {
        typeFilter.addEventListener('change', applyFilters);
    }

    if (materialFilter) {
        materialFilter.addEventListener('change', applyFilters);
    }

    document.querySelectorAll('.details-toggle').forEach((button) => {
        button.addEventListener('click', () => {
            const card = button.closest('.catalog-card');
            if (card) {
                card.classList.toggle('is-open');
                button.textContent = card.classList.contains('is-open') ? 'Ocultar detalle' : 'Ver detalle';
            }
        });
    });

    document.querySelectorAll('form[id$="Form"]').forEach((form) => {
        const status = form.querySelector('[data-status-for]');
        const endpoint = form.id === 'quoteForm' ? '/quote' : '/appointment';

        form.addEventListener('submit', async (event) => {
            event.preventDefault();

            const formData = Object.fromEntries(new FormData(form).entries());

            try {
                const response = await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData),
                });

                const result = await response.json();
                if (!response.ok || result.status !== 'success') {
                    throw new Error(result.message || 'Request failed');
                }

                if (status) {
                    status.textContent = result.message;
                    status.style.color = '#0f766e';
                }
                form.reset();
            } catch (error) {
                if (status) {
                    status.textContent = 'No se pudo enviar. Intenta de nuevo.';
                    status.style.color = '#b91c1c';
                }
            }
        });
    });

    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener('click', (event) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                event.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    applyFilters();
});
