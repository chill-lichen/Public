/* Minimal page utility. No tracking, sample dataset, or network requests. */
for (const year of document.querySelectorAll("[data-current-year]")) {
  year.textContent = String(new Date().getFullYear());
}
