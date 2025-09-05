// Animate the main heading using GSAP library
gsap.from("h1", {
    duration: 1,        // Animation lasts 1 second
    y: -50,             // Starts 50px above and moves down
    opacity: 0,         // Starts fully transparent
    ease: "power3.out", // Smooth easing function
    delay: 0.5          // Wait for half a second before starting
});

// Animate the form sliding in from left
gsap.from("form", {
    duration: 1,
    x: -100,            // Starts 100px left and moves right
    opacity: 0,         // Starts invisible
    delay: 1            // Starts after heading animation
});

// Animate each expense list item individually with a stagger effect
gsap.from("#expense-list li", {
    duration: 0.6,
    x: -30,             // Each item slides in from left by 30px
    opacity: 0,         // Starts transparent
    stagger: 0.1,       // Delay each item's animation by 0.1 seconds
    delay: 1.5          // Starts after form animation
});
