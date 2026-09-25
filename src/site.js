document.documentElement.classList.add("js");

/* =====================================================================
   SETTINGS — edit these
   ===================================================================== */
const CONTACT_EMAIL = "info@eminentdestino.com";
const ROOT = document.body.dataset.root || "";      // "" on the home page, "../" on service pages
const PAGE = document.body.dataset.page || "home";  // "home" or a service id

/* Logo: the first file that loads is used. Put your logo at assets/logo.png (recommended). */
const LOGO_SOURCES = [
  ROOT + "assets/logo.jpg",
  ROOT + "assets/logo.png",
  "https://storage.jahinmusic.com/2026-09-18%2023.58.40.jpg",
  "https://eminentdestino.com/edo-logo.png"
];

/* Hero video: the first source the browser can play is used.
   Recommended: put an H.264 file at assets/hero.mp4 (see README). */
const HERO_VIDEO_SOURCES = [
  { src: ROOT + "assets/hero.mp4", type: "video/mp4" },
  { src: ROOT + "assets/hero.webm", type: "video/webm" },
  { src: "https://storage.jahinmusic.com/0717.mp4", type: "video/mp4" },
  { src: "https://storage.jahinmusic.com/0717.mov" }
];

/* =====================================================================
   DATA
   ===================================================================== */
const SERVICES = /*__SERVICES__*/[];
const SVC = Object.fromEntries(SERVICES.map(s=>[s.id,s]));
const MCN_COPY = /*__MCN_COPY__*/{};

