import Container from "@/components/Container";

export default function Home() {
  return (
    <Container>
      <div>
        <h1 className="text-4xl font-bold text-zinc-900 dark:text-zinc-100">
          Welcome to the Home Page
        </h1>
        <p className="mt-4 text-zinc-700 dark:text-zinc-300">
          This is a protected page. You are successfully authenticated!
        </p>
      </div>
    </Container>
  );
}
