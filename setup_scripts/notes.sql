
/*Automatic commits by default*/ 

/* Show FK constraints for a given table:*/

SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
	REFERENCED_TABLE_SCHEMA = 'api_sql_redis'
    AND REFERENCED_TABLE_NAME = 'users';

/* Disable / enable FK constraints */
SET FOREIGN_KEY_CHECKS=0;
SET FOREIGN_KEY_CHECKS=1;