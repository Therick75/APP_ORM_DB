import {Router} from "express";
import bcrypt from "bcrypt";
import pkg from '@prisma/client';
const { PrismaClient } = pkg;
const router = Router();
const prisma = new PrismaClient();

router.get("/users", async(req, res)=>{
    const user = await prisma.users.findMany()
    res.json(user)
});
// Obtener usuario por ID
router.get("/users/:id", async (req, res) => {
  const user = await prisma.users.findUnique({
    where: { id: parseInt(req.params.id) },
  });

  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  res.json(user);
});
// Crear nuevo usuario con contraseña hasheada
router.post("/users", async (req, res) => {
  try {
    const { name, correo, password } = req.body;
    // Verifica que los datos existen
    if (!name || !correo || !password) {
      return res.status(400).json({ error: "Faltan campos obligatorios" });
    }
    // Encriptar contraseña
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = await prisma.users.create({
      data: {
        name,
        correo,
        password: hashedPassword,
      },
    });
    res.status(201).json(newUser);
  } catch (error) {
    res.status(500).json({ error: "Error al crear usuario", details: error });
  }
});
// Actualizar usuario
router.put("/users/:id", async (req, res) => {
  try {
    const { name, correo, password } = req.body;
    const userId = parseInt(req.params.id);
    const existingUser = await prisma.users.findUnique({ where: { id: userId } });
    if (!existingUser) return res.status(404).json({ error: "Usuario no encontrado" });
    // Si envía nueva contraseña, la hasheamos
    const updatedData = {
      ...(name && { name }),
      ...(correo && { correo }),
      ...(password && { password: await bcrypt.hash(password, 10) }),
    };
    const updatedUser = await prisma.users.update({
      where: { id: userId },
      data: updatedData,
    });
    res.json(updatedUser);
  } catch (error) {
    res.status(500).json({ error: "Error al actualizar usuario", details: error });
  }
});
// Eliminar usuario
router.delete("/users/:id", async (req, res) => {
  try {
    const deletedUser = await prisma.users.delete({
      where: { id: parseInt(req.params.id) },
    });

    res.json(deletedUser);
  } catch (error) {
    res.status(404).json({ error: "Usuario no encontrado" });
  }
});

export default router;

