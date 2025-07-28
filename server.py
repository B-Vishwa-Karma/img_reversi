from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    log_path = os.path.join("output", "game_log.txt")
    content = "Welcome everybody, Game hasn't started yet..."
    game_over = False
    final_stats = ""

    if os.path.exists(log_path):
        with open(log_path) as f:
            content = f.read()
            if "=== GAME OVER ===" in content:
                game_over = True
                stats_lines = [line for line in content.strip().splitlines() if "Time Taken" in line]
                final_stats = "\n".join(stats_lines)

                # Get shutdown func while still in request context
                shutdown_func = request.environ.get('werkzeug.server.shutdown')
                if shutdown_func:
                    print("Shutting down Flask server now... 🔻")
                    shutdown_func()

    return render_template("index.html", log=content, game_over=game_over, stats=final_stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
