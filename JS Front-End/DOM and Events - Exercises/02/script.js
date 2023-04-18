function create(words) {
   const contentDiv = document.getElementById('content');
 
   // create a div with a paragraph for each word
   words.forEach(word => {
     const div = document.createElement('div');
     const p = document.createElement('p');
     p.textContent = word;
     p.style.display = 'none'; // initially hide the paragraph
     div.appendChild(p);
 
     // add click event listener to show the paragraph when the div is clicked
     div.addEventListener('click', () => {
       p.style.display = 'block';
     });
 
     contentDiv.appendChild(div);
   });
 }
 