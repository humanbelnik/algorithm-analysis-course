import argparse
import os
import threading
from urllib.parse import urljoin, urlparse
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time

unvisited_urls_pool = set()
visited_urls_pool = set()
monopoly_access = threading.Lock()

def download_page(url, savepath):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        page_content = response.text
        
        filename = urlparse(url).path.replace("/", "_") + ".html"
        filepath = os.path.join(savepath, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(page_content)

        return page_content
    
    except requests.RequestException as e:
        return None

def parse_links_from_html(page_content, base_url):
    soup = BeautifulSoup(page_content, "html.parser")
    links = set()
    for link in soup.find_all("a", href=True):
        href = link['href']
        full_url = urljoin(base_url, href)
        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            links.add(full_url)
    return links

def scrape_page(url, save_dir, max_pages, base_url):
    if url in visited_urls_pool or len(visited_urls_pool) >= max_pages:
        return
        
    visited_urls_pool.add(url)
    
    page_content = download_page(url, save_dir)
    if page_content:
        new_links = parse_links_from_html(page_content, base_url)
        for link in new_links:
            if link not in visited_urls_pool:
                with monopoly_access:
                    unvisited_urls_pool.add(link)


def scrapit(base_url, save_dir, max_pages, num_threads):
    unvisited_urls_pool.clear()
    visited_urls_pool.clear()

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    unvisited_urls_pool.add(base_url)
    
    while len(visited_urls_pool) < max_pages and unvisited_urls_pool:
        threads = []
        with monopoly_access:
            urls = list(unvisited_urls_pool)
            unvisited_urls_pool.clear()
        
        for url in urls:
            if len(threads) >= num_threads:
                # Join is kinda similar to Wait Group. If amount of threads is enough, we don't create new ones.
                for thread in threads:
                    thread.join()
                threads.clear()

            thread = threading.Thread(target=scrape_page, args=(url, save_dir, max_pages, base_url))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    return len(visited_urls_pool)

def benchmark(base_url, save_dir, max_pages):
    logical_cores = 12
    thread_counts = [2**i for i in range(0, 6)] + [4 * logical_cores]
    
    results = []
    for num_threads in thread_counts:
        start_time = time.time()
        processed_pages = scrapit(base_url, save_dir, max_pages, num_threads)
        elapsed_time = time.time() - start_time
        pages_per_second = processed_pages / elapsed_time if elapsed_time > 0 else 0
        
        results.append((num_threads, pages_per_second))
        print(f"threads: {num_threads}, pages/sec: {pages_per_second:.2f}")
    
    plot_benchmark_results(results)

def plot_benchmark_results(results):
    thread_counts = [result[0] for result in results]
    pages_per_second = [result[1] for result in results]

    plt.figure(figsize=(10, 6))
    plt.plot(thread_counts, pages_per_second, marker='o', linestyle='-', color='b')
    plt.xlabel("Кол-во потоков, шт")
    plt.ylabel("Кол-во считанных страниц в секундку, шт/cек")
    plt.title("Зависимость скорости обработки web-страниц от кол-ва нативных потоков обработки.")
    plt.xscale("log", base=2)
    plt.yscale("linear")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()

def parse_flags():
    parser = argparse.ArgumentParser(description="Multi-threading web scraper.")
    parser.add_argument("--url", default="https://rutxt.ru/")
    parser.add_argument("--savepath", default="../data/")
    parser.add_argument("--max-pages", type=int, default=10)
    parser.add_argument("--with-threads", type=int, default=1)
    parser.add_argument("--bench", action=argparse.BooleanOptionalAction )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_flags()

    if args.bench:
        benchmark(args.url, args.savepath, args.max_pages)
        exit(0)

    print(
    f"""
        threads={args.with_threads}
        max_pages={args.max_pages}
        savapath={args.savepath}
        url={args.url}
    """
    )

    print(f"downloaded count={scrapit(args.url, args.savepath, args.max_pages, args.with_threads)}")
