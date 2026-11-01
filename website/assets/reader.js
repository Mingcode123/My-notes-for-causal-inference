const button=document.querySelector('.menu-button');const sidebar=document.querySelector('.sidebar');function closeNav(){sidebar?.classList.remove('is-open');button?.setAttribute('aria-expanded','false')}button?.addEventListener('click',()=>{const open=sidebar.classList.toggle('is-open');button.setAttribute('aria-expanded',String(open))});document.querySelector('.mobile-close')?.addEventListener('click',closeNav);document.addEventListener('keydown',event=>{if(event.key==='Escape')closeNav()});sidebar?.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{if(innerWidth<901)closeNav()}));document.addEventListener('click',event=>{if(innerWidth<901&&sidebar?.classList.contains('is-open')&&!sidebar.contains(event.target)&&!button?.contains(event.target))closeNav()});
const sectionData=document.getElementById('section-map');
if(sectionData){
  const sectionMap=JSON.parse(sectionData.textContent);
  function currentSection(){
    let anchor='';
    try{anchor=decodeURIComponent(location.hash.slice(1));}catch{}
    // A selected section anchor takes precedence over layout shifts during navigation.
    if(Object.prototype.hasOwnProperty.call(sectionMap,anchor))return anchor;
    let current=null;
    for(const heading of document.querySelectorAll('.article h2[id],.article h3[id],.article h4[id]')){
      if(!sectionMap[heading.id]||!heading.getClientRects().length)continue;
      if(heading.getBoundingClientRect().top<=150)current=heading.id;
    }
    return current;
  }
  document.querySelectorAll('.top-actions a:not([aria-current])').forEach(link=>{
    const base=link.href.split('#')[0];
    link.addEventListener('click',()=>{
      const current=currentSection();
      link.href=base+(current?'#'+encodeURIComponent(sectionMap[current]):'');
    });
  });
}