/* Burmese for all static page text (English is read straight from the HTML) */
const MY = {
"nav.services":"ဝန်ဆောင်မှုများ","nav.mcn":"YouTube MCN","nav.partners":"မိတ်ဖက်များနှင့် API","nav.contact":"ဆက်သွယ်ရန်","cta.work":"EDO နှင့် လက်တွဲရန်",
"hero.badge":"မြန်မာနိုင်ငံ၏ ဒစ်ဂျစ်တယ် ဂေဟစနစ်ကို အားဖြည့်ပေးခြင်း",
"hero.l1":"မြန်မာ့ဖန်တီးသူများ","hero.l2":"ကမ္ဘာသို့ ရောက်ရှိစေမည်",
"hero.lead":"YouTube နှင့် Facebook ဝင်ငွေရရှိရေး၊ ဂီတဖြန့်ချိရေး၊ ဂီတထုတ်ဝေခွင့်၊ မူပိုင်ခွင့်ကာကွယ်ရေးနှင့် အခြားဝန်ဆောင်မှုများအပြင် B2B မိတ်ဖက်များအတွက် White Label နှင့် API ဝန်ဆောင်မှုများလည်း ပါရှိသည်။",
"hero.cta1":"ဝန်ဆောင်မှုများ ကြည့်ရန်","hero.cta2":"MCN တွင် ပါဝင်ရန်",
"play.btn":"ဗီဒီယိုဖွင့်ရန် နှိပ်ပါ",
"about.title":"ကုမ္ပဏီနှစ်ခု၊ မြန်မာနိုင်ငံအတွက် ပလက်ဖောင်းတစ်ခု။",
"about.p":"၂၀၂၆ ခုနှစ်တွင် Eminent (Jahin Music) နှင့် Destino တို့ ပူးပေါင်း၍ Eminent Destino ကို ထူထောင်ခဲ့ပါသည်။ ၎င်းသည် မြန်မာ့ဖန်တီးသူများအား ယခုရရှိနိုင်သည့် ရွေးချယ်စရာများထက် ပိုမိုကောင်းမွန်သော ဝန်ဆောင်မှု ပေးရန် ရည်ရွယ်သည့် ပလက်ဖောင်း ဖြစ်ပါသည်။",
"stat.1":"ဝန်ဆောင်မှု","stat.2":"ငွေထုတ်နည်းလမ်း","stat.3":"ငွေပေးချေမှု ငွေကြေး","stat.4v":"လစဉ်","stat.4":"ငွေပေးချေမှု ကာလ",
"ent.a":"အမေရိကန်ပြည်ထောင်စုတွင် ဌာနချုပ်ထားပြီး ယူအေအီးနှင့် ဘင်္ဂလားဒေ့ရှ်တို့တွင် ရုံးများရှိသော ဂီတဖြန့်ချိရေးနှင့် YouTube MCN ကုမ္ပဏီ။",
"ent.b":"ဒေသတွင်းဈေးကွက်ကို နက်ရှိုင်းစွာ နားလည်သော မြန်မာနိုင်ငံအခြေစိုက် Label နှင့် ဂီတဖြန့်ချိရေးကုမ္ပဏီ။",
"loc.usa":"အမေရိကန် (ဌာနချုပ်)","loc.uae":"ယူအေအီး","loc.bd":"ဘင်္ဂလားဒေ့ရှ်","loc.mm":"မြန်မာနိုင်ငံ",
"svc.title":"သင့်ဂီတနှင့် ချန်နယ်များ လိုအပ်သမျှ အားလုံး။",
"svc.sub":"ဝန်ဆောင်မှု ကိုးခု၊ မိတ်ဖက်တစ်ဦးတည်း။ ဝန်ဆောင်မှုတစ်ခုချင်းကို ဖွင့်ကြည့်ပြီး အလုပ်လုပ်ပုံကို ကြည့်ပါ။",
"svc.more":"ပိုမိုသိရှိရန်",
"mcn.title":"EDO နှင့်အတူ မြန်မာနိုင်ငံမှ ဝင်ငွေရယူပါ။",
"mcn.intro":"YouTube နှင့် Facebook ၏ ဝင်ငွေရရှိရေးစနစ်များကို မြန်မာနိုင်ငံအကောင့်များအတွက် တိုက်ရိုက်အသုံးပြု၍ မရနိုင်ပါ။ EDO ၏ Multi-Channel Network (MCN) တွင် ပါဝင်ပြီး စီမံခန့်ခွဲထားသော ကွန်ရက်မှတစ်ဆင့် ဝင်ငွေရယူနိုင်ပါသည်။ မူဝါဒလမ်းညွှန်မှုနှင့် မြန်မာဘာသာပြော ပံ့ပိုးရေးအဖွဲ့လည်း ရှိပါသည်။",
"mcn.methods":"ငွေထုတ်နည်းလမ်းများ","mcn.currency":"ငွေပေးချေမှု ငွေကြေး","pay.1":"ဘဏ်လွှဲပြောင်းမှု","pay.2":"Crypto","pay.mmk":"ကျပ် (MMK)","mcn.cta":"MCN တွင် ပါဝင်ရန်",
"mcn.1t":"ကျွန်ုပ်တို့၏ MCN တွင် ပါဝင်ပါ","mcn.1d":"သင့် YouTube ချန်နယ်များနှင့် Facebook Page များအတွက် EDO ၏ Multi-Channel Network တွင် ပါဝင်ပါ။ ချန်နယ်ကို အကျဉ်းချုပ်စစ်ဆေးပြီးနောက် စတင်ခြင်းနှင့် စီစဉ်မှုများကို ကျွန်ုပ်တို့အဖွဲ့က ဆောင်ရွက်ပေးပါမည်။",
"mcn.2t":"AdSense အကူအညီနှင့် မူဝါဒလမ်းညွှန်မှု","mcn.2d":"AdSense ဆိုင်ရာ ပြဿနာများတွင် ကူညီပေးပြီး သင့်ချန်နယ် ကောင်းမွန်သော အခြေအနေတွင် ရှိနေစေရန် YouTube မူဝါဒလမ်းညွှန်မှုများ ရှင်းလင်းစွာ ပေးပါသည်။ ပလက်ဖောင်းမူဝါဒက ခွင့်မပြုသည့်နေရာတွင် အတည်ပြုချက်ရမည်ဟု ကတိမပေးနိုင်ပါ။",
"mcn.3t":"လစဉ် အချိန်မှန် ငွေပေးချေမှု","mcn.3d":"သင့်ဝင်ငွေကို မည်သို့တွက်ချက်ထားသည်ကို ပြသသော ရှင်းလင်းသည့် ရှင်းတမ်းများနှင့်အတူ လစဉ် အချိန်မှန် ပေးချေပါသည်။",
"mcn.4t":"သင့်ငွေထုတ်နည်းလမ်း ရွေးချယ်ပါ","mcn.4d":"ဘဏ်လွှဲပြောင်းခြင်း၊ Crypto၊ KBZ Pay၊ Payoneer သို့မဟုတ် PayPal။ သင့်အတွက် အဆင်ပြေသည်ကို ရွေးချယ်နိုင်ပါသည်။",
"mcn.5t":"ကျပ် သို့မဟုတ် USD","mcn.5d":"မြန်မာကျပ် (MMK) ဖြင့် တိုက်ရိုက်ရယူနိုင်သလို လိုလားလျှင် USD ဖြင့်လည်း ရယူနိုင်ပါသည်။ ငွေမပေးချေမီ ငွေလဲနှုန်းကို ကြိုတင်ဖော်ပြပေးပါသည်။",
"mcn.6t":"ယှဉ်ပြိုင်နိုင်သော ဝေစုနှုန်း","mcn.6d":"ဝှက်ထားသော EDO ဆောင်ရွက်ခများ မပါဘဲ ယှဉ်ပြိုင်နိုင်သော ဝင်ငွေခွဲဝေမှု ရရှိပါမည်။ တစ်ဦးချင်း သို့မဟုတ် ဒေသဆိုင်ရာ အခွန်များကို ဖန်တီးသူကိုယ်တိုင် တာဝန်ယူရပါမည်။",
"mcn.7t":"မြန်မာဘာသာပြော ပံ့ပိုးရေးအဖွဲ့","mcn.7d":"မြန်မာဘာသာ ပြောဆိုနိုင်ပြီး ဒေသတွင်းဖန်တီးသူများ၊ ငွေပေးချေမှုနှင့် နေ့စဉ်ချန်နယ်ပြဿနာများကို နားလည်သော အဖွဲ့နှင့် ဆက်သွယ်နိုင်ပါသည်။",
"wl.title":"စနစ်တစ်ခုတည်း၊ သင့်ကိုယ်ပိုင်အမှတ်တံဆိပ်ဖြင့်။",
"wl.intro":"Label များ၊ ဖြန့်ချိသူများနှင့် B2B ဖောက်သည်များအတွက် White Label နှင့် API ဝန်ဆောင်မှုများ — EDO ၏ ဖြန့်ချိရေး၊ MCN နှင့် မူပိုင်ခွင့်ကိရိယာများကို သင့်ကိုယ်ပိုင်အမှတ်တံဆိပ်အောက်တွင် လည်ပတ်နိုင်သည်၊ သို့မဟုတ် သင့်ပလက်ဖောင်းကို ကျွန်ုပ်တို့ပလက်ဖောင်းနှင့် တိုက်ရိုက်ချိတ်ဆက်နိုင်သည်။",
"wl.1t":"White-label ဒက်ရှ်ဘုတ်","wl.1d":"သင့်လိုဂို၊ သင့်ဒိုမိန်း၊ သင့်အရောင်များဖြင့်။ သင့်မိတ်ဖက်များသည် အခြားအမှတ်တံဆိပ်ကို မမြင်ရပါ။",
"wl.2t":"REST API","wl.2d":"သင့်ကိုယ်ပိုင်စနစ်မှ တိုက်ရိုက် Release များ ဖန်တီးခြင်း၊ ကတ်တလော့ တင်ခြင်းနှင့် ဝင်ငွေရှင်းတမ်းများ ရယူခြင်းတို့ကို လုပ်ဆောင်နိုင်သည်။",
"wl.3t":"Webhooks","wl.3d":"ပို့ဆောင်မှုအခြေအနေ၊ Claim များနှင့် ငွေပေးချေမှုများကို ဖြစ်ပေါ်သည့်အတိုင်း အကြောင်းကြားချက် ရရှိမည်။",
"wl.4t":"Sub-account များနှင့် ခွင့်ပြုချက်များ","wl.4d":"Label တစ်ခုချင်းစီ၊ ဖန်တီးသူတစ်ဦးချင်းစီကို ကိုယ်ပိုင် Login နှင့် ခွင့်ပြုချက်များ ပေးနိုင်သည်။",
"wl.5t":"Royalty အစီရင်ခံစာများ","wl.5d":"သင့်အသုံးပြုသူများထံ ပေးပို့နိုင်သည့် ရှင်းလင်းသော ဝင်ငွေရှင်းတမ်းများနှင့် ခွဲဝေမှုစည်းမျဉ်းများ။",
"wl.6t":"ချိတ်ဆက်မှု ပံ့ပိုးမှု","wl.6d":"EDO မှ တာဝန်ခံတစ်ဦးက သင့်အဖွဲ့ စတင်အသုံးပြုနိုင်ရန်နှင့် ဆက်လက်ပံ့ပိုးရန် ကူညီပေးမည်။",
"wl.cta1":"API ဝင်ရောက်ခွင့် တောင်းဆိုရန်","wl.cta2":"White Label ဝန်ဆောင်မှုများ ကြည့်ရန်",
"wl.tab1":"Release ဖန်တီးရန်","wl.tab2":"ဝင်ငွေရှင်းတမ်း ရယူရန်","wl.tab3":"Webhook",
"wl.note":"နမူနာသာ ဖြစ်သည်။ Endpoint နှင့် Field များကို အတည်ပြုထားသော မိတ်ဖက်များထံ ပေးပို့မည်။",
"flow.brand":"သင့်အမှတ်တံဆိပ်","flow.brandsub":"ဒက်ရှ်ဘုတ်၊ ဒိုမိန်း၊ အက်ပ်","flow.hub":"မူပိုင်ခွင့်၊ ဖြန့်ချိမှု၊ ငွေပေးချေမှု","flow.dest":"ကမ္ဘာ့ပလက်ဖောင်းများ","flow.d3":"ဂီတပလက်ဖောင်းများ","flow.d5":"ရုပ်ရှင်နှင့် ဇာတ်လမ်းတွဲ",
"ct.title":"သင့်လက်ရာသည် ပိုကြီးသော စင်မြင့်ကို ထိုက်တန်သည်။",
"ct.sub":"အနုပညာရှင်များ၊ Label များ၊ ဖန်တီးသူများနှင့် မီဒီယာမိတ်ဖက်များ — မြန်မာနိုင်ငံမှ သင့်ကမ္ဘာလုံးဆိုင်ရာ ဒစ်ဂျစ်တယ်အနာဂတ်ကို အတူတကွ တည်ဆောက်ကြပါစို့။",
"ct2.title":"စတင်ရန် အဆင်သင့်ဖြစ်ပါပြီလား? သင့်စီမံကိန်းအကြောင်း ပြောပြပါ။","ct2.sub":"အသေးစိတ်အချက်အလက် အနည်းငယ် ပို့ပေးပါ၊ ကျွန်ုပ်တို့အဖွဲ့က အီးမေးလ်ဖြင့် ပြန်ကြားပါမည်။",
"ct.name":"အမည်","ct.email":"အီးမေးလ်","ct.company":"ကုမ္ပဏီ သို့မဟုတ် ချန်နယ်","ct.interest":"စိတ်ဝင်စားသည့် ဝန်ဆောင်မှု","ct.msg":"မက်ဆေ့ချ်","ct.send":"မက်ဆေ့ချ် ပို့ရန်",
"ft.line":"Eminent (Jahin Music) နှင့် Destino တို့၏ ဖက်စပ်လုပ်ငန်း။ မြန်မာ့ဒစ်ဂျစ်တယ်ဖန်တီးသူများအတွက် ဖန်တီးထားသည်။",
"ft.services":"ဝန်ဆောင်မှုများ","ft.offices":"ရုံးများ","ft.contact":"ဆက်သွယ်ရန်","ft.eminent.h":"Eminent (Jahin Music)",
"ft.eminent":"အမေရိကန် (ဌာနချုပ်)၊ ယူအေအီး၊ ဘင်္ဂလားဒေ့ရှ်","ft.destino":"မြန်မာနိုင်ငံ","soon":"လင့်ခ်ကို မကြာမီ ထည့်သွင်းမည်","ft.top":"အပေါ်သို့ ပြန်သွားရန်",
"crumb.home":"ပင်မစာမျက်နှာ","crumb.services":"ဝန်ဆောင်မှုများ",
"sp.for":"မည်သူများအတွက်လဲ","sp.inc":"ပါဝင်သည်များ","sp.how":"အလုပ်လုပ်ပုံ","sp.start":"စတင်ရန်","sp.email":"အီးမေးလ်ပို့ရန်",
"sp.prev":"ယခင်ဝန်ဆောင်မှု","sp.next":"နောက်ဝန်ဆောင်မှု","sp.more":"အခြားဝန်ဆောင်မှုများ","sp.all":"ဝန်ဆောင်မှုအားလုံး ကြည့်ရန်",
"x.api":"နမူနာ API request တစ်ခု","x.flow":"အစိတ်အပိုင်းများ ပေါင်းစပ်ပုံ",
"payx.title":"သင့်နည်းလမ်းအတိုင်း ငွေရယူပါ။","payx.note":"လစဉ် အချိန်မှန် ပေးချေပါသည်။ ငွေမပေးချေမီ ငွေလဲနှုန်းကို ကြိုတင်ဖော်ပြပါသည်။",
"meta.title":"Eminent Destino (EDO) — မြန်မာ့ဖန်တီးသူများ၊ ကမ္ဘာသို့ ရောက်ရှိစေမည်",
"msg.ok":"သင့်မက်ဆေ့ချ်ပါသော အီးမေးလ်အက်ပ် ပွင့်လာပါမည်။ မပွင့်လျှင် {email} သို့ တိုက်ရိုက်ရေးပို့ပါ။",
"msg.err":"အမည်နှင့် မှန်ကန်သော အီးမေးလ်ကို ဖြည့်ပေးပါ။",
"detail.eyebrow":"ဝန်ဆောင်မှုအကြောင်း အသေးစိတ်",
"detail.partner":"သင့် EDO မိတ်ဖက်ဆက်ဆံရေး",
"detail.talk":"သင့်စီမံကိန်းအကြောင်း ဆွေးနွေးကြပါစို့",
"detail.prepare":"ပြင်ဆင်ထားရမည့်အရာများ",
"detail.prepareNote":"အချက်အလက်အနည်းငယ်က ပထမဆွေးနွေးမှုကို ပိုအသုံးဝင်စေပါသည်။",
"detail.before":"မစတင်မီ သိထားရန်",
"detail.faq":"သိလိုသောမေးခွန်းများနှင့် ရှင်းလင်းသောအဖြေများ။",
"detail.faqNote":"အသေးစိတ်ဖတ်ရှုပြီး သင့်စီမံကိန်းအကြောင်း ကျွန်ုပ်တို့နှင့် ဆွေးနွေးပါ။",
"detail.overview":"ဝန်ဆောင်မှုအကျဉ်းချုပ်",
"detail.why":"EDO ကို ရွေးချယ်ရသည့်အကြောင်း",
"detail.faqShort":"မေးလေ့ရှိသောမေးခွန်းများ",
"detail.nav":"ဝန်ဆောင်မှုကဏ္ဍများ"
};
Object.assign(MY, MCN_COPY, {
  "explore.label":"သင့်အတွက် စတင်ရာနေရာ",
  "explore.title":"မည်သည့်အကူအညီ လိုအပ်ပါသလဲ။",
  "explore.aria":"ဝန်ဆောင်မှုရွေးချယ်ရန်",
  "explore.creator":"ကျွန်ုပ်၏ YouTube ချန်နယ်",
  "explore.artist":"ကျွန်ုပ်၏ ဂီတထုတ်ဝေမှု",
  "explore.partner":"ကျွန်ုပ်၏ ဖန်တီးသူလုပ်ငန်း",
  "explore.action":"ဤဝန်ဆောင်မှုကို ကြည့်ရန်"
});
const EN = {
 "meta.title":document.title,
 "msg.ok":"Your email app is opening with your message ready. If nothing opens, write to {email} directly.",
 "msg.err":"Please add your name and a valid email."
};

