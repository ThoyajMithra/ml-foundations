class Vector:
    def __init__(self,components):
        self.components=list(components)
        self.dimentions=len(components)

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self,other):
        return sum([a * b for a, b in zip(self.components, other.components)])

    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5
    
    def normalize(self):
        mag = self.magnitude()
        return Vector([x / mag for x in self.components])
    
    def cosine_similarity(self,other):
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def __repr__(self):
        return f"Vector({self.components})"

    # def __str__(self):
    #     return f"sorry nigga"


if __name__=="__main__":
    a=Vector([1,2,3])
    b=Vector([2,3,1])

    print(f"a + b = {a + b}")
    print(f"a · b = {a.dot(b)}")
    print(f"|a| = {a.magnitude():.4f}")
    print(f"cosine similarity = {a.cosine_similarity(b):.4f}")
    print(b)



