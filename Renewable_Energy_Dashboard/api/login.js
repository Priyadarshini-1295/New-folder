export default function handler(req, res) {
    if (req.method !== "POST") {
        return res.status(405).json({
            message: "Method not allowed"
        });
    }

    const { username, password } = req.body;

    // Temporary credentials for our project
    if (username === "admin" && password === "admin123") {
        return res.status(200).json({
            success: true,
            message: "Login successful"
        });
    }

    return res.status(401).json({
        success: false,
        message: "Invalid username or password"
    });
}