let LANG="en";
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
$$("[data-i18n]").forEach(el=>{ if(!(el.dataset.i18n in EN)) EN[el.dataset.i18n]=el.textContent.trim(); });
$$("[data-i18n-aria]").forEach(el=>{ EN[el.dataset.i18nAria]=el.getAttribute("aria-label"); });
const t=k=>(LANG==="my"&&MY[k]!==undefined)?MY[k]:(EN[k]!==undefined?EN[k]:k);
function sv(id,f){
  const s=SVC[id]; if(!s) return undefined;
  const [k,i]=f.split(".");
  const pick=o=>i===undefined?o[k]:(o[k]||[])[+i];
  const m=LANG==="my"?pick(s.my):undefined;
  return m!==undefined?m:pick(s.en);
}

/* internal page links keep the chosen language (?lang=my) even when opened from a folder */
const pageLinks=$$("a[href]").filter(a=>{ const h=a.getAttribute("href"); return h&&!/^(#|mailto:|https?:|tel:)/.test(h); });
pageLinks.forEach(a=>{ a.dataset.h0=a.getAttribute("href"); });
function syncLinks(l){
  pageLinks.forEach(a=>{
    const [p,hash]=a.dataset.h0.split("#"); const clean=p.split("?")[0];
    a.setAttribute("href", clean+(l==="my"?"?lang=my":"")+(hash?"#"+hash:""));
  });
}

/* =====================================================================
   LANGUAGE
   ===================================================================== */
function setLang(l){
  LANG=l;
  document.documentElement.lang=l==="my"?"my":"en";
  $$("[data-i18n]").forEach(el=>{ el.textContent=t(el.dataset.i18n); });
  $$("[data-i18n-aria]").forEach(el=>{ el.setAttribute("aria-label",t(el.dataset.i18nAria)); });
  $$("[data-s]").forEach(el=>{ const [id,f]=el.dataset.s.split("|"); const v=sv(id,f); if(v!==undefined) el.textContent=v; });
  $$(".lang button").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.lang===l)));
  syncLinks(l); updateExplorer();
  if(l==="my") document.title = PAGE==="home" ? t("meta.title") : sv(PAGE,"t")+" — Eminent Destino";
  else document.title = document.querySelector('meta[property="og:title"]').content;
  try{ localStorage.setItem("edo-lang",l); }catch(e){}
}
$$(".lang button").forEach(b=>b.addEventListener("click",()=>setLang(b.dataset.lang)));

