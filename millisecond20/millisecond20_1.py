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
        particles1 = list()
        smallest_a = None
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

            particle = Particle(i, p, v, a)

            if smallest_a is None or smallest_a >= particle.acceleration():
                smallest_a = particle.acceleration()
                particles1.append(particle)
        particles2 = list()
        smallest_v = None
        for particle in particles1:
            if particle.acceleration() == smallest_a:
                if smallest_v is None or smallest_v >= particle.velocity():
                    smallest_v = particle.velocity()
                    particles2.append(particle)
        particles3 = sorted(particles2, key=lambda ptc: ptc.distance())

        print(particles3[0].n)


if __name__ == '__main__':
    main()