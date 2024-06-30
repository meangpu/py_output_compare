# nattapongTang_1287
import math


def calculate_cylinder_area(radius, height):
    return 2 * math.pi * radius * (radius + height)


def main():
    r = "radius "
    h = "height"
    a = "surface_area"

    print(f"{r} {h} {a}")
    for i in range(1, 11):
        radius = i
        height = i * 2
        print(
            f"{radius:{len(r)}} {height:{len(h)}} {calculate_cylinder_area(radius, height):{len(a)}.2f}"
        )
        pass


if __name__ == "__main__":
    main()
