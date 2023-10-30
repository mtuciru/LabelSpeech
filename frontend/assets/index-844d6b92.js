import{c as S,h as w,r as j,d as b,R as $,T as d,s as z,j as o,F as E,z as T,L as N,S as F}from"./index-ddf9c13f.js";var R=Object.defineProperty,k=Object.defineProperties,B=Object.getOwnPropertyDescriptors,l=Object.getOwnPropertySymbols,H=Object.prototype.hasOwnProperty,I=Object.prototype.propertyIsEnumerable,f=(e,r,t)=>r in e?R(e,r,{enumerable:!0,configurable:!0,writable:!0,value:t}):e[r]=t,D=(e,r)=>{for(var t in r||(r={}))H.call(r,t)&&f(e,t,r[t]);if(l)for(var t of l(r))I.call(r,t)&&f(e,t,r[t]);return e},L=(e,r)=>k(e,B(r));function W(e,r,t){return typeof e<"u"?e in t.headings.sizes?t.headings.sizes[e].fontSize:w(e):t.headings.sizes[r].fontSize}function V(e,r,t){return typeof e<"u"&&e in t.headings.sizes?t.headings.sizes[e].lineHeight:t.headings.sizes[r].lineHeight}var C=S((e,{element:r,weight:t,inline:n},{size:a})=>({root:L(D({},e.fn.fontStyles()),{fontFamily:e.headings.fontFamily,fontWeight:t||e.headings.sizes[r].fontWeight||e.headings.fontWeight,fontSize:W(a,r,e),lineHeight:n?1:V(a,r,e),margin:0})}));const M=C;var q=Object.defineProperty,s=Object.getOwnPropertySymbols,p=Object.prototype.hasOwnProperty,u=Object.prototype.propertyIsEnumerable,c=(e,r,t)=>r in e?q(e,r,{enumerable:!0,configurable:!0,writable:!0,value:t}):e[r]=t,A=(e,r)=>{for(var t in r||(r={}))p.call(r,t)&&c(e,t,r[t]);if(s)for(var t of s(r))u.call(r,t)&&c(e,t,r[t]);return e},G=(e,r)=>{var t={};for(var n in e)p.call(e,n)&&r.indexOf(n)<0&&(t[n]=e[n]);if(e!=null&&s)for(var n of s(e))r.indexOf(n)<0&&u.call(e,n)&&(t[n]=e[n]);return t};const J={order:1},g=j.forwardRef((e,r)=>{const t=b("Title",J,e),{className:n,order:a,children:_,unstyled:h,size:y,weight:m,inline:v,variant:i}=t,P=G(t,["className","order","children","unstyled","size","weight","inline","variant"]),{classes:O,cx:x}=M({element:`h${a}`,weight:m,inline:v},{name:"Title",unstyled:h,variant:i,size:y});return[1,2,3,4,5,6].includes(a)?$.createElement(d,A({variant:i,component:`h${a}`,ref:r,className:x(O.root,n)},P),_):null});g.displayName="@mantine/core/Title";const Q=()=>{const e=z();return o.jsxs(E,{sx:{flex:1},h:"100vh",justify:"center",align:"center",direction:"column",gap:"24px",children:[o.jsx(g,{color:e.colorScheme==="dark"?"darkBlue.2":"blue.5",fw:500,children:"Ошибка 404"}),o.jsxs(d,{color:e.colorScheme==="dark"?"gray.3":"gray.5",align:"center",children:["Страница, которую вы пытаетесь открыть, не существует.",o.jsx("br",{}),"Наши разработчики будут оповещены об этой проблеме и примут меры для ее устранения."]}),o.jsx(T,{component:N,to:F.fragment,bg:e.colorScheme==="dark"?"darkBlue.2":"blue.5",sx:{":hover":{background:"darkBlue.2"}},children:"На главную"})]})};export{Q as default};
