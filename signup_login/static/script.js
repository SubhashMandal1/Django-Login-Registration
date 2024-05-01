const wrapper = document.querySelector('.wrapper')
const loginLink = document.querySelector('.login-link')
const registerLink = document.querySelector('.register-link')
const btnPopup = document.querySelector('.btnLogin-popup')
const iconClose = document.querySelector('.icon-close')

registerLink.addEventListener('click', () => {
  wrapper.classList.add('active')
})

loginLink.addEventListener('click', () => {
  wrapper.classList.remove('active')
})

btnPopup.addEventListener('click', () => {
  wrapper.classList.add('active-popup')
})

iconClose.addEventListener('click', () => {
  wrapper.classList.remove('active-popup')
})

$(document).ready(() => {
  $('#myForm').submit(event => {
    event.preventDefault() // Prevent default form submission behavior
    validateForm() // Call the form validation function
  })

  function validateForm() {
    var username = $('#username').val()
    var password = $('#password').val()
    var email = $('#email').val()
    var conpass = $('#conpass').val()

    // Make the Ajax request
    $.ajax({
      url: '/check_username/',
      type: 'POST',
      data: {
        username: username,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
      },
      success: response => {
        if (response.exists) {
          alert('Username already exists. Please choose a different username.')
        }
        if (username === '' || password === '' || email === '') {
          alert('Please fill in all fields.')
          return false
        }

        if (password !== conpass) {
          alert("Passwords doesn't match.")
          return false
        } else {
          // Submit the form if all validations pass
          $('#myForm').unbind('submit').submit()
        }
      },
      error: () => {
        alert('Error occurred while checking the username.')
      },
    })

    // Add more field validations as needed
    // if (username === '' || password === '' || email === '') {
    //   alert('Please fill in all fields.')
    //   return false
    // }

    // if (password !== conpass) {
    //   alert("Passwords doesn't match.")
    //   return false
    //}
  }
})
