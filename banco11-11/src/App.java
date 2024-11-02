public class App {
    public static void main(String[] args) throws Exception {
        ContaPoupanca c1 = new ContaPoupanca(2020);

        c1.depositar(2000);
        c1.sacar(20);
    }
}
