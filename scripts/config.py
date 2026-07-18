from pathlib import Path

CONTENT_TYPES = {

    "posts": {

        "incoming": Path("drafts/incoming/posts"),
        "processed": Path("drafts/processed/posts"),
        "output": Path("_posts"),

        "layout": "post",

        "image_root": "/assets/images/posts",

        "list_fields": [
            "Authors",
            "Projects",
            "Tags"
        ],

        "required_columns": [
            "title",
            "authors",
            "projects"
        ],

        "relationships": {
            "authors": "people",
            "projects": "projects"
        }

    },


    "people": {

        "incoming": Path("drafts/incoming/people"),
        "processed": Path("drafts/processed/people"),
        "output": Path("_people"),

        "layout": "person",

        "image_root": "/assets/images/people",
        
        "list_fields": [
            "Projects"
        ],

        "required_columns": [
            "Name",
            "Biography"
        ],

        "relationships": {

            "projects": "projects"

        },

        "identifier": "Name",
        "body_field": "Biography"
    },


    "projects": {

        "incoming": Path("drafts/incoming/projects"),
        "processed": Path("drafts/processed/projects"),
        "output": Path("_projects"),

        "layout": "project",

        "image_root": "/assets/images/projects",

        "list_fields": [
            "Tags",
            "People"
        ],

        "required_columns": [
            "Title",
            "Description",
            "People"
        ],
        
        "relationships": {
            "people": "people"
        },

        "identifier": "Title",
        "body_field": "Description"
    }

}