class Solution:
    def parse_layers(self, pixels, width, height):
        num_layers = len(pixels) // width // height
        return (pixels[i*width*height:(i+1)*width*height] for i in range(num_layers))

    def solve_1(self, text):
        pixels = [int(x) for x in text.strip()]
        fewest_zeros = min(self.parse_layers(pixels, 25, 6), key=lambda lyr: lyr.count(0))
        return fewest_zeros.count(1) * fewest_zeros.count(2)

    def composite_image(self, layers, width, height):
        def composite_pixel(i):
            for layer in layers:
                if layer[i] < 2:
                    return layer[i]
            return 2

        return [composite_pixel(i) for i in range(width * height)]

    def solve_2(self, text):
        pixels = [int(x) for x in text.strip()]
        layers = list(self.parse_layers(pixels, 25, 6))
        image = self.composite_image(layers, 25, 6)

        for i in range(6):
            print(''.join('*' if x is 1 else ' ' for x in image[i*25:(i+1)*25]))
