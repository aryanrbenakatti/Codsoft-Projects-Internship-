document.getElementById("passwordForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const length = document.getElementById("length").value;

    // Disable form elements to prevent multiple submissions
    document.getElementById("passwordForm").querySelector("button").disabled = true;
    document.getElementById("message").textContent = "Generating password...";

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `length=${length}`,
    });

    const result = await response.json();

    // Enable button back after request
    document.getElementById("passwordForm").querySelector("button").disabled = false;

    if (response.ok) {
        document.getElementById("password").value = result.password;
        document.getElementById("message").textContent = "Password generated successfully!";
        document.getElementById("message").style.color = "green"; // Success message
    } else {
        document.getElementById("message").textContent = result.error;
        document.getElementById("message").style.color = "red"; // Error message
    }
});

document.getElementById("copyButton").addEventListener("click", () => {
    const passwordField = document.getElementById("password");
    passwordField.select();
    document.execCommand("copy");

    // Feedback for copying
    const messageElement = document.getElementById("message");
    messageElement.textContent = "Password copied to clipboard!";
    messageElement.style.color = "blue"; // Change message color for "copy" action

    // Play a quick animation for the "Copy" action
    document.getElementById("copyButton").style.transform = "scale(1.1)";
    setTimeout(() => {
        document.getElementById("copyButton").style.transform = "scale(1)";
    }, 200);
});

// 3D effect for tilting the container based on cursor position
document.querySelector('.container').addEventListener('mousemove', (e) => {
    const container = document.querySelector('.container');
    const rect = container.getBoundingClientRect();
    const offsetX = e.clientX - rect.left; // Get cursor X position relative to container
    const offsetY = e.clientY - rect.top;  // Get cursor Y position relative to container
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    // Calculate the tilt values based on cursor position
    const deltaX = (offsetX - centerX) / centerX;
    const deltaY = (offsetY - centerY) / centerY;

    // Apply the tilt effect to the container (using CSS transform property)
    container.style.transform = `rotateY(${deltaX * 15}deg) rotateX(${deltaY * -15}deg)`; // Adjust rotation angles
});

// Reset the tilt effect when the mouse leaves the container
document.querySelector('.container').addEventListener('mouseleave', () => {
    const container = document.querySelector('.container');
    container.style.transform = 'rotateY(0deg) rotateX(0deg)';
});
