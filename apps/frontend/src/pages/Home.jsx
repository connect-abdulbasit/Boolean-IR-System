import React from 'react';
import SearchBar from '../components/SearchBar';
import Results from '../components/Results';
import { api } from '../services/api';
import { useSearch } from '../context/SearchContext';

export default function Home() {
  const {
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
  } = useSearch();

  const handleSearch = async (query) => {
    setLoading(true);
    setError('');
    setResults([]);
    setSearchQuery(query);
    setHasSearched(true);

    try {
      const data = await api.search(query);
      setResults(data.documents || []);
      if (data.documents.length === 0) {
        setError('No documents found');
      }
    } catch (err) {
      setError(`Search failed: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center">
      {!hasSearched ? (
        <div className="flex flex-col items-center justify-center min-h-[80vh] w-full max-w-2xl px-4">
          <div className="mb-8 text-6xl font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">
            Boolean IR
          </div>
          <SearchBar onSearch={handleSearch} loading={loading} />
        </div>
      ) : (
        <div className="w-full">
          <div className="sticky top-0 z-10 flex items-center gap-8 px-6 py-4 bg-white border-b border-gray-200 shadow-sm md:px-10 lg:px-20">
            <div 
              className="text-2xl font-bold border-none cursor-pointer text-blue-600 hover:opacity-80 transition-opacity" 
              onClick={clearSearch}
            >
              Boolean IR
            </div>
            <div className="flex-1 max-w-2xl">
              <SearchBar onSearch={handleSearch} loading={loading} />
            </div>
          </div>
          
          <main className="px-6 py-4 md:px-10 lg:px-20">
            {error && (
              <div className="p-4 mb-6 text-sm text-red-700 bg-red-100 rounded-lg border border-red-200">
                {error}
              </div>
            )}
            
            {loading && (
              <div className="flex items-center gap-3 py-4 text-gray-500">
                <div className="w-5 h-5 border-2 border-blue-500 rounded-full border-t-transparent animate-spin"></div>
                <span>Searching for results...</span>
              </div>
            )}
            
            {!loading && results.length > 0 && (
              <div className="mb-6 text-sm text-gray-500">
                Found {results.length} relevant documents
              </div>
            )}
            
            <Results documents={results} loading={loading} />
          </main>
        </div>
      )}
    </div>
  );
}