/* =====================================================================
   HEADER / MENU / PROGRESS
   ===================================================================== */
const bar=$("#progress");
function onScroll(){ const h=document.documentElement; const p=h.scrollTop/(h.scrollHeight-h.clientHeight||1); bar.style.transform="scaleX("+Math.min(1,Math.max(0,p))+")"; }
addEventListener("scroll",onScroll,{passive:true}); onScroll();
const burger=$("#burger"), mm=$("#mmenu");
burger.addEventListener("click",()=>{ const o=mm.classList.toggle("open"); burger.setAttribute("aria-expanded",String(o)); });
$$("#mmenu a").forEach(a=>a.addEventListener("click",()=>{ mm.classList.remove("open"); burger.setAttribute("aria-expanded","false"); }));

/* =====================================================================
   LOGO LOADER (tries each source; shows a clean EDO wordmark if none load)
   ===================================================================== */
$$(".logo").forEach(logo=>{
  const img=$(".logo__img",logo); let i=0;
  (function next(){
    if(i>=LOGO_SOURCES.length) return;
    const src=LOGO_SOURCES[i++], probe=new Image();
    probe.referrerPolicy="no-referrer";
    probe.onload=()=>{ img.src=src; logo.classList.add("has-img"); };
    probe.onerror=next;
    probe.src=src;
  })();
});

