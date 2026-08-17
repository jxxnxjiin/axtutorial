/* ax-tutor — shared behaviour for hub + generated wiki pages */
(function(){
  // ---- live clock ----
  var clock=document.getElementById('clock');
  if(clock){
    var tick=function(){var d=new Date();clock.textContent=String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0');};
    tick();setInterval(tick,10000);
  }

  // ---- typed prompt (hub only) ----
  var el=document.getElementById('typed');
  if(el){
    var target=el.getAttribute('data-text')||'오늘 배울 것을 한 눈에 보여줘',i=0;
    (function type(){ if(i<=target.length){el.textContent=target.slice(0,i++);setTimeout(type,55);} 
  // ---- 코드블록 복사 버튼: .md 안 모든 pre(예시 프롬프트 포함) 우상단 ----
  [].slice.call(document.querySelectorAll('.md pre')).forEach(function(pre){
    if(pre.closest('.codewrap'))return;
    var wrap=document.createElement('div');wrap.className='codewrap';
    pre.parentNode.insertBefore(wrap,pre);wrap.appendChild(pre);
    var btn=document.createElement('button');
    btn.type='button';btn.className='copybtn mono';btn.textContent='⧉ 복사';
    btn.addEventListener('click',function(){
      var text=(pre.querySelector('code')||pre).innerText.replace(/\n$/,'');
      var done=function(){btn.textContent='✓ 복사됨';btn.classList.add('ok');
        setTimeout(function(){btn.textContent='⧉ 복사';btn.classList.remove('ok');},1600);};
      var fallback=function(){var ta=document.createElement('textarea');ta.value=text;document.body.appendChild(ta);
        ta.select();document.execCommand('copy');document.body.removeChild(ta);done();};
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done).catch(fallback);}
      else{fallback();}
    });
    wrap.appendChild(btn);
  });
})();
  }

  // ---- theme toggle ----
  var root=document.documentElement, tb=document.getElementById('themeBtn');
  try{var saved=localStorage.getItem('ax-theme'); if(saved)root.setAttribute('data-theme',saved);}catch(e){}
  function sync(){
    var l=root.getAttribute('data-theme')==='light';
    var ic=document.getElementById('themeIc'), lbl=document.getElementById('themeLbl');
    if(ic)ic.textContent=l?'◑':'◐'; if(lbl)lbl.textContent=l?'dark':'light';
  }
  sync();
  if(tb)tb.addEventListener('click',function(){
    var next=root.getAttribute('data-theme')==='light'?'dark':'light';
    root.setAttribute('data-theme',next); try{localStorage.setItem('ax-theme',next);}catch(e){} sync();
  });

  // ---- mobile drawer ----
  var side=document.getElementById('side'), burger=document.getElementById('burger');
  if(side&&burger){
    burger.addEventListener('click',function(e){e.stopPropagation();side.classList.toggle('open');});
    side.addEventListener('click',function(e){ if(e.target.closest('.nav-a')&&e.target.closest('.nav-a').getAttribute('href').indexOf('#')===0)side.classList.remove('open'); });
    document.addEventListener('click',function(e){ if(side.classList.contains('open')&&!e.target.closest('#side')&&!e.target.closest('#burger'))side.classList.remove('open'); });
  }

  // ---- sidebar scroll 유지: 페이지 이동 시 스크롤 위치 저장/복원 ----
  var sideNav=document.querySelector('#side nav');
  if(sideNav){
    try{
      var savedTop=sessionStorage.getItem('ax-side-scroll');
      if(savedTop!==null){ sideNav.scrollTop=+savedTop; }
      else{
        var act=sideNav.querySelector('.nav-a.active');
        if(act)act.scrollIntoView({block:'center'});
      }
    }catch(e){}
    window.addEventListener('pagehide',function(){
      try{sessionStorage.setItem('ax-side-scroll',sideNav.scrollTop);}catch(e){}
    });
  }

  // ---- generic scrollspy: highlight in-page toc + nav anchors ----
  var links=[].slice.call(document.querySelectorAll('.toc a[href^="#"], .nav-a[href^="#"]'));
  var map={}; // id -> {toc:[], nav:[]}
  links.forEach(function(a){
    var id=a.getAttribute('href').slice(1); if(!id)return;
    (map[id]=map[id]||{toc:[],nav:[]})[a.classList.contains('nav-a')?'nav':'toc'].push(a);
  });
  var ids=Object.keys(map).filter(function(id){return document.getElementById(id);});
  if(ids.length){
    var clearAll=function(){links.forEach(function(a){a.classList.remove('on');if(a.classList.contains('nav-a'))a.classList.remove('active');});};
    var activate=function(id){
      clearAll();
      (map[id].toc||[]).forEach(function(a){a.classList.add('on');});
      (map[id].nav||[]).forEach(function(a){a.classList.add('active');});
    };
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if(en.isIntersecting)activate(en.target.id); });
    },{rootMargin:'-12% 0px -72% 0px',threshold:0});
    ids.forEach(function(id){io.observe(document.getElementById(id));});
  }

  // ---- 코드블록 복사 버튼: .md 안 모든 pre(예시 프롬프트 포함) 우상단 ----
  [].slice.call(document.querySelectorAll('.md pre')).forEach(function(pre){
    if(pre.closest('.codewrap'))return;
    var wrap=document.createElement('div');wrap.className='codewrap';
    pre.parentNode.insertBefore(wrap,pre);wrap.appendChild(pre);
    var btn=document.createElement('button');
    btn.type='button';btn.className='copybtn mono';btn.textContent='⧉ 복사';
    btn.addEventListener('click',function(){
      var text=(pre.querySelector('code')||pre).innerText.replace(/\n$/,'');
      var done=function(){btn.textContent='✓ 복사됨';btn.classList.add('ok');
        setTimeout(function(){btn.textContent='⧉ 복사';btn.classList.remove('ok');},1600);};
      var fallback=function(){var ta=document.createElement('textarea');ta.value=text;document.body.appendChild(ta);
        ta.select();document.execCommand('copy');document.body.removeChild(ta);done();};
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done).catch(fallback);}
      else{fallback();}
    });
    wrap.appendChild(btn);
  });
})();
