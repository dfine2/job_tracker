import * as React from "react";
import styled from "@emotion/styled";

import { Box } from "@mui/material";

import { DataGrid } from "@mui/x-data-grid";

function JobsTable({ jobs }) {
  const columns = [
    { field: "company", headerName: "Company", width: 90 },
    {
      field: "title",
      headerName: "Title",
      width: 150,
      editable: true,
    },
    {
      field: "compensation",
      headerName: "Compensation",
      width: 150,
      editable: true,
    },
    {
      field: "workModel",
      headerName: "Work Model",
      type: "number",
      width: 110,
      editable: true,
    },
    {
      field: "location",
      headerName: "Location",
      width: 160,
    },
    {
      field: "source",
      headerName: "Source",
      width: 160,
    },
    {
      field: "applicationStatus",
      headerName: "Application Status",
      width: 160,
    },
    {
      field: "resume",
      headerName: "Resume",
      width: 160,
    },
    {
      field: "coverLetter",
      headerName: "Cover Letter",
      width: 160,
    },
  ];
  const rows = jobs.map((_job, index) => {
    const job = JSON.parse(_job);
    console.log(job);
    return {
      id: index,
      company: job.company_name,
      title: job.title,
      compensation: `$${job.compensation_low}-$${job.compensation_high}`,
      workModel: job.work_model,
      location: job.location,
      source: job.source,
      applicationStatus: job.application_status,
    };
  });

  return (
    <Box container sx={{ height: 400, width: 1500 }}>
      <DataGrid
        rows={rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }}
        pageSizeOptions={[5]}
        checkboxSelection
        disableRowSelectionOnClick
      />
    </Box>
  );
}

export default JobsTable