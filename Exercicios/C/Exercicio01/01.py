def desenhar_caixa():
    print("Caixa:")
    print("**********")
    for _ in range(3):
        print("*        *")
    print("**********\n")

def desenhar_oval():
    print("Oval:")
    print("   ****   ")
    print(" *      * ")
    print("*        *")
    print(" *      * ")
    print("   ****   \n")

def desenhar_seta():
    print("Seta:")
    print("    *    ")
    print("   ***   ")
    print("  *****  ")
    print("    *    ")
    print("    *    ")
    print("    *    ")
    print("    *    \n")

def desenhar_losango():
    print("Losango:")
    print("    *    ")
    print("   * *   ")
    print("  *   *  ")
    print(" *     * ")
    print("  *   *  ")
    print("   * *   ")
    print("    *    \n")

# Chamada das funções
desenhar_caixa()
desenhar_oval()
desenhar_seta()
desenhar_losango()