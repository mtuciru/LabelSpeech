import{a as m,b as h,u as f,S as d,j as a,C as x,B as g,T as c,c as w,L as N,d as j,G as k}from"./index-14422766.js";import{u as v,r as b,a as P,T as u,P as p,b as C}from"./ThemeButton-ba958bcd.js";import{C as S}from"./Checkbox-e0fe77da.js";import"./use-input-props-561b2f2e.js";const y=s=>s.length<3?"Логин должен быть длиннее":null,I=s=>{const t=s.split(" ");if(t.length<2)return"Введите корректное ФИО";const e=/^[а-я]{2,}$/i;return t.every(o=>e.test(o))?null:"Используйте кириллицу"},R=s=>s.length<8?"Пароль должен быть длиннее 8 символов":null,A=(s,t)=>s!==t?"Пароли должны совпадать":null,D=()=>{const{t:s}=m(),{successNotification:t,errorNotification:e}=h(),o=f();return[v({validate:{username:r=>s(y(r)),fullName:r=>s(I(r)),password:r=>s(R(r)),passwordConfirm:(r,l)=>s(A(r,l.password))},initialValues:{username:"",fullName:"",password:"",passwordConfirm:"",isStudent:!1,group:""}}),r=>{b(r).then(()=>{t(s("Вы успешно зарегистрировались")),o(d.login)}).catch(l=>{switch(l.request.status){case 406:e(s("Учетная запись с таким логином уже существует"));break;default:e(s("Проверьте вводимые данные"))}})}]},T=()=>{const{classes:s}=P(),{t}=m(),[e,o]=D(),n=i=>{i.keyCode===32&&i.preventDefault()};return a.jsx(x,{className:s.root,children:a.jsxs(g,{className:s.form,children:[a.jsx(c,{className:s.title,children:"Label Speech"}),a.jsx(u,{withAsterisk:!0,placeholder:t("Логин"),className:s.input,onKeyDown:n,...e.getInputProps("username")}),a.jsx(u,{withAsterisk:!0,className:s.input,placeholder:t("Имя и фамилия пользователя"),...e.getInputProps("fullName")}),a.jsx(p,{withAsterisk:!0,placeholder:t("Пароль"),onKeyDown:n,radius:"7px",className:s.password,...e.getInputProps("password")}),a.jsx(p,{withAsterisk:!0,placeholder:t("Повторите пароль"),onKeyDown:n,radius:"7px",className:s.password,...e.getInputProps("passwordConfirm")}),a.jsx(S,{label:t("Являетесь ли Вы членом группы"),...e.getInputProps("isStudent"),size:"xs",className:s.checkbox}),e.values.isStudent&&a.jsx(u,{withAsterisk:!0,placeholder:t("Ваша группа"),onKeyDown:n,className:s.input,...e.getInputProps("group")}),a.jsx(w,{type:"submit",disabled:!(e.values.username&&e.values.fullName&&e.values.password&&e.values.passwordConfirm)||e.values.isStudent&&!e.values.group,className:s.auth,onClick:()=>{o(e.values)},children:t("Зарегистрироваться")}),a.jsxs(c,{className:s.link,children:[t("Уже есть аккаунт?")," ",a.jsx(N,{to:d.login,className:s.link,children:t("Войти")})]})]})})},F=()=>a.jsxs(j,{spacing:0,h:"100vh",children:[a.jsx(k,{position:"right",children:a.jsx(C,{})}),a.jsx(T,{})]});export{F as default};