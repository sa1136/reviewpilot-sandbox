const { createSession, verifySession, isAdmin, displayName } = require("./session");

test("a fresh session verifies", () => {
  const token = createSession("u1");
  expect(verifySession(token).userId).toBe("u1");
});

test("a tampered session is rejected", () => {
  expect(verifySession("u1.123.bad")).toBeNull();
});

test("isAdmin is false without the role", () => {
  expect(isAdmin({ roles: ["viewer"] })).toBe(false);
});

test("displayName is a function", () => {
  expect(typeof displayName).toBe("function");
});
