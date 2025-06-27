async function summarizeArticle(article) {
    const response = await fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: article })
    });

    const data = await response.json();
    return data.summary || "Error generating summary.";
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("submit").onclick = async function () {
        const user = document.getElementById("txt").value;

        document.body.style.cursor = "wait"; //show hourglass cursor

        try {
            const generated = await summarizeArticle(user);
            document.getElementById("output").innerText = generated;
        } catch (error) {
            console.error("Error summarizing:", error);
            document.getElementById("output").innerText = "Something went wrong.";
        } finally {
            document.body.style.cursor = "default"; //default
        }
    };
});
