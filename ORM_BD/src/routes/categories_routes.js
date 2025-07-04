import {Router} from "express";
import pkg from '@prisma/client';
const { PrismaClient } = pkg;
const router = Router();
const prisma = new PrismaClient();

router.get("/categories", async(req, res)=>{
    const categories = await prisma.category.findMany({
        include:{
            products:true,
        }
    })
    res.json(categories)
});
router.get("/categories/:id", async(req, res)=>{
    const categories = await prisma.category.findFirst({
        where: {
            id: parseInt(req.params.id)
        }
    })
    res.json(categories)
});
router.post("/categories", async(req, res)=>{
    const newcategory = await prisma.category.create({
        data:req.body,
    })
    res.json(newcategory)
});
router.delete("/categories/:id", async(req, res)=>{
    const categoriesDelete = await prisma.category.delete({
        where: {
            id: parseInt(req.params.id)
        }
    })
    if(!categoriesDelete)
        return res.status(404).json({error: "Categoria no encontrada"})
    res.json(categoriesDelete)
});
router.put("/categories/:id", async(req, res)=>{
    const categoriesUpdate = await prisma.category.update({
        where: {
            id: parseInt(req.params.id)
        },
        data: req.body,
    })
    if(!categoriesUpdate)
        return res.status(404).json({error: "Categoria no encontrada"})
    res.json(categoriesUpdate)
});


export default router;