/* =====================================================================
   HERO VIDEO (home only)
   ===================================================================== */
const hero=$("#hero"), vid=$("#heroVideo"), playBtn=$("#playBtn");
const reduceMotion=matchMedia("(prefers-reduced-motion: reduce)").matches;

/* Keep the accent centered on the native pointer hotspot, without a trailing delay. */
if(!reduceMotion && matchMedia("(hover:hover) and (pointer:fine)").matches){
  const orbit=document.createElement("span"); orbit.className="cursor-orbit";
  orbit.setAttribute("aria-hidden","true"); document.body.appendChild(orbit);
  document.addEventListener("pointermove",e=>{
    if(e.pointerType!=="mouse") return;
    orbit.style.transform=`translate3d(${e.clientX}px,${e.clientY}px,0) translate(-50%,-50%)`;
    orbit.classList.add("is-visible");
    orbit.classList.toggle("is-interactive",!!e.target.closest("a,button,input,select,textarea,summary,[role=button]"));
  },{passive:true});
  document.addEventListener("pointerleave",()=>orbit.classList.remove("is-visible"));
  addEventListener("blur",()=>orbit.classList.remove("is-visible"));
}
if(hero&&vid){
  HERO_VIDEO_SOURCES.forEach((v,i)=>{
    const s=document.createElement("source"); s.src=v.src; if(v.type) s.type=v.type;
    if(i===HERO_VIDEO_SOURCES.length-1) s.addEventListener("error",()=>hero.classList.add("no-video"));
    vid.appendChild(s);
  });
  vid.muted=true; vid.defaultMuted=true; vid.setAttribute("muted",""); vid.setAttribute("playsinline","");
  ["loadeddata","canplay","playing"].forEach(ev=>vid.addEventListener(ev,()=>{ hero.classList.add("video-ready"); hero.classList.remove("no-video"); }));
  vid.addEventListener("error",()=>hero.classList.add("no-video"));
  setTimeout(()=>{ if(vid.readyState<2) hero.classList.add("no-video"); },6000);
  const tryPlay=()=>{ const p=vid.play(); if(p&&p.catch) p.catch(()=>{ if(hero.classList.contains("video-ready")) playBtn.hidden=false; }); };
  vid.load(); if(reduceMotion) vid.pause(); else tryPlay();
  playBtn.addEventListener("click",()=>{ vid.muted=true; vid.play().then(()=>{ playBtn.hidden=true; }).catch(()=>{}); });
  vid.addEventListener("playing",()=>{ playBtn.hidden=true; });
  new IntersectionObserver(es=>es.forEach(e=>{ if(reduceMotion) return; e.isIntersecting?tryPlay():vid.pause(); }),{threshold:.05}).observe(hero);
  const eb=$("#eqbars"); for(let i=0;i<26;i++){ const b=document.createElement("i"); b.style.animationDelay=(-Math.random()*1.2).toFixed(2)+"s"; b.style.animationDuration=(0.7+Math.random()*0.9).toFixed(2)+"s"; eb.appendChild(b); }
}

