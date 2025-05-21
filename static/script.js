let body = document.querySelector('body');
/** @type {HTMLButtonElement} */
let but_theme = document.querySelector('#theme');
let text = document.querySelector('h1');
let themeColor = false;
let theme = localStorage.getItem('theme') === 'true';
theme
	? body.classList.toggle('dark-theme', theme)
	: body.classList.toggle('dark-theme', theme);

but_theme.addEventListener('click', () => {
	themeColor = !themeColor
	localStorage.setItem('theme', themeColor);
	body.classList.toggle('dark-theme', themeColor);
});




