const form = document.getElementById("login");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/api/token/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        if (!response.ok) {
            throw new Error("Invalid credentials");
        }

        const data = await response.json();

        // 🔐 Store tokens
        localStorage.setItem("access", data.access);
        localStorage.setItem("refresh", data.refresh);

        alert("Login successful!");
        console.log("ACCESS TOKEN:", data.access);

        // Example: call protected API
        getProtectedData();

    } catch (error) {
        alert(error.message);
    }
});

// 🔒 Protected API call
async function getProtectedData() {
    const token = localStorage.getItem("access");

    const response = await fetch("http://127.0.0.1:8000/api/products/", {
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    const data = await response.json();
    console.log("Protected data:", data);
}
