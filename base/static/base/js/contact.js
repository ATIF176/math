document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var form = event.target;
    var formData = new FormData(form);
  
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'submit-form.php', true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        form.reset();
        document.getElementById('success-message').classList.remove('hidden');
      }
    };
    xhr.send(formData);
  });
  