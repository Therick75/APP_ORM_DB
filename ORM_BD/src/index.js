import express from "express";
import categories_routes from "./routes/categories_routes.js";
import products_routes from "./routes/products_routes.js";
import users_routes from "./routes/users_routes.js";

const app = express();


app.use(express.json());

app.use("/api", products_routes);
app.use("/api", categories_routes);
app.use("/api",users_routes);
app.listen(3000);
console.log("Server on port", 3000);