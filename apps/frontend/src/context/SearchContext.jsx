import React, { createContext, useContext, useState } from 'react';

const SearchContext = createContext();

export function SearchProvider({ children }) {
  const [results, setResults] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [hasSearched, setHasSearched] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const clearSearch = () => {
    setResults([]);
    setSearchQuery('');
    setHasSearched(false);
    setError('');
  };

  return (
    <SearchContext.Provider value={{
      results,
      setResults,
      searchQuery,
      setSearchQuery,
      hasSearched,
      setHasSearched,
      loading,
      setLoading,
      error,
      setError,
      clearSearch,
    }}>
      {children}
    </SearchContext.Provider>
  );
}

export function useSearch() {
  const context = useContext(SearchContext);
  if (!context) {
    throw new Error('useSearch must be used within a SearchProvider');
  }
  return context;
}
