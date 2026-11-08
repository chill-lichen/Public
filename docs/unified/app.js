/* Fictional sample data only. No network calls or analytics. */
(function(){
 for(const node of document.querySelectorAll("[data-current-year]"))node.textContent=String(new Date().getFullYear());
 const root=document.getElementById("owner-demo");
 if(!root)return;
 const records=[
  {month:"Jan",invoice:29800,received:27200,cost:16500,ar:11200,overdue:4400},
  {month:"Feb",invoice:32600,received:28900,cost:18500,ar:14900,overdue:5100},
  {month:"Mar",invoice:34400,received:36100,cost:19100,ar:13200,overdue:3900},
  {month:"Apr",invoice:33100,received:30800,cost:20300,ar:15500,overdue:6200},
  {month:"May",invoice:39400,received:35200,cost:22600,ar:19700,overdue:8300},
  {month:"Jun",invoice:42600,received:38200,cost:23100,ar:24100,overdue:11900}
 ];
 const money=n=>new Intl.NumberFormat("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0}).format(n);
 const el=id=>document.getElementById(id);
 const buttons=[...root.querySelectorAll("[data-month]")];
 const tableRows=[...root.querySelectorAll("[data-row-month]")];
 const pos=(n,i)=>[44+i*113,250-(n/50000)*210];
 function chart(){
  for(const [id,key] of [["invoiced-line","invoice"],["collected-line","received"]]){
   const p=el(id);if(!p)continue;
   p.setAttribute("d",records.map((r,i)=>(i===0?"M":"L")+pos(r[key],i).join(",")).join(" "));
  }
 }
 function render(index){
  const r=records[index];
  el("period-title").textContent=r.month+" management report";
  el("m-invoices").textContent=money(r.invoice);
  el("m-received").textContent=money(r.received);
  el("m-ar").textContent=money(r.ar);
  el("m-overdue").textContent=money(r.overdue);
  const delta=r.invoice-r.received;
  const flow=delta>0 ? "In "+r.month+", invoices were "+money(delta)+" higher than payments received."
   : delta<0 ? "In "+r.month+", payments received exceeded invoices by "+money(-delta)+"." : "Invoiced and collected amounts were equal this month.";
  const pct=Math.round(r.overdue/r.ar*100);
  el("owner-note").textContent=flow+" Customers owed "+money(r.ar)+" at month-end; "+money(r.overdue)+" ("+pct+"%) was overdue. That's a collection question worth examining before adding expenses.";
  el("m-contribution").textContent=money(r.invoice-r.cost);
  el("m-contribution-rate").textContent=(100*(r.invoice-r.cost)/r.invoice).toFixed(1)+"% of invoiced work, before overhead";
  buttons.forEach(b=>b.setAttribute("aria-pressed",b.dataset.month===r.month?"true":"false"));
  tableRows.forEach(row=>row.classList.toggle("selected-row",row.dataset.rowMonth===r.month));
  el("monthly-chart").setAttribute("aria-label","Fictional monthly invoices and collections from January to June. "+r.month+" selected: invoiced "+money(r.invoice)+", received "+money(r.received)+".");
  for(const [id,value] of [["selected-invoices-dot",r.invoice],["selected-collected-dot",r.received]]){
   const dot=el(id);if(!dot)continue;
   const [cx,cy]=pos(value,index);dot.setAttribute("cx",cx);dot.setAttribute("cy",cy);
  }
 }
 buttons.forEach(btn=>btn.addEventListener("click",()=>{
  const index=records.findIndex(r=>r.month===btn.dataset.month);
  if(index>=0)render(index);
 }));
 chart();render(5);
})();