/* Service explorer: a small recommendation, with a direct route to the full service. */
let activeExplore="youtube-mcn";
const exploreText={
  "youtube-mcn":{en:"Channel monetization, rights support and a clear monthly settlement process.",my:"ချန်နယ်ဝင်ငွေရရှိရေး၊ မူပိုင်ခွင့်ပံ့ပိုးမှုနှင့် လစဉ်ငွေရှင်းမှု လုပ်ငန်းစဉ်။"},
  "music-distribution":{en:"Release your recordings to music services and manage the catalog in one place.",my:"ဂီတပလက်ဖောင်းများသို့ သင့်အသံဖိုင်များ ဖြန့်ချိပြီး ကတ်တလော့ကို တစ်နေရာတည်းတွင် စီမံပါ။"},
  "white-label":{en:"Give your creators distribution and network services under your own brand.",my:"သင့်အမှတ်တံဆိပ်ဖြင့် ဖန်တီးသူများကို ဖြန့်ချိရေးနှင့် ကွန်ရက်ဝန်ဆောင်မှုများ ပေးပါ။"}
};
function updateExplorer(){
  const name=$("#explorerName"); if(!name) return;
  name.textContent=sv(activeExplore,"t");
  $("#explorerText").textContent=exploreText[activeExplore][LANG];
  $("#explorerLink").href="services/"+activeExplore+".html"+(LANG==="my"?"?lang=my":"");
  $$("[data-explore]").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.explore===activeExplore)));
}
$$("[data-explore]").forEach(b=>b.addEventListener("click",()=>{activeExplore=b.dataset.explore;updateExplorer();}));

