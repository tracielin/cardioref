function myRender()
{
	document.body.innerHTML = document.body.innerHTML.replace(/\\\$/g, '\%\%');
	document.body.innerHTML = document.body.innerHTML.replace(/\$([\s\S]+?)\$/g, '<span class=\"maths\">$1</span>');
	document.body.innerHTML = document.body.innerHTML.replace(/\\\\\[/g, '%%%');
	document.body.innerHTML = document.body.innerHTML.replace(/\\\[/g, '<div class=\"maths\">');
	document.body.innerHTML = document.body.innerHTML.replace(/\\\]/g, '</div>');
	document.body.innerHTML = document.body.innerHTML.replace(/%%%/g, '\\\\\[');	
	document.body.innerHTML = document.body.innerHTML.replace(/\\\(/g, '<span class=\"maths\">');
	document.body.innerHTML = document.body.innerHTML.replace(/\\\)/g, '</span>');
	document.body.innerHTML = document.body.innerHTML.replace(/\%\%/g, '\$');

	// Get all <div class ="maths"> elements in the document

	var x = document.getElementsByClassName('maths');

	for (var i = 0; i < x.length; i++) {
		try {
			if(x[i].tagName == "DIV"){
				t= katex.render(x[i].textContent,x[i],{ displayMode: true }); 
			} else {
				t= katex.render(x[i].textContent,x[i]);
			}
		}
		catch(err) {
			x[i].style.color = 'red';
			x[i].textContent= err;
		}

	}

	document.body.innerHTML = document.body.innerHTML.replace(/\%\[/g, '\\\[');
	document.body.innerHTML = document.body.innerHTML.replace(/\%\]/g, '\\\]');
	document.body.innerHTML = document.body.innerHTML.replace(/\%\(/g, '\\\(');
	document.body.innerHTML = document.body.innerHTML.replace(/\%\)/g, '\\\)');
}
