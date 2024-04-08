var Lr=Object.defineProperty;var Br=(e,t,r)=>t in e?Lr(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r;var E=(e,t,r)=>(Br(e,typeof t!="symbol"?t+"":t,r),r);import{x as b,f as A,y as L,R as y,a6 as Wr,z as dt,a3 as Ur,r as h,g as he,i as Fr,h as kt,D as He,a4 as Fe,I as ce,a5 as Ar,a7 as Hr,a8 as Kr,B as fe,a9 as Gr,aa as qr,k as qe,m as Yr,l as ee,A as te,s as Te,a as q,b as Ct,j as n,q as Zr,M as Ye,d as de,T as J,Y as Qr,Q as Jr,p as ge,F as X,ab as je,c as be}from"./index-14422766.js";import{c as Xr,M as Pe}from"./Menu-676c93e5.js";import{u as ea,g as ta,b as ra,f as Ke,T as aa,S as It}from"./index-e05497de.js";import{D as na,u as oa,g as sa,S as Ae,a as la,b as ia,c as ca}from"./get-select-right-section-props-739d3de5.js";import"./Popover-344254a7.js";function ut(e,t){return r=>{if(typeof r!="string"||r.trim().length===0)throw new Error(t);return`${e}-${r}`}}const Dt={xs:b(16),sm:b(22),md:b(26),lg:b(30),xl:b(36)},da={xs:b(10),sm:b(12),md:b(14),lg:b(16),xl:b(18)};var ua=A((e,{disabled:t,radius:r,readOnly:a},{size:s,variant:c})=>({defaultValue:{display:"flex",alignItems:"center",backgroundColor:t?e.colorScheme==="dark"?e.colors.dark[5]:e.colors.gray[3]:e.colorScheme==="dark"?e.colors.dark[7]:c==="filled"?e.white:e.colors.gray[1],color:t?e.colorScheme==="dark"?e.colors.dark[1]:e.colors.gray[7]:e.colorScheme==="dark"?e.colors.dark[0]:e.colors.gray[7],height:L({size:s,sizes:Dt}),paddingLeft:`calc(${L({size:s,sizes:e.spacing})} / 1.5)`,paddingRight:t||a?L({size:s,sizes:e.spacing}):0,fontWeight:500,fontSize:L({size:s,sizes:da}),borderRadius:L({size:r,sizes:e.radius}),cursor:t?"not-allowed":"default",userSelect:"none",maxWidth:`calc(100% - ${b(10)})`},defaultValueRemove:{color:e.colorScheme==="dark"?e.colors.dark[0]:e.colors.gray[7],marginLeft:`calc(${L({size:s,sizes:e.spacing})} / 6)`},defaultValueLabel:{display:"block",overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"}}));const pa=ua;var fa=Object.defineProperty,$e=Object.getOwnPropertySymbols,Nt=Object.prototype.hasOwnProperty,Tt=Object.prototype.propertyIsEnumerable,pt=(e,t,r)=>t in e?fa(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,ha=(e,t)=>{for(var r in t||(t={}))Nt.call(t,r)&&pt(e,r,t[r]);if($e)for(var r of $e(t))Tt.call(t,r)&&pt(e,r,t[r]);return e},ga=(e,t)=>{var r={};for(var a in e)Nt.call(e,a)&&t.indexOf(a)<0&&(r[a]=e[a]);if(e!=null&&$e)for(var a of $e(e))t.indexOf(a)<0&&Tt.call(e,a)&&(r[a]=e[a]);return r};const ba={xs:16,sm:22,md:24,lg:26,xl:30};function Rt(e){var t=e,{label:r,classNames:a,styles:s,className:c,onRemove:p,disabled:u,readOnly:o,size:i,radius:f="sm",variant:g,unstyled:l}=t,w=ga(t,["label","classNames","styles","className","onRemove","disabled","readOnly","size","radius","variant","unstyled"]);const{classes:$,cx:S}=pa({disabled:u,readOnly:o,radius:f},{name:"MultiSelect",classNames:a,styles:s,unstyled:l,size:i,variant:g});return y.createElement("div",ha({className:S($.defaultValue,c)},w),y.createElement("span",{className:$.defaultValueLabel},r),!u&&!o&&y.createElement(Wr,{"aria-hidden":!0,onMouseDown:p,size:ba[i],radius:2,color:"blue",variant:"transparent",iconSize:"70%",className:$.defaultValueRemove,tabIndex:-1,unstyled:l}))}Rt.displayName="@mantine/core/MultiSelect/DefaultValue";function va({data:e,searchable:t,limit:r,searchValue:a,filter:s,value:c,disableSelectedItemFiltering:p}){if(!t&&c.length===0)return e;if(!t){const o=[];for(let i=0;i<e.length;i+=1)(p||!c.some(f=>f===e[i].value&&!e[i].disabled))&&o.push(e[i]);return o}const u=[];for(let o=0;o<e.length&&(s(a,!p&&c.some(i=>i===e[o].value&&!e[o].disabled),e[o])&&u.push(e[o]),!(u.length>=r));o+=1);return u}var ma=Object.defineProperty,ya=Object.defineProperties,xa=Object.getOwnPropertyDescriptors,ft=Object.getOwnPropertySymbols,wa=Object.prototype.hasOwnProperty,_a=Object.prototype.propertyIsEnumerable,ht=(e,t,r)=>t in e?ma(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,Sa=(e,t)=>{for(var r in t||(t={}))wa.call(t,r)&&ht(e,r,t[r]);if(ft)for(var r of ft(t))_a.call(t,r)&&ht(e,r,t[r]);return e},Oa=(e,t)=>ya(e,xa(t)),Pa=A((e,{invalid:t},{size:r})=>({wrapper:{position:"relative"},values:{minHeight:`calc(${L({size:r,sizes:dt})} - ${b(2)})`,display:"flex",alignItems:"center",flexWrap:"wrap",marginLeft:`calc(-${e.spacing.xs} / 2)`,boxSizing:"border-box","&[data-clearable]":{marginRight:L({size:r,sizes:dt})}},value:{margin:`calc(${e.spacing.xs} / 2 - ${b(2)}) calc(${e.spacing.xs} / 2)`},searchInput:Oa(Sa({},e.fn.fontStyles()),{flex:1,minWidth:b(60),backgroundColor:"transparent",border:0,outline:0,fontSize:L({size:r,sizes:e.fontSizes}),padding:0,marginLeft:`calc(${e.spacing.xs} / 2)`,appearance:"none",color:"inherit",maxHeight:L({size:r,sizes:Dt}),"&::placeholder":{opacity:1,color:t?e.colors.red[e.fn.primaryShade()]:e.colorScheme==="dark"?e.colors.dark[3]:e.colors.gray[5]},"&:disabled":{cursor:"not-allowed"}}),searchInputEmpty:{width:"100%"},searchInputInputHidden:{width:0,minWidth:0,height:0,margin:0,overflow:"hidden"},searchInputPointer:{cursor:"pointer","&:disabled":{cursor:"not-allowed"}},input:{cursor:"pointer","&:disabled":{cursor:"not-allowed"}}}));const ja=Pa;var $a=Object.defineProperty,ka=Object.defineProperties,Ca=Object.getOwnPropertyDescriptors,ke=Object.getOwnPropertySymbols,Et=Object.prototype.hasOwnProperty,Vt=Object.prototype.propertyIsEnumerable,gt=(e,t,r)=>t in e?$a(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,le=(e,t)=>{for(var r in t||(t={}))Et.call(t,r)&&gt(e,r,t[r]);if(ke)for(var r of ke(t))Vt.call(t,r)&&gt(e,r,t[r]);return e},bt=(e,t)=>ka(e,Ca(t)),Ia=(e,t)=>{var r={};for(var a in e)Et.call(e,a)&&t.indexOf(a)<0&&(r[a]=e[a]);if(e!=null&&ke)for(var a of ke(e))t.indexOf(a)<0&&Vt.call(e,a)&&(r[a]=e[a]);return r};function Da(e,t,r){return t?!1:r.label.toLowerCase().trim().includes(e.toLowerCase().trim())}function Na(e,t){return!!e&&!t.some(r=>r.value.toLowerCase()===e.toLowerCase())}function vt(e,t){if(!Array.isArray(e))return;if(t.length===0)return[];const r=t.map(a=>typeof a=="object"?a.value:a);return e.filter(a=>r.includes(a))}const Ta={size:"sm",valueComponent:Rt,itemComponent:na,transitionProps:{transition:"fade",duration:0},maxDropdownHeight:220,shadow:"sm",searchable:!1,filter:Da,limit:1/0,clearSearchOnChange:!0,clearable:!1,clearSearchOnBlur:!1,disabled:!1,initiallyOpened:!1,creatable:!1,shouldCreate:Na,switchDirectionOnFlip:!1,zIndex:Ur("popover"),selectOnBlur:!1,positionDependencies:[],dropdownPosition:"flip"},Mt=h.forwardRef((e,t)=>{const r=he("MultiSelect",Ta,e),{className:a,style:s,required:c,label:p,description:u,size:o,error:i,classNames:f,styles:g,wrapperProps:l,value:w,defaultValue:$,data:S,onChange:k,valueComponent:_,itemComponent:O,id:V,transitionProps:D,maxDropdownHeight:re,shadow:me,nothingFound:ae,onFocus:m,onBlur:N,searchable:P,placeholder:Ee,filter:Ve,limit:ye,clearSearchOnChange:Me,clearable:xe,clearSearchOnBlur:ze,variant:ne,onSearchChange:Qt,searchValue:Jt,disabled:W,initiallyOpened:Xt,radius:Qe,icon:er,rightSection:tr,rightSectionWidth:rr,creatable:Je,getCreateLabel:Xe,shouldCreate:ar,onCreate:et,sx:nr,dropdownComponent:or,onDropdownClose:sr,onDropdownOpen:lr,maxSelectedValues:T,withinPortal:ir,switchDirectionOnFlip:cr,zIndex:dr,selectOnBlur:ur,name:pr,dropdownPosition:fr,errorProps:hr,labelProps:gr,descriptionProps:br,form:vr,positionDependencies:mr,onKeyDown:tt,unstyled:ue,inputContainer:yr,inputWrapperOrder:xr,readOnly:Y,withAsterisk:wr,clearButtonProps:_r,hoverOnSearchChange:rt,disableSelectedItemFiltering:Sr}=r,Or=Ia(r,["className","style","required","label","description","size","error","classNames","styles","wrapperProps","value","defaultValue","data","onChange","valueComponent","itemComponent","id","transitionProps","maxDropdownHeight","shadow","nothingFound","onFocus","onBlur","searchable","placeholder","filter","limit","clearSearchOnChange","clearable","clearSearchOnBlur","variant","onSearchChange","searchValue","disabled","initiallyOpened","radius","icon","rightSection","rightSectionWidth","creatable","getCreateLabel","shouldCreate","onCreate","sx","dropdownComponent","onDropdownClose","onDropdownOpen","maxSelectedValues","withinPortal","switchDirectionOnFlip","zIndex","selectOnBlur","name","dropdownPosition","errorProps","labelProps","descriptionProps","form","positionDependencies","onKeyDown","unstyled","inputContainer","inputWrapperOrder","readOnly","withAsterisk","clearButtonProps","hoverOnSearchChange","disableSelectedItemFiltering"]),{classes:H,cx:at,theme:Pr}=ja({invalid:!!i},{name:"MultiSelect",classNames:f,styles:g,unstyled:ue,size:o,variant:ne}),{systemStyles:jr,rest:$r}=Fr(Or),Le=h.useRef(),Be=h.useRef({}),oe=kt(V),[I,C]=h.useState(Xt),[K,U]=h.useState(-1),[nt,kr]=h.useState("column"),[z,we]=He({value:Jt,defaultValue:"",finalValue:void 0,onChange:Qt}),[Cr,ot]=h.useState(!1),{scrollIntoView:_e,targetRef:st,scrollableRef:Ir}=oa({duration:0,offset:5,cancelable:!1,isList:!0}),lt=Je&&typeof Xe=="function";let We=null;const Dr=S.map(d=>typeof d=="string"?{label:d,value:d}:d),Ue=sa({data:Dr}),[x,se]=He({value:vt(w,S),defaultValue:vt($,S),finalValue:[],onChange:k}),M=h.useRef(!!T&&T<x.length),it=d=>{if(!Y){const v=x.filter(R=>R!==d);se(v),T&&v.length<T&&(M.current=!1)}},Nr=d=>{we(d.currentTarget.value),!W&&!M.current&&P&&C(!0)},Tr=d=>{typeof m=="function"&&m(d),!W&&!M.current&&P&&C(!0)},j=va({data:Ue,searchable:P,searchValue:z,limit:ye,filter:Ve,value:x,disableSelectedItemFiltering:Sr}),ct=(d,v,R)=>{let G=d;for(;R(G);)if(G=v(G),!j[G].disabled)return G;return d};Fe(()=>{U(rt&&z?0:-1)},[z,rt]),Fe(()=>{!W&&x.length>S.length&&C(!1),T&&x.length<T&&(M.current=!1),T&&x.length>=T&&(M.current=!0,C(!1))},[x]);const Se=d=>{if(!Y)if(Me&&we(""),x.includes(d.value))it(d.value);else{if(d.creatable&&typeof et=="function"){const v=et(d.value);typeof v<"u"&&v!==null&&se(typeof v=="string"?[...x,v]:[...x,v.value])}else se([...x,d.value]);x.length===T-1&&(M.current=!0,C(!1)),K===j.length-1&&U(j.length-2),j.length===1&&C(!1)}},Rr=d=>{typeof N=="function"&&N(d),ur&&j[K]&&I&&Se(j[K]),ze&&we(""),C(!1)},Er=d=>{if(Cr||(tt==null||tt(d),Y)||d.key!=="Backspace"&&T&&M.current)return;const v=nt==="column",R=()=>{U(Z=>{var F;const pe=ct(Z,Q=>Q+1,Q=>Q<j.length-1);return I&&(st.current=Be.current[(F=j[pe])==null?void 0:F.value],_e({alignment:v?"end":"start"})),pe})},G=()=>{U(Z=>{var F;const pe=ct(Z,Q=>Q-1,Q=>Q>0);return I&&(st.current=Be.current[(F=j[pe])==null?void 0:F.value],_e({alignment:v?"start":"end"})),pe})};switch(d.key){case"ArrowUp":{d.preventDefault(),C(!0),v?G():R();break}case"ArrowDown":{d.preventDefault(),C(!0),v?R():G();break}case"Enter":{d.preventDefault(),j[K]&&I?Se(j[K]):C(!0);break}case" ":{P||(d.preventDefault(),j[K]&&I?Se(j[K]):C(!0));break}case"Backspace":{x.length>0&&z.length===0&&(se(x.slice(0,-1)),C(!0),T&&(M.current=!1));break}case"Home":{if(!P){d.preventDefault(),I||C(!0);const Z=j.findIndex(F=>!F.disabled);U(Z),_e({alignment:v?"end":"start"})}break}case"End":{if(!P){d.preventDefault(),I||C(!0);const Z=j.map(F=>!!F.disabled).lastIndexOf(!1);U(Z),_e({alignment:v?"end":"start"})}break}case"Escape":C(!1)}},Vr=x.map(d=>{let v=Ue.find(R=>R.value===d&&!R.disabled);return!v&&lt&&(v={value:d,label:d}),v}).filter(d=>!!d).map((d,v)=>y.createElement(_,bt(le({},d),{variant:ne,disabled:W,className:H.value,readOnly:Y,onRemove:R=>{R.preventDefault(),R.stopPropagation(),it(d.value)},key:d.value,size:o,styles:g,classNames:f,radius:Qe,index:v}))),Mr=d=>x.includes(d),zr=()=>{var d;we(""),se([]),(d=Le.current)==null||d.focus(),T&&(M.current=!1)};lt&&ar(z,Ue)&&(We=Xe(z),j.push({label:z,value:z,creatable:!0}));const Oe=!Y&&(j.length>0?I:I&&!!ae);return Fe(()=>{const d=Oe?lr:sr;typeof d=="function"&&d()},[Oe]),y.createElement(ce.Wrapper,le(le({required:c,id:oe,label:p,error:i,description:u,size:o,className:a,style:s,classNames:f,styles:g,__staticSelector:"MultiSelect",sx:nr,errorProps:hr,descriptionProps:br,labelProps:gr,inputContainer:yr,inputWrapperOrder:xr,unstyled:ue,withAsterisk:wr,variant:ne},jr),l),y.createElement(Ae,{opened:Oe,transitionProps:D,shadow:"sm",withinPortal:ir,__staticSelector:"MultiSelect",onDirectionChange:kr,switchDirectionOnFlip:cr,zIndex:dr,dropdownPosition:fr,positionDependencies:[...mr,z],classNames:f,styles:g,unstyled:ue,variant:ne},y.createElement(Ae.Target,null,y.createElement("div",{className:H.wrapper,role:"combobox","aria-haspopup":"listbox","aria-owns":I&&Oe?`${oe}-items`:null,"aria-controls":oe,"aria-expanded":I,onMouseLeave:()=>U(-1),tabIndex:-1},y.createElement("input",{type:"hidden",name:pr,value:x.join(","),form:vr,disabled:W}),y.createElement(ce,le({__staticSelector:"MultiSelect",style:{overflow:"hidden"},component:"div",multiline:!0,size:o,variant:ne,disabled:W,error:i,required:c,radius:Qe,icon:er,unstyled:ue,onMouseDown:d=>{var v;d.preventDefault(),!W&&!M.current&&C(!I),(v=Le.current)==null||v.focus()},classNames:bt(le({},f),{input:at({[H.input]:!P},f==null?void 0:f.input)})},la({theme:Pr,rightSection:tr,rightSectionWidth:rr,styles:g,size:o,shouldClear:xe&&x.length>0,onClear:zr,error:i,disabled:W,clearButtonProps:_r,readOnly:Y})),y.createElement("div",{className:H.values,"data-clearable":xe||void 0},Vr,y.createElement("input",le({ref:Ar(t,Le),type:"search",id:oe,className:at(H.searchInput,{[H.searchInputPointer]:!P,[H.searchInputInputHidden]:!I&&x.length>0||!P&&x.length>0,[H.searchInputEmpty]:x.length===0}),onKeyDown:Er,value:z,onChange:Nr,onFocus:Tr,onBlur:Rr,readOnly:!P||M.current||Y,placeholder:x.length===0?Ee:void 0,disabled:W,"data-mantine-stop-propagation":I,autoComplete:"off",onCompositionStart:()=>ot(!0),onCompositionEnd:()=>ot(!1)},$r)))))),y.createElement(Ae.Dropdown,{component:or||ia,maxHeight:re,direction:nt,id:oe,innerRef:Ir,__staticSelector:"MultiSelect",classNames:f,styles:g},y.createElement(ca,{data:j,hovered:K,classNames:f,styles:g,uuid:oe,__staticSelector:"MultiSelect",onItemHover:U,onItemSelect:Se,itemsRefs:Be,itemComponent:O,size:o,nothingFound:ae,isItemSelected:Mr,creatable:Je&&!!We,createLabel:We,unstyled:ue,variant:ne}))))});Mt.displayName="@mantine/core/MultiSelect";const Ge={context:"Tabs component was not found in the tree",value:"Tabs.Tab or Tabs.Panel component was rendered with invalid value or without value"},[Ra,Ze]=Hr(Ge.context);var Ea=Object.defineProperty,mt=Object.getOwnPropertySymbols,Va=Object.prototype.hasOwnProperty,Ma=Object.prototype.propertyIsEnumerable,yt=(e,t,r)=>t in e?Ea(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,za=(e,t)=>{for(var r in t||(t={}))Va.call(t,r)&&yt(e,r,t[r]);if(mt)for(var r of mt(t))Ma.call(t,r)&&yt(e,r,t[r]);return e};function La({orientation:e,inverted:t,placement:r},a,s){const c=e==="vertical";return s==="default"?{[c?r==="left"?"borderRight":"borderLeft":t?"borderTop":"borderBottom"]:`${b(2)} solid ${a.colorScheme==="dark"?a.colors.dark[4]:a.colors.gray[3]}`}:s==="outline"?{[c?r==="left"?"borderRight":"borderLeft":t?"borderTop":"borderBottom"]:`${b(1)} solid ${a.colorScheme==="dark"?a.colors.dark[4]:a.colors.gray[3]}`}:s==="pills"?{gap:`calc(${a.spacing.sm} / 2)`}:{}}var Ba=A((e,t,{variant:r})=>{const a=t.orientation==="vertical";return{tabsList:za({display:"flex",flexWrap:"wrap",flexDirection:a?"column":"row",justifyContent:Kr[t.position],'& [role="tab"]':{flex:t.grow?1:void 0}},La(t,e,r))}});const Wa=Ba;var Ua=Object.defineProperty,Fa=Object.defineProperties,Aa=Object.getOwnPropertyDescriptors,Ce=Object.getOwnPropertySymbols,zt=Object.prototype.hasOwnProperty,Lt=Object.prototype.propertyIsEnumerable,xt=(e,t,r)=>t in e?Ua(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,Ha=(e,t)=>{for(var r in t||(t={}))zt.call(t,r)&&xt(e,r,t[r]);if(Ce)for(var r of Ce(t))Lt.call(t,r)&&xt(e,r,t[r]);return e},Ka=(e,t)=>Fa(e,Aa(t)),Ga=(e,t)=>{var r={};for(var a in e)zt.call(e,a)&&t.indexOf(a)<0&&(r[a]=e[a]);if(e!=null&&Ce)for(var a of Ce(e))t.indexOf(a)<0&&Lt.call(e,a)&&(r[a]=e[a]);return r};const qa={grow:!1,position:"left"},Bt=h.forwardRef((e,t)=>{const r=he("TabsList",qa,e),{children:a,className:s,grow:c,position:p}=r,u=Ga(r,["children","className","grow","position"]),{orientation:o,variant:i,color:f,radius:g,inverted:l,placement:w,classNames:$,styles:S,unstyled:k}=Ze(),{classes:_,cx:O}=Wa({orientation:o,grow:c,color:f,position:p,radius:g,inverted:l,placement:w},{name:"Tabs",unstyled:k,classNames:$,styles:S,variant:i});return y.createElement(fe,Ka(Ha({},u),{className:O(_.tabsList,s),ref:t,role:"tablist","aria-orientation":o}),a)});Bt.displayName="@mantine/core/TabsList";var Ya=A((e,{orientation:t})=>({panel:{flex:t==="vertical"?1:void 0}}));const Za=Ya;var Qa=Object.defineProperty,Ja=Object.defineProperties,Xa=Object.getOwnPropertyDescriptors,Ie=Object.getOwnPropertySymbols,Wt=Object.prototype.hasOwnProperty,Ut=Object.prototype.propertyIsEnumerable,wt=(e,t,r)=>t in e?Qa(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,en=(e,t)=>{for(var r in t||(t={}))Wt.call(t,r)&&wt(e,r,t[r]);if(Ie)for(var r of Ie(t))Ut.call(t,r)&&wt(e,r,t[r]);return e},tn=(e,t)=>Ja(e,Xa(t)),rn=(e,t)=>{var r={};for(var a in e)Wt.call(e,a)&&t.indexOf(a)<0&&(r[a]=e[a]);if(e!=null&&Ie)for(var a of Ie(e))t.indexOf(a)<0&&Ut.call(e,a)&&(r[a]=e[a]);return r};const an={},Ft=h.forwardRef((e,t)=>{const r=he("TabsPanel",an,e),{value:a,children:s,sx:c,className:p}=r,u=rn(r,["value","children","sx","className"]),o=Ze(),{classes:i,cx:f}=Za({orientation:o.orientation,color:o.color,radius:o.radius,inverted:o.inverted,placement:o.placement},{name:"Tabs",unstyled:o.unstyled,classNames:o.classNames,styles:o.styles,variant:o.variant}),g=o.value===a,l=o.keepMounted||g?s:null;return y.createElement(fe,tn(en({},u),{ref:t,sx:[{display:g?void 0:"none"},...Gr(c)],className:f(i.panel,p),role:"tabpanel",id:o.getPanelId(a),"aria-labelledby":o.getTabId(a)}),l)});Ft.displayName="@mantine/core/TabsPanel";var nn=Object.defineProperty,on=Object.defineProperties,sn=Object.getOwnPropertyDescriptors,_t=Object.getOwnPropertySymbols,ln=Object.prototype.hasOwnProperty,cn=Object.prototype.propertyIsEnumerable,St=(e,t,r)=>t in e?nn(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,ie=(e,t)=>{for(var r in t||(t={}))ln.call(t,r)&&St(e,r,t[r]);if(_t)for(var r of _t(t))cn.call(t,r)&&St(e,r,t[r]);return e},Ot=(e,t)=>on(e,sn(t));function dn(e,{orientation:t,color:r,radius:a,inverted:s,placement:c},p){const u=t==="vertical",o=e.fn.variant({color:r,variant:"filled"}),i=b(e.fn.radius(a)),f=t==="vertical"?c==="left"?`${i} 0 0 ${i}`:` 0 ${i} ${i} 0`:s?`0 0 ${i} ${i}`:`${i} ${i} 0 0`;return p==="default"?Ot(ie({[u?c==="left"?"borderRight":"borderLeft":s?"borderTop":"borderBottom"]:`${b(2)} solid transparent`,[u?c==="left"?"marginRight":"marginLeft":s?"marginTop":"marginBottom"]:b(-2),borderRadius:f},e.fn.hover({backgroundColor:e.colorScheme==="dark"?e.colors.dark[6]:e.colors.gray[0],borderColor:e.colorScheme==="dark"?e.colors.dark[4]:e.colors.gray[3]})),{"&[data-active]":ie({borderColor:o.background,color:e.colorScheme==="dark"?e.white:e.black},e.fn.hover({borderColor:o.background}))}):p==="outline"?{borderRadius:f,border:`${b(1)} solid transparent`,[u?c==="left"?"borderRight":"borderLeft":s?"borderTop":"borderBottom"]:"none","&[data-active]":{borderColor:e.colorScheme==="dark"?e.colors.dark[4]:e.colors.gray[3],"&::before":{content:'""',backgroundColor:e.colorScheme==="dark"?e.colors.dark[7]:e.white,position:"absolute",bottom:u?0:s?"unset":b(-1),top:u?0:s?b(-1):"unset",[u?"width":"height"]:b(1),right:u?c==="left"?b(-1):"unset":0,left:u?c==="left"?"unset":b(-1):0}}}:p==="pills"?Ot(ie({borderRadius:e.fn.radius(a)},e.fn.hover({backgroundColor:e.colorScheme==="dark"?e.colors.dark[6]:e.colors.gray[0]})),{"&[data-active]":ie({backgroundColor:o.background,color:e.white},e.fn.hover({backgroundColor:o.background}))}):{}}var un=A((e,t,{variant:r})=>({tabLabel:{},tab:ie({position:"relative",padding:`${e.spacing.xs} ${e.spacing.md}`,paddingLeft:t.withIcon?e.spacing.xs:void 0,paddingRight:t.withRightSection?e.spacing.xs:void 0,fontSize:e.fontSizes.sm,whiteSpace:"nowrap",zIndex:0,display:"flex",alignItems:"center",justifyContent:t.orientation==="horizontal"?"center":void 0,lineHeight:1,"&:disabled":ie({opacity:.5,cursor:"not-allowed"},e.fn.hover({backgroundColor:"transparent"})),"&:focus":{zIndex:1}},dn(e,t,r)),tabRightSection:{display:"flex",justifyContent:"center",alignItems:"center","&:not(:only-child)":{marginLeft:b(7)}},tabIcon:{display:"flex",justifyContent:"center",alignItems:"center","&:not(:only-child)":{marginRight:b(7)}}}));const pn=un;var fn=Object.defineProperty,hn=Object.defineProperties,gn=Object.getOwnPropertyDescriptors,De=Object.getOwnPropertySymbols,At=Object.prototype.hasOwnProperty,Ht=Object.prototype.propertyIsEnumerable,Pt=(e,t,r)=>t in e?fn(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,bn=(e,t)=>{for(var r in t||(t={}))At.call(t,r)&&Pt(e,r,t[r]);if(De)for(var r of De(t))Ht.call(t,r)&&Pt(e,r,t[r]);return e},vn=(e,t)=>hn(e,gn(t)),mn=(e,t)=>{var r={};for(var a in e)At.call(e,a)&&t.indexOf(a)<0&&(r[a]=e[a]);if(e!=null&&De)for(var a of De(e))t.indexOf(a)<0&&Ht.call(e,a)&&(r[a]=e[a]);return r};const yn={},Kt=h.forwardRef((e,t)=>{const r=he("TabsTab",yn,e),{value:a,children:s,onKeyDown:c,onClick:p,className:u,icon:o,rightSection:i,color:f}=r,g=mn(r,["value","children","onKeyDown","onClick","className","icon","rightSection","color"]),l=Ze(),w=!!o,$=!!i,{theme:S,classes:k,cx:_}=pn({withIcon:w||$&&!s,withRightSection:$||w&&!s,orientation:l.orientation,color:f||l.color,radius:l.radius,inverted:l.inverted,placement:l.placement},{name:"Tabs",unstyled:l.unstyled,classNames:l.classNames,styles:l.styles,variant:l.variant}),O=a===l.value,V=D=>{l.onTabChange(l.allowTabDeactivation&&a===l.value?null:a),p==null||p(D)};return y.createElement(qr,vn(bn({},g),{unstyled:l.unstyled,className:_(k.tab,u),"data-active":O||void 0,ref:t,type:"button",role:"tab",id:l.getTabId(a),"aria-selected":O,tabIndex:O||l.value===null?0:-1,"aria-controls":l.getPanelId(a),onClick:V,onKeyDown:Xr({siblingSelector:'[role="tab"]',parentSelector:'[role="tablist"]',activateOnFocus:l.activateTabWithKeyboard,loop:l.loop,dir:S.dir,orientation:l.orientation,onKeyDown:c})}),o&&y.createElement("span",{className:k.tabIcon},o),s&&y.createElement("span",{className:k.tabLabel},s),i&&y.createElement("span",{className:k.tabRightSection},i))});Kt.displayName="@mantine/core/Tab";function Gt({defaultValue:e,value:t,onTabChange:r,orientation:a,children:s,loop:c,id:p,activateTabWithKeyboard:u,allowTabDeactivation:o,variant:i,color:f,radius:g,inverted:l,placement:w,keepMounted:$=!0,classNames:S,styles:k,unstyled:_}){const O=kt(p),[V,D]=He({value:t,defaultValue:e,finalValue:null,onChange:r});return y.createElement(Ra,{value:{placement:w,value:V,orientation:a,id:O,loop:c,activateTabWithKeyboard:u,getTabId:ut(`${O}-tab`,Ge.value),getPanelId:ut(`${O}-panel`,Ge.value),onTabChange:D,allowTabDeactivation:o,variant:i,color:f,radius:g,inverted:l,keepMounted:$,classNames:S,styles:k,unstyled:_}},s)}Gt.displayName="@mantine/core/TabsProvider";var xn=A((e,{orientation:t,placement:r})=>({root:{display:t==="vertical"?"flex":void 0,flexDirection:r==="right"?"row-reverse":"row"}}));const wn=xn;var _n=Object.defineProperty,Sn=Object.defineProperties,On=Object.getOwnPropertyDescriptors,Ne=Object.getOwnPropertySymbols,qt=Object.prototype.hasOwnProperty,Yt=Object.prototype.propertyIsEnumerable,jt=(e,t,r)=>t in e?_n(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,Pn=(e,t)=>{for(var r in t||(t={}))qt.call(t,r)&&jt(e,r,t[r]);if(Ne)for(var r of Ne(t))Yt.call(t,r)&&jt(e,r,t[r]);return e},jn=(e,t)=>Sn(e,On(t)),$n=(e,t)=>{var r={};for(var a in e)qt.call(e,a)&&t.indexOf(a)<0&&(r[a]=e[a]);if(e!=null&&Ne)for(var a of Ne(e))t.indexOf(a)<0&&Yt.call(e,a)&&(r[a]=e[a]);return r};const kn={orientation:"horizontal",loop:!0,activateTabWithKeyboard:!0,allowTabDeactivation:!1,unstyled:!1,inverted:!1,variant:"default",placement:"left"},B=h.forwardRef((e,t)=>{const r=he("Tabs",kn,e),{defaultValue:a,value:s,orientation:c,loop:p,activateTabWithKeyboard:u,allowTabDeactivation:o,children:i,id:f,onTabChange:g,variant:l,color:w,className:$,unstyled:S,classNames:k,styles:_,radius:O,inverted:V,keepMounted:D,placement:re}=r,me=$n(r,["defaultValue","value","orientation","loop","activateTabWithKeyboard","allowTabDeactivation","children","id","onTabChange","variant","color","className","unstyled","classNames","styles","radius","inverted","keepMounted","placement"]),{classes:ae,cx:m}=wn({orientation:c,color:w,radius:O,inverted:V,placement:re},{unstyled:S,name:"Tabs",classNames:k,styles:_,variant:l});return y.createElement(Gt,{activateTabWithKeyboard:u,defaultValue:a,orientation:c,onTabChange:g,value:s,id:f,loop:p,allowTabDeactivation:o,color:w,variant:l,radius:O,inverted:V,keepMounted:D,placement:re,classNames:k,styles:_,unstyled:S},y.createElement(fe,jn(Pn({},me),{className:m(ae.root,$),id:f,ref:t}),i))});B.List=Bt;B.Tab=Kt;B.Panel=Ft;B.displayName="@mantine/core/Tabs";const Cn=qe("Building2",[["path",{d:"M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z",key:"1b4qmf"}],["path",{d:"M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2",key:"i71pzd"}],["path",{d:"M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2",key:"10jefs"}],["path",{d:"M10 6h4",key:"1itunk"}],["path",{d:"M10 10h4",key:"tcdvrf"}],["path",{d:"M10 14h4",key:"kelpxr"}],["path",{d:"M10 18h4",key:"1ulq68"}]]),In=qe("MoreVertical",[["circle",{cx:"12",cy:"12",r:"1",key:"41hilf"}],["circle",{cx:"12",cy:"5",r:"1",key:"gxeob9"}],["circle",{cx:"12",cy:"19",r:"1",key:"lyex9k"}]]),Dn=qe("Users",[["path",{d:"M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2",key:"1yyitq"}],["circle",{cx:"9",cy:"7",r:"4",key:"nufk8"}],["path",{d:"M22 21v-2a4 4 0 0 0-3-3.87",key:"kshegd"}],["path",{d:"M16 3.13a4 4 0 0 1 0 7.75",key:"1da9ce"}]]);class Nn{constructor(){E(this,"state","close");E(this,"name","");E(this,"description","");E(this,"labels",[]);E(this,"reload",!0);E(this,"setReload",t=>{this.reload=t});E(this,"setState",t=>{this.state=t});E(this,"setName",t=>{this.name=t});E(this,"setDescription",t=>{this.description=t});E(this,"setLabels",t=>{this.labels=t});E(this,"clear",()=>{this.name="",this.description="",this.labels=[],this.state="close"});Yr(this)}}const ve=new Nn;function Tn(){return ee.get(te.allProjects)}function Rn(e,t,r){return ee.post(te.project,{name:e,description:t,label_list:r})}function En(e){return ee.delete(`${te.project}/${e}`)}function Vn(){return ee.get(te.orgs)}function Mn(e){return ee.get(`${te.orgUsers}/${e}`)}function $t(e,t){return ee.post(te.projectUsers,{user_id:e,project_id:t})}function zn(){return ee.post(te.statistics,{})}const Ln=Te(({id:e})=>{const{t}=q(),[r,a]=h.useState(!1),{successNotification:s,errorNotification:c}=Ct(),{setReload:p}=ve,u=()=>{En(e).then(()=>{s(t("Проект удалён")),p(!0)}).catch(()=>c(t("Удалить проект не удалось")))};return n.jsxs(n.Fragment,{children:[n.jsxs(Pe,{children:[n.jsx(Pe.Target,{children:n.jsx(Zr,{children:n.jsx(In,{size:16})})}),n.jsx(Pe.Dropdown,{children:n.jsx(Pe.Item,{onClick:()=>a(!0),children:t("Удалить")})})]}),n.jsx(Ye,{opened:r,onClose:()=>a(!1),withCloseButton:!1,centered:!0,children:n.jsxs(de,{children:[n.jsx(J,{children:t("Вы действительно хотите удалить проект?")}),n.jsx(Qr,{saveRights:u,close:()=>a(!1)})]})})]})}),Bn=()=>{const{t:e}=q();return h.useMemo(()=>[{accessorKey:"name",header:e("Проект"),cell:t=>t.getValue()||e("Без названия")},{accessorKey:"description",header:e("Описание"),cell:t=>t.getValue()},{accessorKey:"owner",header:e("Владелец"),cell:t=>t.getValue()==="Admin"?"Администратор":t.getValue()},{accessorKey:"created_at",header:e("Дата создания"),cell:t=>new Date(t.getValue()).toLocaleString("ru",{day:"2-digit",month:"2-digit",year:"2-digit",hour:"2-digit",minute:"2-digit"})},{accessorKey:"id",header:()=>null,cell:({row:t})=>n.jsx(Ln,{id:t.original.id})}],[e])},Wn=e=>{const t=Bn();return{table:ea({data:e,columns:t,getCoreRowModel:ta(),getFilteredRowModel:ra()})}},Un=(e,t)=>{const[r,a]=h.useState([]),[s,c]=h.useState(!0);return h.useEffect(()=>{e&&Tn().then(({data:p})=>a(p)).finally(()=>{c(!1),t(!1)})},[e,t]),{data:r,loading:s}},Zt=A(e=>{const t=e.colorScheme==="dark";return{container:{flex:1,whiteSpace:"nowrap",borderRadius:"10px",position:"static",overflow:"auto","::-webkit-scrollbar":{height:"7px",width:"7px",background:t?"#1C1E26":"white"},"::-webkit-scrollbar:horizontal":{borderRadius:"0 0 0 10px"},"::-webkit-scrollbar:vertical":{borderRadius:"0 10px 0 0"},"::-webkit-scrollbar-corner":{width:"10px",height:"10px",borderRadius:"0 0 10px 0",background:t?"#1C1E26":"white"},"::-webkit-scrollbar-thumb":{backgroundColor:t?e.colors.darkGray[4]:e.colors.darkGray[1],borderRadius:"10px"}},table:{position:"static",backgroundColor:t?"#1C1E26":"white",color:t?e.colors.gray[4]:"black","thead, tbody":{"th, td":{padding:"12px !important",":last-of-type":{borderRight:"none"},":first-of-type":{borderLeft:"none"}}}},tableHead:{position:"sticky",background:t?"#1C1E26":"white",zIndex:1,left:0,top:0,"::after":{content:'""',position:"absolute",left:0,bottom:0,height:".7px",background:t?e.colors.dark[4]:e.colors.gray[4],width:"100%"}},th:{color:`${e.colors.gray[5]} !important`,fontWeight:500}}}),Fn=({headerGroups:e})=>{const{classes:t}=Zt();return n.jsx("thead",{className:t.tableHead,children:e.map(r=>n.jsx("tr",{children:r.headers.map(a=>n.jsx("th",{colSpan:a.colSpan,className:t.th,children:Ke(a.column.columnDef.header,a.getContext())},a.id))},r.id))})},An=({rows:e})=>n.jsx("tbody",{children:e.rows.map(t=>n.jsx("tr",{children:t.getVisibleCells().map(r=>r.column.id.includes("id")?n.jsx("td",{role:"gridcell",style:{display:"flex",justifyContent:"end"},children:Ke(r.column.columnDef.cell,r.getContext())},r.id):n.jsx("td",{role:"gridcell",children:Ke(r.column.columnDef.cell,r.getContext())},r.id))},t.id))}),Hn=Te(()=>{const{reload:e,setReload:t}=ve,{data:r,loading:a}=Un(e,t),{table:s}=Wn(r),{classes:c}=Zt();return h.useEffect(()=>t(!0),[t]),n.jsx(Jr,{visible:a,className:c.container,children:n.jsxs(aa,{className:c.table,children:[n.jsx(Fn,{headerGroups:s.getHeaderGroups()}),n.jsx(An,{rows:s.getRowModel()})]})})}),Kn=A(({colorScheme:e,colors:t})=>({root:{minWidth:"270px","& .mantine-Input-input":{paddingRight:"12px"},"& .mantine-MultiSelect-rightSection":{display:"none"},"& .mantine-MultiSelect-searchInput":{"::placeholder":{color:e==="dark"?t.gray[7]:t.gray[4]}}}})),Gn=({data:e,setData:t,...r})=>{const{classes:a}=Kn(),[s,c]=h.useState(""),p=u=>{u.code==="Enter"&&!e.includes(s)&&s.trim()&&(t([...e,s]),c(""))};return n.jsx(Mt,{creatable:!0,searchable:!0,data:e,value:e,searchValue:s,onKeyDown:p,onChange:u=>t(u),onSearchChange:u=>c(u),className:a.root,...r})},qn=Te(()=>{const{name:e,description:t,setName:r,setDescription:a,labels:s,setLabels:c,setState:p,state:u,clear:o}=ve,{t:i}=q(),{colors:f,colorScheme:g}=ge();return n.jsx(Ye,{centered:!0,withCloseButton:!1,opened:u==="first",onClose:o,children:n.jsxs(de,{spacing:10,children:[n.jsxs(X,{justify:"space-between",children:[n.jsx(J,{fw:500,children:i("О проекте")}),n.jsxs(X,{gap:0,children:[n.jsx(je,{style:{strokeWidth:9},size:16,color:g==="dark"?f.darkBlue[2]:f.blue[5]}),n.jsx(je,{style:{strokeWidth:9},size:16,color:g==="dark"?f.darkGray[5]:f.gray[3]})]})]}),n.jsx(J,{children:i("Название")}),n.jsx(ce,{value:e,onChange:l=>r(l.target.value)}),n.jsx(J,{children:i("Описание")}),n.jsx(ce,{value:t,onChange:l=>a(l.target.value)}),n.jsx(J,{children:i("Классы")}),n.jsx(Gn,{data:s,setData:c,placeholder:i("Введите название класса и нажмите Enter..."),w:400}),n.jsx(be,{onClick:()=>p("second"),disabled:!e||!s.length,w:"fit-content",sx:{alignSelf:"center"},children:i("Продолжить")})]})})}),Re=A(({colorScheme:e,colors:t})=>{const r=e==="dark";return{title:{justifyContent:"space-between",padding:24,fontWeight:500},tabs:{border:`1px solid ${r?t.darkGray[3]:t.gray[3]}`},users:{flex:1,width:"50%",height:500,borderTop:`1px solid ${r?t.darkGray[3]:t.gray[3]}`,borderLeft:`1px solid ${r?t.darkGray[3]:t.gray[3]}`,"&>.mantine-Text-root":{textAlign:"center",borderBottom:`1px solid ${r?t.darkGray[3]:t.gray[3]}`,padding:"6px 0"}},item:{borderBottom:`1px solid ${r?t.darkGray[3]:t.gray[3]}`,padding:"10px 15px",justifyContent:"space-between",alignItems:"center"},button:{position:"absolute",bottom:20,right:20},add:{background:"none",color:t.blue[5],fontWeight:300,fontSize:12,"&:hover":{background:"none",textDecoration:"underline"}},panel:{overflowY:"scroll","::-webkit-scrollbar":{width:"0px"}}}}),Yn=({organizations:e,selected:t,selectOrg:r})=>{const{colors:a,colorScheme:s}=ge(),{classes:c}=Re(),{t:p}=q(),u=s==="dark"?a.darkGray[5]:a.gray[3],[o,i]=h.useState(""),[f,g]=h.useState(e);return h.useEffect(()=>{g(e.filter(l=>l.toLowerCase().startsWith(o.toLowerCase())))},[o,e]),n.jsxs(n.Fragment,{children:[n.jsx(ce,{value:o,onChange:l=>i(l.target.value),icon:n.jsx(It,{size:16}),placeholder:p("Поиск...")}),f.map(l=>n.jsxs(X,{className:c.item,bg:t.includes(l)?u:"none",children:[l,n.jsx(be,{className:c.add,onClick:()=>r(l),children:p(t.includes(l)?"Убрать":"Добавить")})]},l))]})},Zn=({users:e,selected:t,selectUser:r})=>{const{classes:a}=Re(),{colors:s,colorScheme:c}=ge(),{t:p}=q(),u=c==="dark"?s.darkGray[5]:s.gray[3],[o,i]=h.useState(""),[f,g]=h.useState(e);return h.useEffect(()=>{g(e.filter(l=>l.fullname.toLowerCase().startsWith(o.toLowerCase())))},[o,e]),n.jsxs(n.Fragment,{children:[n.jsx(ce,{value:o,onChange:l=>i(l.target.value),icon:n.jsx(It,{size:16}),placeholder:p("Поиск...")}),f.map(l=>n.jsxs(X,{className:a.item,bg:t.includes(l)?u:"none",children:[l.fullname,n.jsx(be,{className:a.add,onClick:()=>r(l),children:p(t.includes(l)?p("Убрать"):p("Добавить"))})]},l.id))]})},Qn=({selectedOrgs:e,organizations:t,selectOrg:r,users:a,selectedUsers:s,selectUser:c})=>{const{classes:p}=Re(),{t:u}=q(),{colors:o}=ge();return n.jsxs(B,{w:"50%",defaultValue:"organizations",children:[n.jsxs(B.List,{className:p.tabs,children:[n.jsx(B.Tab,{value:"organizations",icon:n.jsx(Cn,{size:14,color:o.gray[6]}),children:u("Организации")}),n.jsx(B.Tab,{value:"users",icon:n.jsx(Dn,{size:14,color:o.gray[6]}),children:u("Пользователи")})]}),n.jsx(B.Panel,{h:460,value:"organizations",className:p.panel,children:n.jsx(Yn,{selected:e,organizations:t,selectOrg:r})}),n.jsx(B.Panel,{h:460,value:"users",className:p.panel,children:n.jsx(Zn,{users:a,selected:s,selectUser:c})})]})},Jn=Te(()=>{const{classes:e}=Re(),{state:t,name:r,description:a,labels:s,clear:c,setReload:p}=ve,[u,o]=h.useState([]),[i,f]=h.useState([]),[g,l]=h.useState([]),[w,$]=h.useState([]),{successNotification:S,errorNotification:k}=Ct(),{t:_}=q(),{colors:O,colorScheme:V}=ge(),D=()=>{$([]),f([]),c()},re=()=>{const m=w.map(P=>P.id),N=s.map(P=>({label:P}));Rn(r,a,N).then(({data:P})=>{i.length?i.forEach(Ee=>{Mn(Ee).then(({data:Ve})=>{const ye=[...Ve,...m],Me=ye.filter((xe,ze)=>ye.indexOf(xe)===ze);$t(Me,[P]).then(()=>{S(_("Проект создан")),p(!0),D()})}).catch(()=>k(_("Не удалось создать проект")))}):w.length?$t(m,[P]).then(()=>{S(_("Проект создан")),p(!0),D()}).catch(()=>k(_("Не удалось создать проект"))):(S(_("Проект создан")),p(!0),D())}).catch(()=>k(_("Не удалось создать проект")))},me=m=>{f(i.includes(m)?i.filter(N=>N!==m):[...i,m])},ae=m=>{$(w.includes(m)?w.filter(N=>N!==m):[...w,m])};return h.useEffect(()=>{Vn().then(({data:m})=>o(m)),zn().then(({data:m})=>l(m.map(({id:N,fullname:P})=>({id:N,fullname:P}))))},[]),n.jsxs(Ye,{withCloseButton:!1,opened:t==="second",onClose:D,centered:!0,padding:0,size:800,children:[n.jsxs(X,{className:e.title,children:[n.jsx(J,{children:_("Выберите пользователей")}),n.jsxs(X,{gap:0,children:[n.jsx(je,{style:{strokeWidth:9},size:16,color:V==="dark"?O.darkGray[5]:O.gray[3]}),n.jsx(je,{style:{strokeWidth:9},size:16,color:V==="dark"?O.darkBlue[2]:O.blue[5]})]})]}),n.jsxs(X,{w:"100%",children:[n.jsx(Qn,{users:g,organizations:u,selectOrg:me,selectUser:ae,selectedOrgs:i,selectedUsers:w}),n.jsxs(de,{className:e.users,spacing:0,children:[n.jsx(J,{children:_("Пользователи проекта")}),n.jsxs(de,{className:e.panel,h:390,children:[i.map(m=>n.jsxs(fe,{className:e.item,children:["Пользователи из ",m]},m)),w.map(({id:m,fullname:N})=>n.jsx(fe,{className:e.item,children:N},m))]}),n.jsx(be,{className:e.button,onClick:re,children:_("Создать проект")})]})]})]})}),Xn=()=>{const{setState:e}=ve,{t}=q();return n.jsxs(de,{h:"90vh",py:"30px",children:[n.jsx(be,{onClick:()=>e("first"),w:"fit-content",children:t("Создать проект")}),n.jsx(Hn,{}),n.jsx(qn,{}),n.jsx(Jn,{})]})},so=()=>n.jsx(de,{children:n.jsx(Xn,{})});export{so as default};
