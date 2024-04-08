import{f as at,a3 as lt,r as g,D as ue,a4 as de,R as D,I as fe,a5 as rt}from"./index-14422766.js";import{D as ot,u as st,g as it,S as G,a as ct,b as ut,c as dt}from"./get-select-right-section-props-739d3de5.js";import{u as ft}from"./use-input-props-561b2f2e.js";function pt({data:t,searchable:a,limit:l,searchValue:r,filter:x,value:B,filterDataOnExactSearchMatch:$}){if(!a)return t;const C=B!=null&&t.find(d=>d.value===B)||null;if(C&&!$&&(C==null?void 0:C.label)===r){if(l){if(l>=t.length)return t;const d=t.indexOf(C),L=d+l,E=L-t.length;return E>0?t.slice(d-E):t.slice(d,L)}return t}const P=[];for(let d=0;d<t.length&&(x(r,t[d])&&P.push(t[d]),!(P.length>=l));d+=1);return P}var ht=at(()=>({input:{"&:not(:disabled)":{cursor:"pointer","&::selection":{backgroundColor:"transparent"}}}}));const mt=ht;var vt=Object.defineProperty,wt=Object.defineProperties,bt=Object.getOwnPropertyDescriptors,j=Object.getOwnPropertySymbols,he=Object.prototype.hasOwnProperty,me=Object.prototype.propertyIsEnumerable,pe=(t,a,l)=>a in t?vt(t,a,{enumerable:!0,configurable:!0,writable:!0,value:l}):t[a]=l,F=(t,a)=>{for(var l in a||(a={}))he.call(a,l)&&pe(t,l,a[l]);if(j)for(var l of j(a))me.call(a,l)&&pe(t,l,a[l]);return t},J=(t,a)=>wt(t,bt(a)),gt=(t,a)=>{var l={};for(var r in t)he.call(t,r)&&a.indexOf(r)<0&&(l[r]=t[r]);if(t!=null&&j)for(var r of j(t))a.indexOf(r)<0&&me.call(t,r)&&(l[r]=t[r]);return l};function Dt(t,a){return a.label.toLowerCase().trim().includes(t.toLowerCase().trim())}function St(t,a){return!!t&&!a.some(l=>l.label.toLowerCase()===t.toLowerCase())}const It={required:!1,size:"sm",shadow:"sm",itemComponent:ot,transitionProps:{transition:"fade",duration:0},initiallyOpened:!1,filter:Dt,maxDropdownHeight:220,searchable:!1,clearable:!1,limit:1/0,disabled:!1,creatable:!1,shouldCreate:St,selectOnBlur:!1,switchDirectionOnFlip:!1,filterDataOnExactSearchMatch:!1,zIndex:lt("popover"),positionDependencies:[],dropdownPosition:"flip"},Ot=g.forwardRef((t,a)=>{const l=ft("Select",It,t),{inputProps:r,wrapperProps:x,shadow:B,data:$,value:C,defaultValue:P,onChange:d,itemComponent:L,onKeyDown:E,onBlur:Q,onFocus:X,transitionProps:ve,initiallyOpened:we,unstyled:Y,classNames:_,styles:k,filter:be,maxDropdownHeight:ge,searchable:m,clearable:K,nothingFound:ee,limit:De,disabled:T,onSearchChange:A,searchValue:Se,rightSection:Ie,rightSectionWidth:Oe,creatable:Ce,getCreateLabel:te,shouldCreate:_e,selectOnBlur:ye,onCreate:ne,dropdownComponent:xe,onDropdownClose:Pe,onDropdownOpen:Ee,withinPortal:Ve,portalProps:Re,switchDirectionOnFlip:Fe,zIndex:Be,name:Le,dropdownPosition:ke,allowDeselect:ae,placeholder:ze,filterDataOnExactSearchMatch:He,form:Ne,positionDependencies:Me,readOnly:S,clearButtonProps:je,hoverOnSearchChange:le}=l,$e=gt(l,["inputProps","wrapperProps","shadow","data","value","defaultValue","onChange","itemComponent","onKeyDown","onBlur","onFocus","transitionProps","initiallyOpened","unstyled","classNames","styles","filter","maxDropdownHeight","searchable","clearable","nothingFound","limit","disabled","onSearchChange","searchValue","rightSection","rightSectionWidth","creatable","getCreateLabel","shouldCreate","selectOnBlur","onCreate","dropdownComponent","onDropdownClose","onDropdownOpen","withinPortal","portalProps","switchDirectionOnFlip","zIndex","name","dropdownPosition","allowDeselect","placeholder","filterDataOnExactSearchMatch","form","positionDependencies","readOnly","clearButtonProps","hoverOnSearchChange"]),{classes:Ke,cx:Te,theme:Ae}=mt(),[i,Ue]=g.useState(we),[v,s]=g.useState(-1),U=g.useRef(),z=g.useRef({}),[re,We]=g.useState("column"),I=re==="column",{scrollIntoView:V,targetRef:W,scrollableRef:Ze}=st({duration:0,offset:5,cancelable:!1,isList:!0}),qe=ae===void 0?K:ae,f=e=>{if(i!==e){Ue(e);const n=e?Ee:Pe;typeof n=="function"&&n()}},Z=Ce&&typeof te=="function";let q=null;const Ge=$.map(e=>typeof e=="string"?{label:e,value:e}:e),H=it({data:Ge}),[p,y,oe]=ue({value:C,defaultValue:P,finalValue:null,onChange:d}),w=H.find(e=>e.value===p),[b,Je]=ue({value:Se,defaultValue:(w==null?void 0:w.label)||"",finalValue:void 0,onChange:A}),O=e=>{Je(e),m&&typeof A=="function"&&A(e)},Qe=()=>{var e;S||(y(null),oe||O(""),(e=U.current)==null||e.focus())};g.useEffect(()=>{const e=H.find(n=>n.value===p);e?O(e.label):(!Z||!p)&&O("")},[p]),g.useEffect(()=>{w&&(!m||!i)&&O(w.label)},[w==null?void 0:w.label]);const N=e=>{if(!S)if(qe&&(w==null?void 0:w.value)===e.value)y(null),f(!1);else{if(e.creatable&&typeof ne=="function"){const n=ne(e.value);typeof n<"u"&&n!==null&&y(typeof n=="string"?n:n.value)}else y(e.value);oe||O(e.label),s(-1),f(!1),U.current.focus()}},o=pt({data:H,searchable:m,limit:De,searchValue:b,filter:be,filterDataOnExactSearchMatch:He,value:p});Z&&_e(b,o)&&(q=te(b),o.push({label:b,value:b,creatable:!0}));const se=(e,n,c)=>{let u=e;for(;c(u);)if(u=n(u),!o[u].disabled)return u;return e};de(()=>{s(le&&b?0:-1)},[b,le]);const R=p?o.findIndex(e=>e.value===p):0,h=!S&&(o.length>0?i:i&&!!ee),ie=()=>{s(e=>{var n;const c=se(e,u=>u-1,u=>u>0);return W.current=z.current[(n=o[c])==null?void 0:n.value],h&&V({alignment:I?"start":"end"}),c})},ce=()=>{s(e=>{var n;const c=se(e,u=>u+1,u=>u<o.length-1);return W.current=z.current[(n=o[c])==null?void 0:n.value],h&&V({alignment:I?"end":"start"}),c})},M=()=>window.setTimeout(()=>{var e;W.current=z.current[(e=o[R])==null?void 0:e.value],V({alignment:I?"end":"start"})},0);de(()=>{h&&M()},[h]);const Xe=e=>{switch(typeof E=="function"&&E(e),e.key){case"ArrowUp":{e.preventDefault(),i?I?ie():ce():(s(R),f(!0),M());break}case"ArrowDown":{e.preventDefault(),i?I?ce():ie():(s(R),f(!0),M());break}case"Home":{if(!m){e.preventDefault(),i||f(!0);const n=o.findIndex(c=>!c.disabled);s(n),h&&V({alignment:I?"end":"start"})}break}case"End":{if(!m){e.preventDefault(),i||f(!0);const n=o.map(c=>!!c.disabled).lastIndexOf(!1);s(n),h&&V({alignment:I?"end":"start"})}break}case"Escape":{e.preventDefault(),f(!1),s(-1);break}case" ":{m||(e.preventDefault(),o[v]&&i?N(o[v]):(f(!0),s(R),M()));break}case"Enter":m||e.preventDefault(),o[v]&&i&&(e.preventDefault(),N(o[v]))}},Ye=e=>{typeof Q=="function"&&Q(e);const n=H.find(c=>c.value===p);ye&&o[v]&&i&&N(o[v]),O((n==null?void 0:n.label)||""),f(!1)},et=e=>{typeof X=="function"&&X(e),m&&f(!0)},tt=e=>{S||(O(e.currentTarget.value),K&&e.currentTarget.value===""&&y(null),s(-1),f(!0))},nt=()=>{S||(f(!i),p&&!i&&s(R))};return D.createElement(fe.Wrapper,J(F({},x),{__staticSelector:"Select"}),D.createElement(G,{opened:h,transitionProps:ve,shadow:B,withinPortal:Ve,portalProps:Re,__staticSelector:"Select",onDirectionChange:We,switchDirectionOnFlip:Fe,zIndex:Be,dropdownPosition:ke,positionDependencies:[...Me,b],classNames:_,styles:k,unstyled:Y,variant:r.variant},D.createElement(G.Target,null,D.createElement("div",{role:"combobox","aria-haspopup":"listbox","aria-owns":h?`${r.id}-items`:null,"aria-controls":r.id,"aria-expanded":h,onMouseLeave:()=>s(-1),tabIndex:-1},D.createElement("input",{type:"hidden",name:Le,value:p||"",form:Ne,disabled:T}),D.createElement(fe,F(J(F(F({autoComplete:"off",type:"search"},r),$e),{ref:rt(a,U),onKeyDown:Xe,__staticSelector:"Select",value:b,placeholder:ze,onChange:tt,"aria-autocomplete":"list","aria-controls":h?`${r.id}-items`:null,"aria-activedescendant":v>=0?`${r.id}-${v}`:null,onMouseDown:nt,onBlur:Ye,onFocus:et,readOnly:!m||S,disabled:T,"data-mantine-stop-propagation":h,name:null,classNames:J(F({},_),{input:Te({[Ke.input]:!m},_==null?void 0:_.input)})}),ct({theme:Ae,rightSection:Ie,rightSectionWidth:Oe,styles:k,size:r.size,shouldClear:K&&!!w,onClear:Qe,error:x.error,clearButtonProps:je,disabled:T,readOnly:S}))))),D.createElement(G.Dropdown,{component:xe||ut,maxHeight:ge,direction:re,id:r.id,innerRef:Ze,__staticSelector:"Select",classNames:_,styles:k},D.createElement(dt,{data:o,hovered:v,classNames:_,styles:k,isItemSelected:e=>e===p,uuid:r.id,__staticSelector:"Select",onItemHover:s,onItemSelect:N,itemsRefs:z,itemComponent:L,size:r.size,nothingFound:ee,creatable:Z&&!!q,createLabel:q,"aria-label":x.label,unstyled:Y,variant:r.variant}))))});Ot.displayName="@mantine/core/Select";export{Ot as S};