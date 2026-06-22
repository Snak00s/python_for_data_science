class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print scalar product of V1 and V2"""
        dot = 0
        for i in range(len(V1)):
            dot += V1[i] * V2[i]
        print(dot)
        return

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print vect of addition of V1 and V2"""
        print([float(V1[i] + V2[i]) for i in range(len(V1))])
        return

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print vect of sub of V1 and V2"""
        print([float(V1[i] - V2[i]) for i in range(len(V1))])
        return
