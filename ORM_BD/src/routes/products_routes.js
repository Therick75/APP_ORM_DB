import { Router } from "express";
import pkg from '@prisma/client';
const { PrismaClient } = pkg;



const router = Router();
const prisma = new PrismaClient();

router.get("/products", async(req, res)=>{
    const products = await prisma.product.findMany({
        include: {
            category:true,
        }
    })
    res.json(products)
});
router.get("/products/:id", async(req, res)=>{
    const prodcutfound = await prisma.product.findFirst({
        where: {
            id: parseInt(req.params.id)
        },
        include: {
            category: true,
        }
    }) 
    res.json(prodcutfound)
});
router.post("/products", async(req, res)=>{
    const newproduct = await prisma.product.create({
        data:req.body,
    })
    res.json(newproduct)
});
router.put("/products/:id", async(req, res)=>{
    const prodcutUpdate = await prisma.product.update({
        where: {
            id: parseInt(req.params.id)
        },
        data: req.body
    })
    if(!prodcutUpdate)
        return res.status(404).json({error: "Producto no existe"})
    res.json(prodcutUpdate)
});
router.delete("/products/:id", async(req, res)=>{
    const productDeleted = await prisma.product.delete({
        where: {
            id: parseInt(req.params.id)
        }
    })
    if(!productDeleted)
        return res.status(404).json({error: "Producto no encontrado"})
    res.json(productDeleted)
});

export default router;