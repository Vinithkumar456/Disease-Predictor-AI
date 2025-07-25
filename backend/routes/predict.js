const express = require("express");
const router = express.Router();
const { spawn } = require("child_process");

router.post("/predict", (req, res) => {
  const symptoms = req.body.symptoms;

  const python = spawn("python", ["./python/predict.py", JSON.stringify(symptoms)]);

  let result = "";
  python.stdout.on("data", (data) => {
    result += data.toString();
  });

  python.stderr.on("data", (data) => {
    console.error(`Python error: ${data}`);
  });

  python.on("close", (code) => {
    if (code !== 0) {
      return res.status(500).json({ error: "Prediction failed" });
    }
    try {
      const parsed = JSON.parse(result);
      res.json(parsed);
    } catch (e) {
      res.status(500).json({ error: "Failed to parse prediction result" });
    }
  });
});

module.exports = router;
