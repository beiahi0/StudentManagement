/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.{html,js}"],

    theme: {
        container: {
            padding: '7rem',
            center: true,
        },
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}

