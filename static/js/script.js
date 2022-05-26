const price = document.querySelector('#price')
const output = document.querySelector('#outputClass')

output.textContent = price.value;

price.addEventListener('input', function () {
    output.textContent = price.value;
})
