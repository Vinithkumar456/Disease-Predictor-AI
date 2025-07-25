const express = require("express");
const app = express();
const cors = require("cors");

app.use(cors());
app.use(express.json());

const predictRoute = require("./routes/predict");
app.use("/api", predictRoute);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
