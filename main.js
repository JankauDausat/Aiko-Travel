
            const correctEmail = "user@example.com";
            const correctPassword = "password123";
            let attemptCount = 0;

            document.getElementById("loginForm").addEventListener("submit", function(event) {
                event.preventDefault();
                
                const email = document.getElementById("email").value;
                const password = document.getElementById("password").value;
                
                if (email === correctEmail && password === correctPassword) {
                    window.location.href = "../after/after-login.html";
                } else {
                    attemptCount++;
                    document.getElementById("error-message").style.display = "block";
                
                    if (attemptCount >= 3) {
                        document.getElementById("resetButton").style.display = "block";
                    }
                }
            });

            document.getElementById("resetButton").addEventListener("click", function() {
                alert("Silakan hubungi admin untuk mereset password Anda.");
            });