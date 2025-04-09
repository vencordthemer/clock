let use24HourFormat = true; // Default to 24-hour format

function updateClock() {
    const clockElement = document.getElementById('clock');
    if (!clockElement) {
        console.error("Clock element not found!");
        return; // Stop if the element doesn't exist
    }

    const now = new Date();
    let hours = now.getHours();
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    let ampm = '';

    if (!use24HourFormat) {
        ampm = hours >= 12 ? ' PM' : ' AM';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
    }

    const hoursStr = String(hours).padStart(2, '0');

    clockElement.textContent = `${hoursStr}:${minutes}:${seconds}${ampm}`;
}

// Toggle format function
function toggleFormat() {
    use24HourFormat = !use24HourFormat;
    updateClock(); // Update the clock display immediately
}

// Add event listener to the button
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('format-toggle');
    if (toggleButton) {
        toggleButton.addEventListener('click', toggleFormat);
    }
});

// Update the clock immediately on load
updateClock();

// Update the clock every second
setInterval(updateClock, 1000); 