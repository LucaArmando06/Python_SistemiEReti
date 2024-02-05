class Robot():
    def __init__(self, nome, massa, tipologia):
        self.nome = nome
        self.massa = massa
        self.tipologia = tipologia
    
    def controlloPericoloso(self):
        if self.tipologia == "Umanoide" and self.massa > 100:
            return f"il robot {self.nome} è pericoloso"
        else: 
            return f"il robot {self.nome} non è pericoloso"
        
    def stampaRobot(self):
        return f"Nome: {self.nome}, massa: {self.massa}, tipologia: {self.tipologia}"

def main():
    robot = Robot("robot", 200, "Non umanoide")
    print(robot.stampaRobot())
    print(robot.controlloPericoloso())

    robot1 = Robot("robot1", 200, "Umanoide")
    print(robot1.stampaRobot())
    print(robot1.controlloPericoloso())

if __name__ == "__main__":
    main()