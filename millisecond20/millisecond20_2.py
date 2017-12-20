class Particle:
    def __init__(self, n, p, v, a):
        self.n = n
        self.p = p
        self.v = v
        self.a = a

    def distance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

    def velocity(self):
        return abs(self.v[0]) + abs(self.v[1]) + abs(self.v[2])

    def acceleration(self):
        return abs(self.a[0]) + abs(self.a[1]) + abs(self.a[2])


    def update(self):
        next_velocity = (self.v[0] + self.a[0], self.v[1] + self.a[1], self.v[2] + self.a[2])
        self.v = next_velocity
        next_position = (self.p[0] + self.v[0], self.p[1] + self.v[1], self.p[2] + self.v[2])
        self.p = next_position


def main():
    with open("input") as file:
        lines = [line.split(", ") for line in file.read().splitlines()]
        particles = list()
        for i, line in enumerate(lines):
            start = line[0].index('<')
            end = line[0].index('>')
            p = tuple([int(num) for num in line[0][start+1:end].split(",")])

            start = line[1].index('<')
            end = line[1].index('>')
            v = tuple([int(num) for num in line[1][start + 1:end].split(",")])

            start = line[2].index('<')
            end = line[2].index('>')
            a = tuple([int(num) for num in line[2][start + 1:end].split(",")])

            particles.append(Particle(i, p, v, a))
        destroyed = set()

        rounds = 0

        # Too much trouble to calculate if particles are going to collide
        # Let's just assume they are done colliding when there has not been
        # any for 100 updates
        while rounds < 100:
            rounds += 1
            for i in range(0, len(particles)):
                curr = particles[i]
                if curr.n not in destroyed:
                    for particle in particles[i+1:]:
                        if particle.n not in destroyed and curr.p == particle.p:
                            destroyed.add(curr.n)
                            destroyed.add(particle.n)
                            rounds = 0
            for particle in particles:
                if particle.n not in destroyed:
                    particle.update()
        print(len(particles) - len(destroyed))

if __name__ == '__main__':
    main()