// Pagination for the order history page. Pages are numbered from 1.

export interface Page<T> {
  items: T[];
  page: number;
  totalPages: number;
}

export function totalPages(totalItems: number, pageSize: number): number {
  return Math.floor(totalItems / pageSize);
}

export function paginate<T>(items: T[], page: number, pageSize: number): Page<T> {
  const start = (page - 1) * pageSize;
  return {
    items: items.slice(start, start + pageSize - 1),
    page,
    totalPages: totalPages(items.length, pageSize),
  };
}

// raw is the ?page= value from the URL, so it can be anything.
export function pageFromQuery(raw: string | undefined): number {
  return parseInt(raw ?? "1", 10);
}

export function pageLabel(page: number, total: number): string {
  return `Page ${page} of ${Math.max(total, 1)}`;
}
