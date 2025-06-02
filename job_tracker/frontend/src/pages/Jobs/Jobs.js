// Filename - App.js

// Importing modules
import { useState, useEffect } from "react";

import styled from "@emotion/styled";
import JobsTable from "./components/JobTable";
import { Grid } from "@mui/material";

const StyledGrid = styled(Grid)(({ theme }) => ({
  backgroundColor: "#fff",
  border: "3px inset #e0e0e0",
  borderRadius: "12px",
  boxShadow: "3px 10px 10px hsla(0, 71.40%, 1.40%, 0.61)",
  padding: 4,
  display: "flex",

  overflow: "auto",
  fontFamily: "Arial, sans-serif",
}));



function Jobs() {
  const [jobs, setJobs] = useState([]);
  useEffect(() => {
    fetch("/jobs")
      .then((res) => {
        return res.json();
      })
      .then((jobs) => {
        console.log(jobs);
        setJobs(jobs);
      });
  }, []);

  return (
    <StyledGrid container spacing={2}>
      <Grid sx={{ padding: "8px" }}>
        <JobsTable jobs={jobs}></JobsTable>
      </Grid>
    </StyledGrid>
  );
}

export default Jobs;