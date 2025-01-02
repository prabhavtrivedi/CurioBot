// Function to measure and report web performance metrics
const reportWebVitals = onPerfEntry => {
  // Check if onPerfEntry is provided and is a valid function
  if (onPerfEntry && onPerfEntry instanceof Function) {
    // Dynamically import the web-vitals library
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      // Measure and pass each web vital metric to the provided callback
      getCLS(onPerfEntry);  // Measures Cumulative Layout Shift (CLS)
      getFID(onPerfEntry);  // Measures First Input Delay (FID)
      getFCP(onPerfEntry);  // Measures First Contentful Paint (FCP)
      getLCP(onPerfEntry);  // Measures Largest Contentful Paint (LCP)
      getTTFB(onPerfEntry); // Measures Time to First Byte (TTFB)
    });
  }
};

// Export the function for use in the app
export default reportWebVitals;
