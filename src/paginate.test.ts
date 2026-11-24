import { describe, expect, it } from "vitest";
import { pageFromQuery, pageLabel, paginate, totalPages } from "./paginate";

describe("paginate", () => {
  it("counts pages for an exact fit", () => {
    expect(totalPages(20, 10)).toBe(2);
  });

  it("returns the requested page number", () => {
    expect(paginate([1, 2, 3], 1, 10).page).toBe(1);
  });

  it("reads the page from the query", () => {
    expect(pageFromQuery("3")).toBe(3);
    expect(pageFromQuery(undefined)).toBe(1);
  });

  it("labels the page", () => {
    expect(pageLabel(2, 5)).toBe("Page 2 of 5");
    expect(pageLabel(1, 0)).toBe("Page 1 of 1");
  });
});
