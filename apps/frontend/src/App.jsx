import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import DocumentDetail from './pages/DocumentDetail';
import { SearchProvider } from './context/SearchContext';

export default function App() {
  return (
    <BrowserRouter>
      <SearchProvider>
        <div className="min-h-screen bg-gray-50 selection:bg-blue-100">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/document/:docId" element={<DocumentDetail />} />
          </Routes>
        </div>
      </SearchProvider>
    </BrowserRouter>
  );
}
