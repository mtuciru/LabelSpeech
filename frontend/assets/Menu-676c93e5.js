import{r as v,a7 as xe,f as C,x as I,g as P,R as m,B as Y,a5 as De,ac as Ie,T as Me,ad as Ee,D as Se,a4 as Ne}from"./index-14422766.js";import{P as H}from"./Popover-344254a7.js";function M(e,r){let o=e;for(;(o=o.parentElement)&&!o.matches(r););return o}function ke(e,r,o){for(let t=e-1;t>=0;t-=1)if(!r[t].disabled)return t;if(o){for(let t=r.length-1;t>-1;t-=1)if(!r[t].disabled)return t}return e}function je(e,r,o){for(let t=e+1;t<r.length;t+=1)if(!r[t].disabled)return t;if(o){for(let t=0;t<r.length;t+=1)if(!r[t].disabled)return t}return e}function Re(e,r,o){return M(e,o)===M(r,o)}function Ce({parentSelector:e,siblingSelector:r,onKeyDown:o,loop:t=!0,activateOnFocus:c=!1,dir:d="rtl",orientation:a}){return n=>{var f;o==null||o(n);const s=Array.from(((f=M(n.currentTarget,e))==null?void 0:f.querySelectorAll(r))||[]).filter(p=>Re(n.currentTarget,p,e)),l=s.findIndex(p=>n.currentTarget===p),i=je(l,s,t),g=ke(l,s,t),w=d==="rtl"?g:i,u=d==="rtl"?i:g;switch(n.key){case"ArrowRight":{a==="horizontal"&&(n.stopPropagation(),n.preventDefault(),s[w].focus(),c&&s[w].click());break}case"ArrowLeft":{a==="horizontal"&&(n.stopPropagation(),n.preventDefault(),s[u].focus(),c&&s[u].click());break}case"ArrowUp":{a==="vertical"&&(n.stopPropagation(),n.preventDefault(),s[g].focus(),c&&s[g].click());break}case"ArrowDown":{a==="vertical"&&(n.stopPropagation(),n.preventDefault(),s[i].focus(),c&&s[i].click());break}case"Home":{n.stopPropagation(),n.preventDefault(),!s[0].disabled&&s[0].focus();break}case"End":{n.stopPropagation(),n.preventDefault();const p=s.length-1;!s[p].disabled&&s[p].focus();break}}}}function Te(e,r,o){var t;return o?Array.from(((t=M(o,r))==null?void 0:t.querySelectorAll(e))||[]).findIndex(c=>c===o):null}function _(e,r){return o=>{e==null||e(o),r==null||r(o)}}function Le(){const[e,r]=v.useState(-1);return[e,{setHovered:r,resetHovered:()=>r(-1)}]}function Ae({open:e,close:r,openDelay:o,closeDelay:t}){const c=v.useRef(-1),d=v.useRef(-1),a=()=>{window.clearTimeout(c.current),window.clearTimeout(d.current)},n=()=>{a(),o===0?e():c.current=window.setTimeout(e,o)},f=()=>{a(),t===0?r():d.current=window.setTimeout(r,t)};return v.useEffect(()=>a,[]),{openDropdown:n,closeDropdown:f}}const Z={context:"Menu component was not found in the tree",children:"Menu.Target component children should be an element or a component that accepts ref. Fragments, strings, numbers and other primitive values are not supported"},[He,$]=xe(Z.context);var Ve=C(e=>({divider:{marginTop:I(4),marginBottom:I(4),borderTop:`${I(1)} solid ${e.colorScheme==="dark"?e.colors.dark[4]:e.colors.gray[2]}`}}));const ze=Ve;var Ke=Object.defineProperty,E=Object.getOwnPropertySymbols,ee=Object.prototype.hasOwnProperty,re=Object.prototype.propertyIsEnumerable,K=(e,r,o)=>r in e?Ke(e,r,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[r]=o,Ue=(e,r)=>{for(var o in r||(r={}))ee.call(r,o)&&K(e,o,r[o]);if(E)for(var o of E(r))re.call(r,o)&&K(e,o,r[o]);return e},Fe=(e,r)=>{var o={};for(var t in e)ee.call(e,t)&&r.indexOf(t)<0&&(o[t]=e[t]);if(e!=null&&E)for(var t of E(e))r.indexOf(t)<0&&re.call(e,t)&&(o[t]=e[t]);return o};const qe={},oe=v.forwardRef((e,r)=>{const o=P("MenuDivider",qe,e),{children:t,className:c}=o,d=Fe(o,["children","className"]),{classNames:a,styles:n,unstyled:f,variant:s}=$(),{classes:l,cx:i}=ze(null,{name:"Menu",classNames:a,styles:n,unstyled:f,variant:s});return m.createElement(Y,Ue({className:i(l.divider,c),ref:r},d))});oe.displayName="@mantine/core/MenuDivider";var Be=Object.defineProperty,S=Object.getOwnPropertySymbols,te=Object.prototype.hasOwnProperty,ne=Object.prototype.propertyIsEnumerable,U=(e,r,o)=>r in e?Be(e,r,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[r]=o,We=(e,r)=>{for(var o in r||(r={}))te.call(r,o)&&U(e,o,r[o]);if(S)for(var o of S(r))ne.call(r,o)&&U(e,o,r[o]);return e},Ge=(e,r)=>{var o={};for(var t in e)te.call(e,t)&&r.indexOf(t)<0&&(o[t]=e[t]);if(e!=null&&S)for(var t of S(e))r.indexOf(t)<0&&ne.call(e,t)&&(o[t]=e[t]);return o};const Je={};function ae(e){const r=P("MenuDropdown",Je,e),{children:o,onMouseEnter:t,onMouseLeave:c}=r,d=Ge(r,["children","onMouseEnter","onMouseLeave"]),a=v.useRef(),n=$(),f=i=>{(i.key==="ArrowUp"||i.key==="ArrowDown")&&(i.preventDefault(),a.current.querySelectorAll("[data-menu-item]")[0].focus())},s=_(t,()=>n.trigger==="hover"&&n.openDropdown()),l=_(c,()=>n.trigger==="hover"&&n.closeDropdown());return m.createElement(H.Dropdown,We({onMouseEnter:s,onMouseLeave:l,role:"menu","aria-orientation":"vertical"},d),m.createElement("div",{tabIndex:-1,"data-menu-dropdown":!0,"data-autofocus":!0,onKeyDown:f,ref:a,style:{outline:0}},o))}ae.displayName="@mantine/core/MenuDropdown";var Qe=Object.defineProperty,Xe=Object.defineProperties,Ye=Object.getOwnPropertyDescriptors,F=Object.getOwnPropertySymbols,Ze=Object.prototype.hasOwnProperty,er=Object.prototype.propertyIsEnumerable,q=(e,r,o)=>r in e?Qe(e,r,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[r]=o,rr=(e,r)=>{for(var o in r||(r={}))Ze.call(r,o)&&q(e,o,r[o]);if(F)for(var o of F(r))er.call(r,o)&&q(e,o,r[o]);return e},or=(e,r)=>Xe(e,Ye(r)),tr=C((e,{color:r,radius:o})=>({item:or(rr({},e.fn.fontStyles()),{WebkitTapHighlightColor:"transparent",fontSize:e.fontSizes.sm,border:0,backgroundColor:"transparent",outline:0,width:"100%",textAlign:"left",textDecoration:"none",boxSizing:"border-box",padding:`${e.spacing.xs} ${e.spacing.sm}`,cursor:"pointer",borderRadius:e.fn.radius(o),color:r?e.fn.variant({variant:"filled",primaryFallback:!1,color:r}).background:e.colorScheme==="dark"?e.colors.dark[0]:e.black,display:"flex",alignItems:"center","&:disabled":{color:e.colorScheme==="dark"?e.colors.dark[3]:e.colors.gray[5],pointerEvents:"none",userSelect:"none"},"&[data-hovered]":{backgroundColor:r?e.fn.variant({variant:"light",color:r}).background:e.colorScheme==="dark"?e.fn.rgba(e.colors.dark[3],.35):e.colors.gray[1]}}),itemLabel:{flex:1},itemIcon:{display:"flex",justifyContent:"center",alignItems:"center",marginRight:e.spacing.xs},itemRightSection:{}}));const nr=tr;var ar=Object.defineProperty,sr=Object.defineProperties,lr=Object.getOwnPropertyDescriptors,N=Object.getOwnPropertySymbols,se=Object.prototype.hasOwnProperty,le=Object.prototype.propertyIsEnumerable,B=(e,r,o)=>r in e?ar(e,r,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[r]=o,ir=(e,r)=>{for(var o in r||(r={}))se.call(r,o)&&B(e,o,r[o]);if(N)for(var o of N(r))le.call(r,o)&&B(e,o,r[o]);return e},cr=(e,r)=>sr(e,lr(r)),dr=(e,r)=>{var o={};for(var t in e)se.call(e,t)&&r.indexOf(t)<0&&(o[t]=e[t]);if(e!=null&&N)for(var t of N(e))r.indexOf(t)<0&&le.call(e,t)&&(o[t]=e[t]);return o};const fr={},ie=v.forwardRef((e,r)=>{const o=P("MenuItem",fr,e),{children:t,className:c,color:d,closeMenuOnClick:a,icon:n,rightSection:f}=o,s=dr(o,["children","className","color","closeMenuOnClick","icon","rightSection"]),l=$(),{classes:i,cx:g,theme:w}=nr({radius:l.radius,color:d},{name:"Menu",classNames:l.classNames,styles:l.styles,unstyled:l.unstyled,variant:l.variant}),u=v.useRef(),p=l.getItemIndex(u.current),y=s,h=_(y.onMouseLeave,()=>l.setHovered(-1)),x=_(y.onMouseEnter,()=>l.setHovered(l.getItemIndex(u.current))),T=_(y.onClick,()=>{typeof a=="boolean"?a&&l.closeDropdownImmediately():l.closeOnItemClick&&l.closeDropdownImmediately()}),L=_(y.onFocus,()=>l.setHovered(l.getItemIndex(u.current)));return m.createElement(Y,cr(ir({component:"button",type:"button"},s),{tabIndex:-1,onFocus:L,className:g(i.item,c),ref:De(u,r),role:"menuitem","data-menu-item":!0,"data-hovered":l.hovered===p?!0:void 0,onMouseEnter:x,onMouseLeave:h,onClick:T,onKeyDown:Ce({siblingSelector:"[data-menu-item]",parentSelector:"[data-menu-dropdown]",activateOnFocus:!1,loop:l.loop,dir:w.dir,orientation:"vertical",onKeyDown:y.onKeydown})}),n&&m.createElement("div",{className:i.itemIcon},n),t&&m.createElement("div",{className:i.itemLabel},t),f&&m.createElement("div",{className:i.itemRightSection},f))});ie.displayName="@mantine/core/MenuItem";const ur=Ie(ie);var pr=C(e=>({label:{color:e.colorScheme==="dark"?e.colors.dark[2]:e.colors.gray[6],fontWeight:500,fontSize:e.fontSizes.xs,padding:`calc(${e.spacing.xs} / 2) ${e.spacing.sm}`,cursor:"default"}}));const mr=pr;var vr=Object.defineProperty,k=Object.getOwnPropertySymbols,ce=Object.prototype.hasOwnProperty,de=Object.prototype.propertyIsEnumerable,W=(e,r,o)=>r in e?vr(e,r,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[r]=o,_r=(e,r)=>{for(var o in r||(r={}))ce.call(r,o)&&W(e,o,r[o]);if(k)for(var o of k(r))de.call(r,o)&&W(e,o,r[o]);return e},gr=(e,r)=>{var o={};for(var t in e)ce.call(e,t)&&r.indexOf(t)<0&&(o[t]=e[t]);if(e!=null&&k)for(var t of k(e))r.indexOf(t)<0&&de.call(e,t)&&(o[t]=e[t]);return o};const yr={},fe=v.forwardRef((e,r)=>{const o=P("MenuLabel",yr,e),{children:t,className:c}=o,d=gr(o,["children","className"]),{classNames:a,styles:n,unstyled:f,variant:s}=$(),{classes:l,cx:i}=mr(null,{name:"Menu",classNames:a,styles:n,unstyled:f,variant:s});return m.createElement(Me,_r({className:i(l.label,c),ref:r},d),t)});fe.displayName="@mantine/core/MenuLabel";var wr=Object.defineProperty,j=Object.getOwnPropertySymbols,ue=Object.prototype.hasOwnProperty,pe=Object.prototype.propertyIsEnumerable,G=(e,r,o)=>r in e?wr(e,r,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[r]=o,Or=(e,r)=>{for(var o in r||(r={}))ue.call(r,o)&&G(e,o,r[o]);if(j)for(var o of j(r))pe.call(r,o)&&G(e,o,r[o]);return e},Pr=(e,r)=>{var o={};for(var t in e)ue.call(e,t)&&r.indexOf(t)<0&&(o[t]=e[t]);if(e!=null&&j)for(var t of j(e))r.indexOf(t)<0&&pe.call(e,t)&&(o[t]=e[t]);return o};const br={refProp:"ref"},me=v.forwardRef((e,r)=>{const o=P("MenuTarget",br,e),{children:t,refProp:c}=o,d=Pr(o,["children","refProp"]);if(!Ee(t))throw new Error(Z.children);const a=$(),n=_(t.props.onClick,()=>a.trigger==="click"&&a.toggleDropdown()),f=_(t.props.onMouseEnter,()=>a.trigger==="hover"&&a.openDropdown()),s=_(t.props.onMouseLeave,()=>a.trigger==="hover"&&a.closeDropdown());return m.createElement(H.Target,Or({refProp:c,popupType:"menu",ref:r},d),v.cloneElement(t,{onClick:n,onMouseEnter:f,onMouseLeave:s,"data-expanded":a.opened?!0:void 0}))});me.displayName="@mantine/core/MenuTarget";var $r=C({dropdown:{padding:I(4)}});const hr=$r;var xr=Object.defineProperty,Dr=Object.defineProperties,Ir=Object.getOwnPropertyDescriptors,R=Object.getOwnPropertySymbols,ve=Object.prototype.hasOwnProperty,_e=Object.prototype.propertyIsEnumerable,J=(e,r,o)=>r in e?xr(e,r,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[r]=o,Q=(e,r)=>{for(var o in r||(r={}))ve.call(r,o)&&J(e,o,r[o]);if(R)for(var o of R(r))_e.call(r,o)&&J(e,o,r[o]);return e},X=(e,r)=>Dr(e,Ir(r)),Mr=(e,r)=>{var o={};for(var t in e)ve.call(e,t)&&r.indexOf(t)<0&&(o[t]=e[t]);if(e!=null&&R)for(var t of R(e))r.indexOf(t)<0&&_e.call(e,t)&&(o[t]=e[t]);return o};const Er={closeOnItemClick:!0,loop:!0,trigger:"click",openDelay:0,closeDelay:100};function b(e){const r=P("Menu",Er,e),{children:o,onOpen:t,onClose:c,opened:d,defaultOpened:a,onChange:n,closeOnItemClick:f,loop:s,closeOnEscape:l,trigger:i,openDelay:g,closeDelay:w,classNames:u,styles:p,unstyled:y,radius:h,variant:x}=r,T=Mr(r,["children","onOpen","onClose","opened","defaultOpened","onChange","closeOnItemClick","loop","closeOnEscape","trigger","openDelay","closeDelay","classNames","styles","unstyled","radius","variant"]),{classes:L,cx:ge}=hr(),[ye,{setHovered:we,resetHovered:Oe}]=Le(),[O,V]=Se({value:d,defaultValue:a,finalValue:!1,onChange:n}),D=()=>{V(!1),O&&(c==null||c())},A=()=>{V(!0),!O&&(t==null||t())},z=()=>O?D():A(),{openDropdown:Pe,closeDropdown:be}=Ae({open:A,close:D,closeDelay:w,openDelay:g}),$e=he=>Te("[data-menu-item]","[data-menu-dropdown]",he);return Ne(()=>{Oe()},[O]),m.createElement(He,{value:{opened:O,toggleDropdown:z,getItemIndex:$e,hovered:ye,setHovered:we,closeOnItemClick:f,closeDropdown:i==="click"?D:be,openDropdown:i==="click"?A:Pe,closeDropdownImmediately:D,loop:s,trigger:i,radius:h,classNames:u,styles:p,unstyled:y,variant:x}},m.createElement(H,X(Q({},T),{radius:h,opened:O,onChange:z,defaultOpened:a,trapFocus:i==="click",closeOnEscape:l&&i==="click",__staticSelector:"Menu",classNames:X(Q({},u),{dropdown:ge(L.dropdown,u==null?void 0:u.dropdown)}),styles:p,unstyled:y,variant:x}),o))}b.displayName="@mantine/core/Menu";b.Item=ur;b.Label=fe;b.Dropdown=ae;b.Target=me;b.Divider=oe;export{b as M,Ce as c};