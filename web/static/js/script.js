// Animate the heading
gsap.from("h1", {
    duration: 1,
    y: -50,
    opacity: 0,
    ease: "power3.out",
    delay:5
});

// Animate the form
gsap.from("form", {
    duration: 1,
    x: -100,
    opacity: 0,
    delay: 5
});

// Animate each expense list item
gsap.from("#expense-list li", {
    duration: 0.6,
    x: -30,
    opacity: 0,
    stagger: 0.1,
    delay: 5
});