/* The example is calculated from finalized earnings; it is not a payout promise. */
const earnings=$("#mcnEarnings");
if(earnings){
  const update=()=>{$("#mcnResult").textContent=new Intl.NumberFormat("en-US",{style:"currency",currency:"USD"}).format(Math.max(0,Math.min(1e9,Number(earnings.value)||0))*.8);};
  earnings.addEventListener("input",update); update();
}

/* =====================================================================
   REVEALS, ROWS, COUNTERS, TILE GLOW
   ===================================================================== */
const io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target);} }),{threshold:.12,rootMargin:"0px 0px -6% 0px"});
$$("[data-reveal],[data-row]").forEach(el=>io.observe(el));
const co=new IntersectionObserver(es=>es.forEach(e=>{
  if(!e.isIntersecting) return; co.unobserve(e.target);
  const end=+e.target.dataset.count, t0=performance.now();
  (function step(now){ const k=Math.min(1,(now-t0)/1200); e.target.textContent=String(Math.round(end*(1-Math.pow(1-k,3)))).padStart(2,"0"); if(k<1) requestAnimationFrame(step); })(t0);
}),{threshold:.6});
$$("[data-count]").forEach(el=>co.observe(el));
if(matchMedia("(pointer:fine)").matches){
  $$("[data-tilt]").forEach(el=>el.addEventListener("pointermove",e=>{ const r=el.getBoundingClientRect(); el.style.setProperty("--mx",(e.clientX-r.left)+"px"); el.style.setProperty("--my",(e.clientY-r.top)+"px"); }));
}

/* =====================================================================
   API SAMPLE (home + API page)
   ===================================================================== */
