class Bmi_modules:
    @staticmethod
    def base_bw_calculation(height: float)-> float:#身長から基準体重の算出
        base_bw = 22*((height/100)**2)
        return base_bw