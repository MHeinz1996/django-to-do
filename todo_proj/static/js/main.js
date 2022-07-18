function login(event) {
    event.preventDefault()
    let email = event.target[0].value
    let password = event.target[1].value
    console.log(`email: ${email}, password: ${password}`)
    
    axios.post('/login/', {
        'email': email,
        'password': password
    }).then((response) => {
        console.log(response)
        window.location.href = '/'
    })
}

function signup(event) {
    event.preventDefault()
    let email = event.target[0].value
    let password = event.target[1].value
    console.log(`email: ${email}, password: ${password}`)
    
    axios.post('/signup/', {
        'email': email,
        'password': password
    }).then((response) => {
        console.log(response)
        window.location.href = '/login/'
    })
}

function add_task(event) {
    event.preventDefault()
    let title = event.target[0].value
    let description = event.target[1].value
    console.log(`${title}: ${description}`)

    axios.post('add_task/', {
        'title': title,
        'description': description
    }).then((response) => {
        window.location.href = '/'
    })
}