const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

$(document).ready(() => {
    $('[data-toggle="popover"]').popover();   
});

// const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
// const popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
//     return new bootstrap.Popover(popoverTriggerEl)
// })
// const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
// const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
//     return new bootstrap.Tooltip(tooltipTriggerEl)
// })

const button = document.querySelector('#button');
const tooltip = document.querySelector('#tooltip');

// const popperInstance = Popper.createPopper(button, tooltip, {
//     modifiers: [
//         {
//             name: 'offset',
//             options: {
//                 offset: [0, 8],
//             },
//         },
//     ],
// });
function show() {
// Make the tooltip visible
tooltip.setAttribute('data-show', '');
// Enable the event listeners
popperInstance.setOptions((options) => ({
    ...options,
    modifiers: [
        ...options.modifiers,
        { name: 'eventListeners', enabled: true },
    ],
}));
// Update its position
popperInstance.update();
}
function hide() {
// Hide the tooltip
    tooltip.removeAttribute('data-show');

// Disable the event listeners
    popperInstance.setOptions((options) => ({
        ...options,
        modifiers: [
            ...options.modifiers,
            { name: 'eventListeners', enabled: false },
        ],
    }));
}

const showEvents = ['mouseenter', 'focus'];
const hideEvents = ['mouseleave', 'blur'];

showEvents.forEach((event) => {
button.addEventListener(event, show);
});

hideEvents.forEach((event) => {
    button.addEventListener(event, hide);
});

// const popover = new bootstrap.Popover('.example-popover', {
//     container: 'body'
// });