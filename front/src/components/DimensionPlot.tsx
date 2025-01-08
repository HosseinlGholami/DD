// src/components/DimensionPlot.tsx
import React from "react";
import Plot from "react-plotly.js";

interface PlotData {
  x: number[];
  y: number[];
  z: number[];
}

interface DimensionPlotProps {
  plotData: PlotData;
}

const DimensionPlot: React.FC<DimensionPlotProps> = ({ plotData }) => {
  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        position: "relative",
        overflow: "hidden",
      }}
    >
      <Plot
        style={{ width: "100%", height: "100%" }}
        useResizeHandler={true}
        config={{ responsive: true }}
        data={[
          {
            x: plotData.x,
            y: plotData.y,
            z: plotData.z,
            mode: "markers",
            marker: {
              size: 5, // Adjust the size as needed
              color: "rgba(0, 0, 0, 1)", // Color of the points
              opacity: 0.8,
            },
            type: "scatter3d",
            name: "Dimension Points",
          },
        ]}
        layout={{
          margin: { t: 0, b: 0, l: 0, r: 0 },
          scene: {
            xaxis: { title: "X Axis", range: [-500, 500] },
            yaxis: { title: "Y Axis", range: [0, 800] },
            zaxis: { title: "Z Axis", range: [-700, -100] },
            camera: {
              eye: {
                x: -1.5,
                y: -1.5,
                z: 2,
              },
            },
          },
        }}
      />
    </div>
  );
};

export default DimensionPlot;
