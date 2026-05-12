import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    width = max(10, os.get_terminal_size().columns - 40)
    start = os.times().elapsed

    # Affichage initial avant de commencer l'itération
    print(
        f"{0:3d}%|{' ' * width}| 0/{total} [00:00<?, ?it/s]",
        flush=True,
    )

    for index, item in enumerate(lst, start=1):
        elapsed = os.times().elapsed - start
        rate = index / elapsed if elapsed > 0 else 0.0

        percent = index / total
        filled = int(width * percent)

        # Construction de la barre
        bar = "█" * filled + " " * (width - filled)

        # Temps écoulé au format MM:SS
        elapsed_minutes = int(elapsed // 60)
        elapsed_seconds = int(elapsed % 60)
        elapsed_str = (
            f"{elapsed_minutes:02d}:{elapsed_seconds:02d}"
        )

        # Temps restant estimé au format MM:SS
        remaining = (
            (total - index) / rate if rate > 0 else 0
        )
        remaining_minutes = int(remaining // 60)
        remaining_seconds = int(remaining % 60)
        remaining_str = (
            f"{remaining_minutes:02d}:{remaining_seconds:02d}"
        )

        # Mise à jour sur la même ligne
        print(
            f"\r{int(percent * 100):3d}%|{bar}| "
            f"{index}/{total} "
            f"[{elapsed_str}<{remaining_str}, "
            f"{rate:5.2f}it/s]",
            end="",
            flush=True,
        )

        yield item


def main() -> int:
    """
   The function must copy the function tqdm with the yield operator.

    Args:
        argv (list[str]): Command line arguments.

    Returns:
        int: 0 on success, 1 on error.
    """
    for _ in ft_tqdm(range(0, 333)):
        pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
