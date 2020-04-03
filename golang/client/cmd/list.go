package cmd

import (
	"context"
	"fmt"
	"io"

	blogpb "../../../proto"
	"github.com/spf13/cobra"
)

// listCmd represents the read command
var listCmd = &cobra.Command{
	Use:   "list",
	Short: "List all blog posts",
	RunE: func(cmd *cobra.Command, args []string) error {
		// Create the request (this can be inline below too)
		req := &blogpb.ListBlogsReq{}
		// Call ListBlogs that returns a stream
		stream, err := client.ListBlogs(context.Background(), req)
		// Check for errors
		if err != nil {
			return err
		}
		// Start iterating
		for {
			// stream.Recv returns a pointer to a ListBlogRes at the current iteration
			res, err := stream.Recv()
			// If end of stream, break the loop
			if err == io.EOF {
				break
			}
			// if err, return an error
			if err != nil {
				return err
			}
			// If everything went well use the generated getter to print the blog message
			fmt.Println(res.GetBlog())
		}
		return nil
	},
}

func init() {
	rootCmd.AddCommand(listCmd)
}
