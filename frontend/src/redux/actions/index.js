export const mobileMedia = () => {
  return {
    type: 'MOBILE',
  };
};

export const menuCollapse = () => {
  return {
    type: 'COLLAPSE',
  };
};

export const showResults = () => {
  return {
    type: 'SHOW_RESULTS',
  };
};

export const dontShowResults = () => {
  return {
    type: 'DONT_SHOW_RESULTS',
  };
};

export const setResults = (data) => {
  return {
    type: 'SET_RESULTS',
    payload: data,
  };
};

export const setQuery = (query) => {
  return {
    type: 'QUERY',
    payload: query,
  };
};

export const isLoading = () => {
  return {
    type: 'LOADING',
  };
};

export const resultsIsLoading = () => {
  return {
    type: 'RESULTS_LOADING',
  };
};

export const openTableSearch = () => {
  return {
    type: 'OPEN_TABLE_SEARCH',
  };
};

export const closeTableSearch = () => {
  return {
    type: 'CLOSE_TABLE_SERACH',
  };
};

export const denseSearchMethod = () => {
  return {
    type: 'DENSE_VECTORS',
  };
};

export const elasticSearchMethod = () => {
  return {
    type: 'ELASTIC_SEARCH',
  };
};
