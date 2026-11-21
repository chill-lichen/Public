/* Shared behaviour for both design directions: service menu, selection carry-over, two-step intake.
   Mockup only. Nothing is sent anywhere. */
(function () {
  "use strict";

  var STAGES = [
    { key: "diagnostic", n: "1", name: "Diagnostic", line: "Understand the situation", body: "Get the facts in one place before anyone builds anything." },
    { key: "prescription", n: "2", name: "Prescription", line: "Prepare the plan materials", body: "Turn your direction into review-ready drafts." },
    { key: "operation", n: "3", name: "Operation", line: "Keep things running", body: "Ongoing upkeep, month after month." }
  ];

  var SERVICES = [
    { id: "d-gather", stage: "diagnostic", title: "Client data gathering", desc: "I collect statements, account details and questionnaires, then organize them into one clean client file.", get: "An organized file and a list of what's still missing" },
    { id: "d-snapshot", stage: "diagnostic", title: "Household snapshot", desc: "A summary of balance sheet and cash flow, built from the data you provide, so you start the meeting knowing the picture.", get: "A one-page summary for your review" },
    { id: "d-owner", stage: "diagnostic", title: "Business-owner readiness review", tag: "CEPA", desc: "I gather what an exit or succession conversation depends on: financials, ownership details, and readiness answers.", get: "Organized business financials and a gaps list" },
    { id: "d-books", stage: "diagnostic", title: "Firm books check-up", desc: "A look at your practice's own books: what's reconciled, what's behind, and what's miscategorized.", get: "A short status note and a catch-up estimate" },

    { id: "p-entry", stage: "prescription", title: "Planning software entry", desc: "I enter client data into your planning software and check it against the source documents.", get: "A client file that's ready to model" },
    { id: "p-scenarios", stage: "prescription", title: "Scenario runs", desc: "I run the scenarios you specify and lay the outputs side by side.", get: "Draft outputs for your review" },
    { id: "p-packet", stage: "prescription", title: "Meeting packet", desc: "Plan outputs, agenda and supporting pages, assembled in your template.", get: "A review-ready packet" },
    { id: "p-owner", stage: "prescription", title: "Owner discussion materials", tag: "CEPA", desc: "Draft materials for an exit or succession conversation, for you and the client's other professionals.", get: "Draft pages for you to review and edit" },

    { id: "o-books", stage: "operation", title: "Monthly bookkeeping & close", desc: "I categorize transactions, reconcile bank and card accounts, and close each month.", get: "Reconciled books and a short note on anything unusual" },
    { id: "o-fees", stage: "operation", title: "Fee revenue tie-out", desc: "Advisory fee revenue tied back to your billing or custodian reports.", get: "A monthly reconciliation" },
    { id: "o-followup", stage: "operation", title: "Meeting follow-up & CRM upkeep", desc: "Notes, task lists and CRM entries after each client meeting.", get: "An up-to-date CRM" },
    { id: "o-cpa", stage: "operation", title: "Year-end CPA package", desc: "Organized records for your CPA at year end. Tax preparation is not included.", get: "One tidy package for your CPA" }
  ];

  var KEY = "ry-mockup-selection";

  function readSel() {
    var fromUrl = new URLSearchParams(location.search).get("s");
    if (fromUrl !== null) return fromUrl.split(",").filter(valid);
    try { return (JSON.parse(localStorage.getItem(KEY)) || []).filter(valid); } catch (e) { return []; }
  }
  function valid(id) { return SERVICES.some(function (s) { return s.id === id; }); }
  var sel = readSel();
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(sel)); } catch (e) { /* storage blocked: selection still rides on links */ }
    updateCtas();
  }
  function has(id) { return sel.indexOf(id) !== -1; }
  function toggle(id) { sel = has(id) ? sel.filter(function (x) { return x !== id; }) : sel.concat(id); save(); }
  function byId(id) { return SERVICES.filter(function (s) { return s.id === id; })[0]; }
  function stageOf(key) { return STAGES.filter(function (s) { return s.key === key; })[0]; }

  /* Every "Start intake" link carries the selection forward. */
  function updateCtas() {
    document.querySelectorAll("[data-cta]").forEach(function (a) {
      var base = a.getAttribute("data-cta");
      a.setAttribute("href", sel.length ? base + "?s=" + sel.join(",") : base);
    });
    document.querySelectorAll("[data-count]").forEach(function (el) {
      el.textContent = String(sel.length);
    });
    document.querySelectorAll("[data-count-label]").forEach(function (el) {
      el.textContent = sel.length === 0 ? "Nothing selected yet" : sel.length === 1 ? "1 service selected" : sel.length + " services selected";
    });
    document.querySelectorAll("[data-tray]").forEach(function (el) { el.classList.toggle("is-on", sel.length > 0); });
  }

  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* ---------- Service menu ---------- */
  function renderMenu(root) {
    var layout = root.getAttribute("data-menu"); // "columns" or "tabs"
    var html = "";
    if (layout === "tabs") {
      html += '<div class="tabs" role="tablist" aria-label="Service stages">';
      STAGES.forEach(function (st, i) {
        html += '<button class="tab" role="tab" id="tab-' + st.key + '" aria-controls="panel-' + st.key + '" aria-selected="' + (i === 0) + '" data-tab="' + st.key + '">' +
          '<span class="tab-n">' + st.n + '</span><span class="tab-text"><strong>' + st.name + '</strong><small>' + st.line + '</small></span>' +
          '<span class="tab-count" data-stage-count="' + st.key + '"></span></button>';
      });
      html += "</div>";
    }
    html += '<div class="stages">';
    STAGES.forEach(function (st, i) {
      html += '<section class="stage" id="panel-' + st.key + '" role="' + (layout === "tabs" ? "tabpanel" : "group") + '" aria-labelledby="' + (layout === "tabs" ? "tab-" + st.key : "h-" + st.key) + '"' + (layout === "tabs" && i > 0 ? " hidden" : "") + ">";
      html += '<header class="stage-head"><span class="stage-n">Stage ' + st.n + '</span><h3 id="h-' + st.key + '">' + st.name + '</h3><p>' + st.line + '. ' + st.body + '</p></header>';
      html += '<div class="cards">';
      SERVICES.filter(function (s) { return s.stage === st.key; }).forEach(function (s) {
        html += '<label class="svc" for="svc-' + s.id + '"><input type="checkbox" id="svc-' + s.id + '" value="' + s.id + '"' + (has(s.id) ? " checked" : "") + '>' +
          '<span class="svc-top"><span class="svc-title">' + esc(s.title) + '</span>' + (s.tag ? '<span class="svc-tag">' + s.tag + '</span>' : "") + '<span class="svc-check" aria-hidden="true"></span></span>' +
          '<span class="svc-desc">' + esc(s.desc) + '</span>' +
          '<span class="svc-get"><span>You get</span> ' + esc(s.get) + '</span></label>';
      });
      html += "</div></section>";
    });
    html += "</div>";
    root.innerHTML = html;

    root.addEventListener("change", function (e) {
      if (e.target.matches('input[type="checkbox"]')) { toggle(e.target.value); stageCounts(); }
    });
    root.querySelectorAll("[data-tab]").forEach(function (btn) {
      btn.addEventListener("click", function () { showTab(root, btn.getAttribute("data-tab")); });
      btn.addEventListener("keydown", function (e) {
        if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
        var tabs = Array.prototype.slice.call(root.querySelectorAll("[data-tab]"));
        var i = tabs.indexOf(btn) + (e.key === "ArrowRight" ? 1 : -1);
        var next = tabs[(i + tabs.length) % tabs.length];
        next.focus(); showTab(root, next.getAttribute("data-tab"));
      });
    });
    function stageCounts() {
      root.querySelectorAll("[data-stage-count]").forEach(function (el) {
        var k = el.getAttribute("data-stage-count");
        var c = sel.filter(function (id) { return byId(id).stage === k; }).length;
        el.textContent = c ? String(c) : "";
      });
    }
    stageCounts();
  }
  function showTab(root, key) {
    root.querySelectorAll("[data-tab]").forEach(function (b) { b.setAttribute("aria-selected", String(b.getAttribute("data-tab") === key)); });
    root.querySelectorAll(".stage").forEach(function (p) { p.hidden = p.id !== "panel-" + key; });
  }

  /* ---------- Two-step intake ---------- */
  function renderIntake(root) {
    var servicesHref = root.getAttribute("data-services-href") || "services.html";
    var step1 = root.querySelector('[data-step="1"]');
    var step2 = root.querySelector('[data-step="2"]');
    var done = root.querySelector('[data-step="done"]');
    var chips = root.querySelector("[data-chips]");
    var bar = root.querySelectorAll("[data-progress] li");

    function drawChips() {
      if (!sel.length) {
        chips.innerHTML = '<p class="chips-empty">No services picked yet. That\'s fine; describe the work below, or <a href="' + servicesHref + '">choose from the menu</a>.</p>';
        return;
      }
      chips.innerHTML = STAGES.map(function (st) {
        var items = sel.map(byId).filter(function (s) { return s.stage === st.key; });
        if (!items.length) return "";
        return '<div class="chip-group"><span class="chip-stage">' + st.name + '</span>' + items.map(function (s) {
          return '<span class="chip">' + esc(s.title) + '<button type="button" class="chip-x" data-remove="' + s.id + '" aria-label="Remove ' + esc(s.title) + '">×</button></span>';
        }).join("") + "</div>";
      }).join("") + '<a class="chips-edit" data-cta="' + servicesHref + '" href="' + servicesHref + '">Edit selection</a>';
      updateCtas();
    }
    chips.addEventListener("click", function (e) {
      var id = e.target.getAttribute && e.target.getAttribute("data-remove");
      if (id) { toggle(id); drawChips(); }
    });
    drawChips();

    function go(n) {
      step1.hidden = n !== 1; step2.hidden = n !== 2; done.hidden = n !== 3;
      bar.forEach(function (li, i) { li.classList.toggle("is-current", i === n - 1); li.classList.toggle("is-done", i < n - 1); });
      var focusTarget = root.querySelector('[data-step="' + (n === 3 ? "done" : n) + '"] h2, [data-step="' + (n === 3 ? "done" : n) + '"] h3');
      if (focusTarget) { focusTarget.setAttribute("tabindex", "-1"); focusTarget.focus({ preventScroll: true }); }
      root.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    step1.querySelector("form").addEventListener("submit", function (e) {
      e.preventDefault();
      var f = e.target;
      if (!f.reportValidity()) return;
      root.querySelector("[data-who]").textContent = (f.elements.fname.value || "").split(" ")[0] || "there";
      go(2);
    });
    root.querySelector("[data-back]").addEventListener("click", function () { go(1); });

    /* Mock calendar: next 5 weekdays, a few open times each. */
    var days = root.querySelector("[data-days]");
    var times = root.querySelector("[data-times]");
    var confirmBtn = root.querySelector("[data-confirm]");
    var picked = { day: null, time: null };
    var slots = ["9:00 AM", "10:30 AM", "1:00 PM", "2:30 PM", "4:00 PM"];
    var list = [];
    var d = new Date(); d.setHours(12, 0, 0, 0);
    while (list.length < 5) { d.setDate(d.getDate() + 1); if (d.getDay() !== 0 && d.getDay() !== 6) list.push(new Date(d)); }
    days.innerHTML = list.map(function (dt, i) {
      return '<button type="button" class="day" data-day="' + i + '" aria-pressed="false"><span>' + dt.toLocaleDateString("en-US", { weekday: "short" }) + '</span><strong>' + dt.getDate() + '</strong><small>' + dt.toLocaleDateString("en-US", { month: "short" }) + "</small></button>";
    }).join("");
    function drawTimes() {
      if (picked.day === null) { times.innerHTML = '<p class="times-empty">Pick a day to see open times.</p>'; return; }
      times.innerHTML = slots.filter(function (_, j) { return (j + picked.day) % 4 !== 3; }).map(function (t) {
        return '<button type="button" class="time" data-time="' + t + '" aria-pressed="' + (picked.time === t) + '">' + t + "</button>";
      }).join("");
    }
    days.addEventListener("click", function (e) {
      var b = e.target.closest("[data-day]"); if (!b) return;
      picked.day = +b.getAttribute("data-day"); picked.time = null;
      days.querySelectorAll("[data-day]").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      drawTimes(); confirmBtn.disabled = true;
    });
    times.addEventListener("click", function (e) {
      var b = e.target.closest("[data-time]"); if (!b) return;
      picked.time = b.getAttribute("data-time");
      times.querySelectorAll("[data-time]").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      confirmBtn.disabled = false;
    });
    drawTimes();
    confirmBtn.addEventListener("click", function () {
      var dt = list[picked.day];
      root.querySelector("[data-when]").textContent = dt.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric" }) + " at " + picked.time + " Pacific";
      go(3);
    });
  }

  document.querySelectorAll("[data-menu]").forEach(renderMenu);
  document.querySelectorAll("[data-intake]").forEach(renderIntake);
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = String(new Date().getFullYear()); });
  updateCtas();
})();
