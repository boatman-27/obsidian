---
tags:
  - random
  - programming
---
This document provides an overview of how to set up a Next.js project, understand its file structure, handle routing and navigation, work with images (including external sources), use server and client components, implement dynamic routing and loading states, and create API routes.

---
## 🚀 1. Setup
1. **Install Node.js**: Make sure you have Node.js installed (preferably the latest LTS version).
2. **Create a new Next.js project**:
    ```bash
    npx create-next-app@latest my-next-app
    cd my-next-app
    ```
3. **Run the development server**:
    ```bash
    npm run dev
    ```
    Your app will be available at `http://localhost:3000`.
---
## 📂 2. File Structure
A typical Next.js project looks like this:

```
my-next-app/
├── app/               # (optional) New App Router directory
│   ├── page.tsx       # Entry point for the route "/"
│   ├── layout.tsx     # Shared layout
│   ├── about/         # Nested route: "/about"
│   └── blog/[slug]/   # Dynamic route: "/blog/:slug"
├── pages/             # (Classic Pages Router, optional)
│   ├── index.tsx      # Entry point for the route "/"
│   ├── about.tsx      # Route "/about"
│   └── api/           # API routes (serverless functions)
├── public/            # Static assets (images, fonts, etc.)
├── styles/            # CSS/SCSS files
├── next.config.js     # Next.js configuration
├── tsconfig.json      # TypeScript config (if using TS)
└── package.json       # Project metadata and dependencies
```

- **`app/`**: The new App Router directory (recommended for new projects).
- **`pages/`**: Legacy Pages Router directory (still valid).
- **`public/`**: Static files served at the root URL.
- **`styles/`**: Global styles or CSS Modules.

---

## 🧭 3. Routes and Navigation

### Pages Router (`pages/`)

- Each `.tsx` or `.js` file inside `pages/` automatically becomes a route.
- Nested folders create nested routes.
- Dynamic routes: `[param].tsx`.

### App Router (`app/`)

- Use `page.tsx` for route entry points.
- Use `layout.tsx` for layouts shared across routes.
- Dynamic routes use `[param]` syntax.

### Linking Between Routes

Use the `Link` component:

```tsx
import Link from 'next/link';

export default function Home() {
  return (
    <Link href="/about">About Page</Link>
  );
}
```

---

## 🖼️ 4. Images & External Sources

Next.js optimizes images with the `<Image>` component:

```tsx
import Image from 'next/image';

<Image
  src="/my-image.jpg"
  alt="Description"
  width={500}
  height={300}
/>
```

### External Images

To use images from external domains, update `next.config.js`:

```js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        pathname: '/images/**',
      },
    ],
  },
};
```

---

## 🧩 5. Server vs Client Components

- **Server Components**: Run only on the server, never send unnecessary JS to the client. Use `.server.tsx` conventionally, or just use default `page.tsx`.
    
- **Client Components**: Must include `'use client'` at the top. Required for interactivity (state, effects, event listeners).
    

Example Client Component:

```tsx
'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

---

## 📚 6. Dynamic Routing & Loading States

### Dynamic Routes

- File name: `[id]/page.tsx`
- Example path: `/blog/[slug]/page.tsx` -> `/blog/my-first-post`

Access params:

```tsx
export default function Page({ params }: { params: { slug: string } }) {
  return <div>Post: {params.slug}</div>;
}
```

### Loading States

In the App Router, use a `loading.tsx` file in the same directory:

```
blog/[slug]/
 ├── page.tsx
 └── loading.tsx
```

`loading.tsx` will automatically display while your dynamic page is generating.

---
## ⚙️ 7. API Routes

Next.js lets you build backend endpoints using the `pages/api/` directory.
Example `pages/api/hello.ts`:

```ts
import type { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ message: 'Hello from API!' });
}
```

- Available at `/api/hello`.
- Runs as a serverless function.

---
## ✅ Summary
- **Setup**: `create-next-app`
- **File Structure**: `app/` for App Router, `pages/` for Pages Router.
- **Routes**: Automatic file-based routing, dynamic segments with `[param]`.
- **Navigation**: Use `Link` component.
- **Images**: Use `<Image>`, configure `remotePatterns` for external hosts.
- **Components**: Use Server Components by default; mark interactive ones as `'use client'`.
- **Dynamic Routing**: Use `[param]` and `loading.tsx` for smooth UX.
- **API Routes**: Build backend endpoints in `pages/api/`.
---

**Useful Links**:

- [Next.js Documentation](https://nextjs.org/docs)
- [App Router Docs](https://nextjs.org/docs/app/building-your-application/routing)
- [Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image)