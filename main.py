from triangle import TriangleAnalyzer

def main():
    print("\n" + "=" * 50)
    print("ОПРЕДЕЛЕНИЯ ТРЕУГОЛЬНИКА")
    print("=" * 50)
    print("Велдите длтины сторон")
    print()
    
    triangle_analyzer = TriangleAnalyzer(100)
    
    while True:
        print("-" * 40)
        input_a = input("Сторона A: ")
        if input_a.lower() == 'exit':
            print("\nПрограмма завершена")
            break
            
        input_b = input("Сторона B: ")
        if input_b.lower() == 'exit':
            print("\nПрограмма завершена")
            break
            
        input_c = input("Сторона C: ")
        if input_c.lower() == 'exit':
            print("\nПрограмма завершена")
            break
        
        print()
        triangle_type, vertex_coords = triangle_analyzer.process_request(input_a, input_b, input_c)
        
        if triangle_type:
            print(f"Результат: {triangle_type}")
            print(f"Координаты вершин (в поле 100x100):")
            print(f"   Вершина A: {vertex_coords[0]}")
            print(f"   Вершина B: {vertex_coords[1]}")
            print(f"   Вершина C: {vertex_coords[2]}")
        print()

if __name__ == "__main__":
    main()