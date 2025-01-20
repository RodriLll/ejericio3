from schemas.russian_roulette import BulletType

class RussianRouletteService:

    @staticmethod
    def shoot(payload: dict) -> bool:
        bullet_type = payload.get("bullet_type")
        dong_size = payload.get("dong_size")

        if bullet_type in [BulletType.SILVER, BulletType.GOLD] and dong_size < 0.5:
            return {"message": "Safaste makinola"}
        if bullet_type in [BulletType.SILVER, BulletType.GOLD] and dong_size > 0.5:
            return {"message": "Te cabio la papirola por manicero"}
        if bullet_type == BulletType.DIAMOND:
            return {"message": "Solo pitudos pueden jugar con balas de diamante"}
        else:
            return {"message": "No se que hiciste pero no deberias haber llegado hasta aca"}
        