const SAMPLES={
 release:{req:'POST /v1/releases\nAuthorization: Bearer YOUR_API_KEY\n\n{\n  "title": "Ayeyarwady Nights",\n  "artist_id": "art_1024",\n  "type": "single",\n  "territories": ["worldwide"],\n  "release_date": "2026-11-01"\n}',
          res:'201 Created\n{\n  "id": "rel_88f2",\n  "status": "in_review",\n  "brand": "your-label"\n}'},
 statement:{req:'GET /v1/statements?period=2026-09\nAuthorization: Bearer YOUR_API_KEY',
          res:'200 OK\n{\n  "period": "2026-09",\n  "status": "ready",\n  "payout_currency": "MMK",\n  "download_url": "https://…/statement.csv"\n}'},
 webhook:{req:'POST https://your-app.com/edo-webhook\nX-EDO-Signature: sha256=…',
          res:'{\n  "event": "claim.resolved",\n  "channel_id": "ch_5521",\n  "status": "monetized"\n}'}
};
const esc=s=>s.replace(/&/g,"&amp;").replace(/</g,"&lt;");
function hl(line){
  let s=esc(line);
  s=s.replace(/^(\d{3} [A-Za-z ]+)$/,'<span class="m">$1</span>');
  s=s.replace(/^(GET|POST|PUT|DELETE)(\s)/,'<span class="m">$1</span>$2');
  s=s.replace(/"([^"]+)":/g,'<span class="k">"$1"</span>:').replace(/: "([^"]*)"/g,': <span class="s">"$1"</span>');
  return s;
}
let typeTimer;
function showTab(name){
  $$(".tabs button").forEach(b=>b.setAttribute("aria-selected",String(b.dataset.tab===name)));
  const smp=SAMPLES[name], reqEl=$("#codeReq"), resEl=$("#codeRes");
  clearTimeout(typeTimer);
  reqEl.innerHTML='<span class="lbl">REQUEST</span>'+smp.req.split("\n").map(hl).join("\n");
  resEl.innerHTML='<span class="lbl">RESPONSE</span>';
  const lines=smp.res.split("\n"); let i=0;
  (function next(){
    if(i>=lines.length) return;
    const d=document.createElement("span"); d.className="ln"; d.innerHTML=hl(lines[i]); resEl.appendChild(d); i++;
    if(reduceMotion) next(); else typeTimer=setTimeout(next,120);
  })();
}
if($("#codeReq")){ $$(".tabs button").forEach(b=>b.addEventListener("click",()=>showTab(b.dataset.tab))); showTab("release"); }

/* =====================================================================
   CONTACT
   ===================================================================== */
const sel=$("#interest");
document.addEventListener("click",e=>{ const el=e.target.closest("[data-interest]"); if(el&&sel) sel.value=el.dataset.interest; });
[$("#mailLink"),$("#mailLink2"),$("#mailBtn")].forEach(a=>{ if(a){ a.href="mailto:"+CONTACT_EMAIL; if(a.id!=="mailBtn") a.textContent=CONTACT_EMAIL; } });
const form=$("#form");
if(form){
  form.addEventListener("submit",e=>{
    e.preventDefault();
    const f=e.target, m=$("#msg"), name=f.name.value.trim(), email=f.email.value.trim();
    if(!name||!/^\S+@\S+\.\S+$/.test(email)){ m.className="msg err"; m.textContent=t("msg.err"); return; }
    const opt=sv(f.interest.value,"t");
    const body="Name: "+name+"\nEmail: "+email+"\nCompany/Channel: "+f.company.value.trim()+"\nInterested in: "+opt+"\n\n"+f.message.value.trim();
    location.href="mailto:"+CONTACT_EMAIL+"?subject="+encodeURIComponent("EDO enquiry — "+opt)+"&body="+encodeURIComponent(body);
    m.className="msg ok"; m.textContent=t("msg.ok").replace("{email}",CONTACT_EMAIL);
  });
}
$("#yr").textContent=new Date().getFullYear();

/* =====================================================================
   START
   ===================================================================== */
const qs=new URLSearchParams(location.search);
if(sel){ const pre=qs.get("s")||(PAGE!=="home"?PAGE:null); if(pre&&SVC[pre]) sel.value=pre; }
let saved=null; try{ saved=localStorage.getItem("edo-lang"); }catch(e){}
const start=qs.get("lang")||saved||((navigator.language||"").toLowerCase().startsWith("my")?"my":"en");
setLang(start==="my"?"my":"en");
