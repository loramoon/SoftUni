function result() {
    let inputs = document.querySelectorAll('input');
    for (let i = 0; i < inputs.length; i++) {
      inputs[i].addEventListener('focus', (event) => {
        let currentDiv = event.target.parentNode;
        currentDiv.classList.add('focused');
      });
      inputs[i].addEventListener('blur', (event) => {
        let currentDiv = event.target.parentNode;
        currentDiv.classList.remove('focused');
      });
    }
  }
  